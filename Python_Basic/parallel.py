#parallel (song song): thực hiện nhiều công việc cùng lúc thay vì thực hiện tuần tự. Tính toán trên nhiều máy tính hoặc lõi cpu cùng lúc

#Multithreading dùng threading để tạo & quản lý các luồng (threads) riêng biệt
#MultiprocessingL dùng multiprocessing tạo các tiến trình riêng biệt, phù hợp tính toán nặng
from multiprocessing import Pool
#Asyncio dùng asyncio lập trình đồng bộ doroutine và event loop
#Thư viện như concurrent.futures, joblib, Ray
from concurrent.futures import ThreadPoolExecutor

def calculate_sum(file):
    return 1
    # Tính toán tổng của tệp và trả về kết quả

file_list = ["file1.txt", "file2.txt", ..., "file10.txt"]
with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(calculate_sum, file_list))




