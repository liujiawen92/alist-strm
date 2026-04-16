# alist-strm-fixed Dockerfile
# 基于原镜像，应用所有必要修复

FROM itefuir/alist-strm:latest

# 复制修复脚本
COPY fixes/ /tmp/fixes/

# 应用所有修复
RUN python3.9 /tmp/fixes/apply_fixes.py && rm -rf /tmp/fixes

# 标记修复版本
ENV FIXED_VERSION=6.0.8-fixed
