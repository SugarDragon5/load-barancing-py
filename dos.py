import requests
import time

# ターゲットURL
url = 'http://127.0.0.1:5000'

# リクエストを送信する回数
num_requests = 100

# リクエストを送信する間隔（秒）
interval = 0.01  # 10ミリ秒

def send_requests():
    for i in range(num_requests):
        try:
            response = requests.get(url)
            print(f'Request {i + 1}: {response.status_code} - {response.text}')
        except requests.exceptions.RequestException as e:
            print(f'Request {i + 1} failed: {e}')
        time.sleep(interval)

if __name__ == '__main__':
    start = time.time()
    send_requests()
    end = time.time()
    print(f'Total time: {end - start} seconds')
