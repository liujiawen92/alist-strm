# 快速开始指南

## 选项 1: Docker Hub（推荐）

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

---

## 选项 2: GitHub Container Registry

```bash
# 登录
echo YOUR_GITHUB_TOKEN | docker login ghcr.io -u liujiawen92 --password-stdin

# 拉取
docker pull ghcr.io/liujiawen92/alist-strm-fixed:latest
```

---

## 选项 3: 使用群晖 NAS 直接构建

```bash
# SSH 登录群晖后
cd /tmp
git clone https://github.com/liujiawen92/alist-strm-fixed.git
cd alist-strm-fixed

# 构建
docker build -t alist-strm-fixed:latest .

# 不需要推送，直接使用本地镜像
```

然后在群晖 Docker 中使用 `alist-strm-fixed:latest` 镜像创建容器。
