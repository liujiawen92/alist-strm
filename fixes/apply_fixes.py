#!/usr/bin/env python3.9
"""
alist-strm 修复脚本
修复原镜像中的所有 bug
"""
import re
import os

def apply_fixes():
    fixes_applied = []

    # ========== Fix 1: 禁用自动更新 ==========
    app_py = '/app/app.py'
    with open(app_py, 'r') as f:
        content = f.read()

    if '    check_and_apply_updates()' in content and 'DISABLED' not in content:
        content = content.replace(
            '    check_and_apply_updates()',
            '    # check_and_apply_updates()  # DISABLED: auto-update causes crash loop'
        )
        with open(app_py, 'w') as f:
            f.write(content)
        fixes_applied.append('Fix 1: Disabled auto-update')

    # ========== Fix 2: 修复 python3.9 路径 ==========
    with open(app_py, 'r') as f:
        content = f.read()

    if 'command = f"python3.9 {main_script_path} {config_id}"' in content:
        content = content.replace(
            'command = f"python3.9 {main_script_path} {config_id}"',
            'command = f"/usr/local/bin/python3.9 {main_script_path} {config_id}"'
        )
        with open(app_py, 'w') as f:
            f.write(content)
        fixes_applied.append('Fix 2: Fixed python3.9 path in run_config')

    # ========== Fix 3-6: 修复 main.py ==========
    main_py = '/app/main.py'
    with open(main_py, 'r') as f:
        content = f.read()

    # Fix 3: 修复 process_with_cache 调用缺少 min_interval, max_interval
    old_call = "process_with_cache(webdav, config, script_config, config_id, script_config['size_threshold'], logger)"
    new_call = """download_interval = config.get('download_interval_range', (1, 3))
            if isinstance(download_interval, tuple):
                min_interval, max_interval = download_interval
            else:
                min_interval, max_interval = map(int, download_interval.split('-'))
            process_with_cache(webdav, config, script_config, config_id, script_config['size_threshold'], logger, min_interval, max_interval)"""

    if old_call in content and 'min_interval, max_interval = download_interval' not in content:
        content = content.replace(old_call, new_call)
        fixes_applied.append('Fix 3: Added min_interval, max_interval to process_with_cache call')

    # Fix 4: 修复参数顺序 - local_tree 应该在 min_interval 之前
    content = content.replace(
        'logger,  min_interval, max_interval, local_tree, visited=None',
        'logger, local_tree,  min_interval, max_interval, visited=None'
    )
    content = content.replace(
        'logger, min_interval, max_interval, local_tree, visited=None',
        'logger, local_tree, min_interval, max_interval, visited=None'
    )
    fixes_applied.append('Fix 4: Fixed argument order in list_files_recursive_with_cache calls')

    # Fix 5: 添加 get_jwt_token 重试逻辑
    # 找到 get_jwt_token 函数并替换
    func_pattern = r'def get_jwt_token\(url, username, password, logger\):.*?(?=\ndef |\nclass |$)'
    match = re.search(func_pattern, content, re.DOTALL)

    if match and 'retries=3' not in match.group(0):
        new_func = '''def get_jwt_token(url, username, password, logger, retries=3):
    import time
    api_url = f"{url}/api/auth/login"
    payload = {"username": username, "password": password}

    for attempt in range(retries):
        try:
            response = requests.post(api_url, json=payload, timeout=15)
            if response.status_code == 200:
                data = response.json()
                if data.get('code') == 200 and data.get('data') and data['data'].get('token'):
                    return data['data']['token']
                else:
                    logger.warning(f"Get Token failed (attempt {attempt+1}/{retries}): {data.get('message')}")
            else:
                logger.warning(f"Get Token HTTP error (attempt {attempt+1}/{retries}): {response.status_code}")
        except Exception as e:
            logger.warning(f"Request Token error (attempt {attempt+1}/{retries}): {e}")

        if attempt < retries - 1:
            time.sleep(2)

    logger.error(f"Get JWT Token failed after {retries} retries")
    return None

'''
        content = content[:match.start()] + new_func + content[match.end():]
        fixes_applied.append('Fix 5: Added retry logic to get_jwt_token')

    with open(main_py, 'w') as f:
        f.write(content)

    # 打印修复摘要
    print("=" * 50)
    print("alist-strm fixes applied:")
    for fix in fixes_applied:
        print(f"  [OK] {fix}")
    print("=" * 50)
    print(f"Total: {len(fixes_applied)} fixes applied")

if __name__ == '__main__':
    apply_fixes()
