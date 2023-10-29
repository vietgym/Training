'''Tuple là 1 ctdl giống list, nhưng có 1 số khác biệt:
1. Bất biến (immutable): Không thể thay đổi nội dung, không thể thêm, sửa, xoá
2. Khoá (hashable): Các tuple có thể đc sử dụng làm key trong các dictionary...
Tuple đc sử dụng để bảo vệ dữ liệu không được thay đổi hoặc dùng làm key...
'''

my_tuple = (1, 2, 3, "Hello", 5) #tạo
print(my_tuple[3]) #truy cập

for item in my_tuple: # duyệt
    print(item)

#tuple làm key trong dictionary
my_dict = {
    ("John", "Doe"): 90,
    ("Alice", "Smith"): 85,
    ("Bob", "Johnson"): 78,
}
for student, grade in my_dict.items():
    print(f"{student[0]} {student[1]}: {grade}")
