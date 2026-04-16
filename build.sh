#!/bin/bash
# 本地构建脚本
# 用法: ./build.sh YOUR_DOCKERHUB_USERNAME

set -e

USERNAME=${1:-""}

if [ -z "$USERNAME" ]; then
    echo "用法: ./build.sh YOUR_DOCKERHUB_USERNAME"
    exit 1
fi

echo "构建镜像..."
docker build -t alist-strm-fixed:latest .

echo "标记镜像..."
docker tag alist-strm-fixed:latest ${USERNAME}/alist-strm-fixed:latest

echo "推送镜像到 Docker Hub..."
docker push ${USERNAME}/alist-strm-fixed:latest

echo "完成！"
echo "使用: docker pull ${USERNAME}/alist-strm-fixed:latest"
