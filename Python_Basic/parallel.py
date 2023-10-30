#parallel (song song): thực hiện nhiều công việc cùng lúc thay vì thực hiện tuần tự. Tính toán trên nhiều máy tính hoặc lõi cpu cùng lúc

#Multithreading dùng threading để tạo & quản lý các luồng (threads) riêng biệt
#MultiprocessingL dùng multiprocessing tạo các tiến trình riêng biệt, phù hợp tính toán nặng
from multiprocessing import Pool
#Asyncio dùng asyncio lập trình đồng bộ doroutine và event loop
#Thư viện như concurrent.futures, joblib, Ray
import concurrent.futures
def process_data(data):
    result = data ** 2
    print(f"Xử lý dữ liệu {data}: Kết quả = {result}")
data = [1, 2, 3, 4, 5]
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(process_data, data)



