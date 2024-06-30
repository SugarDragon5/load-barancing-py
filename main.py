import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# バックエンドサーバーのリスト
servers = [
    'http://127.0.0.1:5000'
]
current_server = 0

@app.route('/')
def load_balancer():
    global current_server
    try:
        response = requests.get(servers[current_server])
        current_server = (current_server + 1) % len(servers)
        return response.text
    except requests.exceptions.RequestException as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
