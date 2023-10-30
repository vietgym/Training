#list (danh sách) là ctdl lưu trữ 1 tập hợp phần tử
#tạo
my_list = [1, 2, 3, "Hello", 5]
empty_list = []

first_element = my_list[0] #truy cập phần tử đầu tiên
my_list[4] = "world" #gán gt pt

last_elememt = 6
my_list.append(last_elememt) #thêm pt vào cuối ds
my_list.insert(2, "Insert ne") #chèn

my_list.remove('Hello')  # Xóa phần tử có giá trị 'Hello'
del my_list[1]  # Xóa phần tử
popped_value = my_list.pop(2)  # Xóa phần tử trả về giá trị

length = len(my_list) #độ dài ds

#my_list.sort()  # Sắp xếp tăng dần
my_list.reverse()  # Đảo ngược các phần tử

for i in range(len(my_list)): #duyệt
    print(my_list[i])

print(my_list)