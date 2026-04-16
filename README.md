# alist-strm-fixed

基于 [itefuir/alist-strm](https://hub.docker.com/r/itefuir/alist-strm) 的修复版本。

## 修复内容

1. **禁用自动更新** - 避免因更新服务器连接失败导致的崩溃循环
2. **修复 python3.9 路径** - 使用完整路径避免 subprocess 找不到命令
3. **修复 process_with_cache 参数缺失** - 补充 min_interval 和 max_interval 参数
4. **修复函数参数顺序** - local_tree 应在 min_interval 之前
5. **添加 JWT Token 获取重试** - 网络波动时自动重试 3 次

## 使用方法

### Docker Hub

```bash
docker pull YOUR_DOCKERHUB_USERNAME/alist-strm-fixed:latest
```

### docker-compose.yml

```yaml
version: '3'
services:
  alist-strm:
    image: YOUR_DOCKERHUB_USERNAME/alist-strm-fixed:latest
    container_name: alist-strm
    ports:
      - "5245:5000"
    environment:
      - TZ=Asia/Shanghai
      - FLASK_APP=app.py
      - FLASK_ENV=production
      - CONFIG_PATH=/config
    volumes:
      - ./video:/data/video
      - ./config:/config
    restart: unless-stopped
```

## 本地构建

```bash
# 构建
docker build -t alist-strm-fixed:latest .

# 标记
docker tag alist-strm-fixed:latest YOUR_DOCKERHUB_USERNAME/alist-strm-fixed:latest

# 推送
docker push YOUR_DOCKERHUB_USERNAME/alist-strm-fixed:latest
```

## GitHub Actions 自动构建

将此仓库推送到 GitHub，配置 Secrets：
- `DOCKER_USERNAME`: Docker Hub 用户名
- `DOCKER_PASSWORD`: Docker Hub 密码或 Access Token

每次推送到 main 分支会自动构建并推送镜像。
