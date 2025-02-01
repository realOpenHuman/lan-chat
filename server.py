from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# 添加客户端映射和IP-编号映射
clients = {}
ip_numbers = {}
client_counter = 0

# 加载已存在的IP-编号映射
def load_ip_numbers():
    global client_counter
    if os.path.exists('ip_numbers.json'):
        with open('ip_numbers.json', 'r') as f:
            ip_numbers.update(json.load(f))
            client_counter = max(ip_numbers.values(), default=0)

# 保存IP-编号映射
def save_ip_numbers():
    with open('ip_numbers.json', 'w') as f:
        json.dump(ip_numbers, f)

# 程序启动时加载映射
load_ip_numbers()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    global client_counter
    client_ip = request.remote_addr
    
    # 如果IP地址未分配编号，则分配新编号
    if client_ip not in ip_numbers:
        client_counter += 1
        ip_numbers[client_ip] = client_counter
        save_ip_numbers()
    
    # 记录当前连接的客户端信息
    clients[request.sid] = {
        'number': ip_numbers[client_ip],
        'ip': client_ip
    }
    print(f'客户端 #{ip_numbers[client_ip]} ({client_ip}) 已连接')

@socketio.on('disconnect')
def handle_disconnect():
    if request.sid in clients:
        print(f'客户端 #{clients[request.sid]["number"]} ({clients[request.sid]["ip"]}) 已断开连接')
        del clients[request.sid]

@socketio.on('message')
def handle_message(data):
    client_num = clients[request.sid]['number']
    formatted_message = f'#{client_num}: {data}'
    print(f'收到来自客户端的消息: {formatted_message}')
    emit('response', formatted_message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)