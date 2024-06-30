import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# バックエンドサーバーのリスト
servers = [
    'http://127.0.0.1:5001',
    'http://127.0.0.1:5002'
]
current_server = 0

async def request_server(server, path):
    try:
        response = requests.get(server + path)
        return response.text
    except requests.exceptions.RequestException as e:
        return str(e), 500

@app.route('/')
def load_balancer():
    global current_server
    try:
        response = request_server(servers[current_server], request.path)
        current_server = (current_server + 1) % len(servers)
        return response
    except requests.exceptions.RequestException as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
