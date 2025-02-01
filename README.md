# 局域网聊天程序

一个基于 Flask 和 Socket.IO 的简单局域网实时聊天应用。

## 功能特点

- 支持多用户实时聊天
- 自动为每个IP地址分配唯一编号
- 持久化保存用户IP-编号映射关系
- 断线重连时保持相同的用户编号
- 基于Bootstrap的响应式Web界面

## 技术栈

- **后端**:
  - Python
  - Flask
  - Flask-SocketIO

- **前端**:
  - HTML/CSS
  - Bootstrap 4
  - jQuery
  - Socket.IO-client

## 安装步骤

1. 克隆项目到本地
2. 安装所需依赖：

```bash
pip install flask flask-socketio
```
服务器将在 http://0.0.0.0:5000 启动

## 使用说明
启动服务器后，局域网内的用户可通过服务器IP访问
每个用户会获得一个唯一的编号(#1, #2 等)
