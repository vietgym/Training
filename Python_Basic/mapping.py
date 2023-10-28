#Mapping (ánh xạ) sử dụng dữ liệu dictionary (từ điển) hoặc mapping object để ánh xạ các khoá tới các giá trị tương ứng
#dictionary cũng là 1 ctdl mapping
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict["name"])

#MappingView object: keys, values và items
keys = my_dict.keys()  # Trả về danh sách các key
values = my_dict.values()  # Trả về danh sách các giá trị

#defaultdict cũng là ctdl mapping
#Hàm map
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)  # Ánh xạ từ số nguyên sang bình phương
squared_numbers_list = list(squared_numbers) # Chuyển kết quả về danh sách
print(squared_numbers_list)