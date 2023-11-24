'''
Hãy viết một chương trình Python để quản lý một danh bạ điện thoại. Chương trình nên cho phép người dùng thực hiện các tác vụ sau:
Thêm liên hệ mới vào danh bạ với thông tin bao gồm tên, số điện thoại.
Hiển thị danh sách tất cả các liên hệ trong danh bạ.
Tìm kiếm liên hệ bằng tên và hiển thị thông tin liên hệ nếu tìm thấy.
Xóa liên hệ khỏi danh bạ bằng tên.
'''
phonebook = {}
#thêm liên hệ mới
def add_contact():
    name = input("Nhập tên: ")
    phone = input("Nhập sdt: ")
    phonebook[name] = {"SDT" : phone}
    print("Liên hệ", name, "được thêm vào danh bạ")

#hiển thị danh sách
def display():
    if not phonebook:
        print("Danh bạ trống")
    else:
        print("Danh bạ: ")
        for name, itm in phonebook.items():
            print(f"Tên: {name}, SDT: {itm['SDT']}")

#Tìm theo tên
def search():
    name_search = input("Nhập tên muốn tìm: ")
    if name_search in phonebook:
        itm = phonebook[name_search]
        print(f"Tên: {name_search}, SDT: {itm['SDT']}")
    else:
        print("Không có tên này.")

def delete():
    name_del = input("Nhập tên muốn xoá: ")
    if name_del in phonebook:
        del phonebook[name_del]
        print(f"Đã xoá {name_del} khỏi danh bạ")
    else:
        print("Không có tên này")

while True:
    print("===================================")
    print("1. Thêm liên hệ")
    print("2. Hiển thị danh bạ")
    print("3. Tìm theo tên")
    print("4. Xoá theo tên")
    print("5. Thoát")

    chois = input("Lựa chọn: ")

    if chois == "1":
        add_contact()
    elif chois == "2":
        display()
    elif chois == "3":
        search()
    elif chois == "4":
        delete()
    elif chois == "5":
        break
    else:
        print("Nhập sai")