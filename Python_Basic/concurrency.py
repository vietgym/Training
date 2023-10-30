#concurrent: thực hiện nhiều tác vụ đồng thời mà không nhất thiết phải cùng lúc

import concurrent.futures
import requests
urls = ["https://www.example.com", "https://www.google.com", "https://www.openai.com"]
def fetch_url(url):
    print(url)
    response = requests.get(url)
    return url, response.status_code

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(fetch_url, urls))

for url, status_code in results:
    print(f"URL: {url}, Status Code: {status_code}")
