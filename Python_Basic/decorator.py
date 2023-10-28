#Decorator (trang trí) cho phép bọc 1 hàm của 1 phương thức của đối tượng bằng 1 hàm khác. Dùng thực hiện các tác vụ như đăng nhập, ghi log, đo thời gian...

import time
# Định nghĩa một decorator để ghi lại thời gian thực thi
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} thực thi trong {execution_time} giây")
        return result
    return wrapper

# Sử dụng decorator trên một hàm
@timing_decorator
def slow_function():
    time.sleep(2)  # Giả lập một hàm mất thời gian để thực thi

# Gọi hàm đã được trang bị decorator
slow_function()


