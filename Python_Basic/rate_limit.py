#rate limit (giới hạn tốc độ) được sử dụng ể giới hạn sô lượng yêu cầu hoặc thao tác được thực hiện trong 1 khoảng thời gian cụ thể để tránh quá tải

#dùng thư viện có sẵn
from ratelimit import limits, sleep_and_retry
@sleep_and_retry
@limits(calls=2, period=3)  # 2 yêu cầu mỗi 3 giây
def make_api_request():
    print("Thực hiện API thành công")
for _ in range(5):
    make_api_request()


import time
# Định nghĩa một decorator để thực hiện rate limiting
def rate_limit(limit, interval):
    def decorator(func):
        last_called = [0]
        def wrapper(*args, **kwargs):
            now = time.time()
            if now - last_called[0] < interval:
                print(f"Rate limited: Chờ {interval - (now - last_called[0]):.2f} giây trước khi thử lại.")
                return None
            result = func(*args, **kwargs)
            last_called[0] = time.time()
            return result
        return wrapper
    return decorator

# Sử dụng decorator rate_limit
@rate_limit(limit=2, interval=5)  # Giới hạn 2 lần gọi mỗi 5 giây
def api_request():
    print("Thực hiện yêu cầu API thành công.")
for _ in range(5):
    api_request()