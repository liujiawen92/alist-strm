# 快速开始指南

## 选项 1: Docker Hub（推荐）

### 1. 准备
- 在 https://hub.docker.com 注册账号
- 创建 Access Token（Settings -> Security -> New Access Token）

### 2. 本地构建并推送
```bash
# 登录 Docker Hub
docker login

# 构建
docker build -t YOUR_DOCKERHUB_USERNAME/alist-strm-fixed:latest .

# 推送
docker push YOUR_DOCKERHUB_USERNAME/alist-strm-fixed:latest
```

### 3. 使用
```bash
docker pull YOUR_DOCKERHUB_USERNAME/alist-strm-fixed:latest
```

---

## 选项 2: GitHub Container Registry

### 1. 准备
- 在 GitHub 创建 Personal Access Token（Settings -> Developer settings -> Personal access tokens -> Tokens (classic)）
- 勾选 `write:packages` 权限

### 2. 本地构建并推送
```bash
# 登录 GitHub Container Registry
echo YOUR_GITHUB_TOKEN | docker login ghcr.io -u YOUR_GITHUB_USERNAME --password-stdin

# 构建并标记
docker build -t ghcr.io/YOUR_GITHUB_USERNAME/alist-strm-fixed:latest .

# 推送
docker push ghcr.io/YOUR_GITHUB_USERNAME/alist-strm-fixed:latest
```

### 3. 使用
```bash
docker pull ghcr.io/YOUR_GITHUB_USERNAME/alist-strm-fixed:latest
```

---

## 选项 3: 使用群晖 NAS 直接构建

如果你有群晖 Docker，可以在群晖上直接构建：

```bash
# SSH 登录群晖后
cd /tmp
git clone YOUR_REPO_URL
cd alist-strm-fixed

# 构建
docker build -t alist-strm-fixed:latest .

# 不需要推送，直接使用本地镜像
```

然后在群晖 Docker 中使用 `alist-strm-fixed:latest` 镜像创建容器。
