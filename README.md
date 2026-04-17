# alist-strm-fixed

[![Docker Pulls](https://img.shields.io/docker/pulls/liujiawen92/alist-strm-fixed?style=flat-square&logo=docker)](https://hub.docker.com/r/liujiawen92/alist-strm-fixed)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/liujiawen92/alist-strm-fixed/docker-build.yml?style=flat-square&logo=github)](https://github.com/liujiawen92/alist-strm-fixed/actions)
[![GitHub last commit](https://img.shields.io/github/last-commit/liujiawen92/alist-strm-fixed?style=flat-square&logo=github)](https://github.com/liujiawen92/alist-strm-fixed)
[![GitHub License](https://img.shields.io/github/license/liujiawen92/alist-strm-fixed?style=flat-square&logo=github)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-amd64%20%7C%20arm64-blue?style=flat-square&logo=linux)]()

基于 [itefuir/alist-strm](https://hub.docker.com/r/itefuir/alist-strm) 的修复版本，解决原镜像中的崩溃循环和参数缺失问题，并提供现代化深色主题管理界面。

## v2.0 新特性（Bootstrap 5 深色主题 UI）

- 🎨 **Bootstrap 5 深色主题** - 护眼深色界面，紫罗兰色点缀
- 📱 **响应式布局** - 支持桌面和移动端
- ✅ **全页面兼容** - 首页、配置管理、定时任务、设置、关于等所有页面完整支持
- 🔐 **安全认证页** - 独立的深色主题登录/注册/忘记密码页面
- ⚡ **零崩溃** - 禁用自动更新，彻底解决崩溃循环

## 修复内容

1. **禁用自动更新** - 避免因更新服务器连接失败导致的崩溃循环
2. **修复 python3.9 路径** - 使用完整路径避免 subprocess 找不到命令
3. **修复 process_with_cache 参数缺失** - 补充 min_interval 和 max_interval 参数
4. **修复函数参数顺序** - local_tree 应在 min_interval 之前
5. **添加 JWT Token 获取重试** - 网络波动时自动重试 3 次
6. **Bootstrap 5 深色主题 UI** - 现代化管理界面（v2.0 新增）

## 快速开始

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
      - "8080:5000"
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

## 登录账号

首次部署后请通过 Web 界面（忘记密码）功能设置账号，或通过环境变量 `SECURITY_CODE` 重置。

## 环境变量

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `SECRET_KEY` | Flask 加密密钥 | 随机生成 |
| `SECURITY_CODE` | 重置密码安全码 | 随机生成 |
| `WEB_PORT` | Web 服务端口 | `5000` |

## 版本标签

## 本地构建

```bash
# 克隆仓库
git clone https://github.com/liujiawen92/alist-strm-fixed.git
cd alist-strm-fixed

# 构建并推送
./build.sh
```

## 相关项目

- [itefuir/alist-strm](https://github.com/tefuirZ/alist-strm) - 原项目
- [Docker Hub](https://hub.docker.com/r/liujiawen92/alist-strm-fixed) - 镜像地址

## License

MIT License - 详见 [LICENSE](LICENSE) 文件
