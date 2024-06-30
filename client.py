from flask import Flask
import subprocess

app = Flask(__name__)

server_name = 0

@app.route('/')
def hello_world():
    return f'Hello from {server_name}'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
    proc = subprocess.Popen('whoami', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, stderr = proc.communicate()
    server_name = stdout
