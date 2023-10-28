#Dictionary (từ điển) là 1 cấu trúc dữ liệu theo cặp key-value.
def dis(product):
    print("-----------------------")
    for key, value in product.items():
        print(key, ":", value)

#Khởi tạo
product = {
    "name" : "jean",
    "cost" : 30.99,
    "color" : "white",
    "size" : "M",
}
dis(product)

#Thay đổi thông tin
product["cost"] = 15.99

#Thêm thông tin
product["nsx"] = "2023-28-10"

#xoá thông tin
del product["size"]

dis(product)