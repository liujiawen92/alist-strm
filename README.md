# alist-strm

基于 [itefuir/alist-strm](https://hub.docker.com/r/itefuir/alist-strm) 的修复版本，解决原镜像中的崩溃循环和参数缺失问题。

## 修复内容

1. **禁用自动更新** - 避免因更新服务器连接失败导致的崩溃循环
2. **修复 python3.9 路径** - 使用完整路径避免 subprocess 找不到命令
3. **修复 process_with_cache 参数缺失** - 补充 min_interval 和 max_interval 参数
4. **修复函数参数顺序** - local_tree 应在 min_interval 之前
5. **添加 JWT Token 获取重试** - 网络波动时自动重试 3 次

## 使用方法

### Docker Hub

```bash
docker pull liujiawen92/alist-strm-fixed:latest
```

### docker-compose.yml

```yaml
version: '3'
services:
  alist-strm:
    image: liujiawen92/alist-strm-fixed:latest
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

## 版本标签

| Tag | 说明 |
|-----|------|
| `latest` | 最新版本 |
| `6.0.8-fixed` | 当前修复版本（基于 alist-strm 6.0.8） |

## 本地构建

```bash
# 构建
docker build -t alist-strm-fixed:latest .

# 标记
docker tag alist-strm-fixed:latest liujiawen92/alist-strm-fixed:latest

# 推送
docker push liujiawen92/alist-strm-fixed:latest
```

## GitHub Actions 自动构建

每次推送到 master 分支会自动构建并推送镜像到 Docker Hub（amd64 + arm64 双架构）。

## 相关项目

- [itefuir/alist-strm](https://github.com/tefuirZ/alist-strm) - 原项目
- [Docker Hub](https://hub.docker.com/r/liujiawen92/alist-strm-fixed) - 镜像地址

## License

MIT License
