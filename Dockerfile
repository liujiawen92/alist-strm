# alist-strm-fixed Dockerfile
# 基于原镜像，应用所有必要修复
#
# v2.0 - Bootstrap 5 深色主题 UI + 全模板优化
#   - 全新 Bootstrap 5 深色主题管理界面
#   - 所有模板兼容 app.py 变量架构
#   - 禁用崩溃自动更新，修复参数缺失，JWT 重试

FROM itefuir/alist-strm:latest

# 复制修复脚本
COPY fixes/ /tmp/fixes/

# 应用所有 Python 代码修复（禁用自动更新、修复路径、修复参数等）
RUN python3.9 /tmp/fixes/apply_fixes.py && rm -rf /tmp/fixes

# 复制深色主题模板（覆盖原镜像内置模板）
COPY templates/ /app/templates/

# 标记修复版本
ENV FIXED_VERSION=6.0.9-ui
