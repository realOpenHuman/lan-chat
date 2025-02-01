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
聊天界面支持:
实时消息发送和接收
按回车键快速发送
自动滚动到最新消息
文件结构
├── server.py          # 服务器主程序
├── templates/         # 前端模板目录
│   └── index.html    # 聊天界面  
└── ip_numbers.json   # IP-编号映射文件(自动生成)
注意事项
确保防火墙允许5000端口访问
首次运行会自动创建 ip_numbers.json 文件
开发环境已启用Debug模式，部署时请关闭