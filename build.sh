#!/bin/bash
# 本地构建脚本
# 用法: ./build.sh [version_tag]

set -e

VERSION=${1:-"6.0.8-fixed"}
USERNAME="liujiawen92"
IMAGE="alist-strm-fixed"

echo "构建镜像..."
docker build -t ${IMAGE}:latest .

echo "标记镜像..."
docker tag ${IMAGE}:latest ${USERNAME}/${IMAGE}:latest
docker tag ${IMAGE}:latest ${USERNAME}/${IMAGE}:${VERSION}

echo "推送镜像到 Docker Hub..."
docker push ${USERNAME}/${IMAGE}:latest
docker push ${USERNAME}/${IMAGE}:${VERSION}

echo "完成！"
echo "使用: docker pull ${USERNAME}/${IMAGE}:latest"
echo "版本: docker pull ${USERNAME}/${IMAGE}:${VERSION}"
