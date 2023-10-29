#Lambda function là 1 hàm nhỏ không cần đặt tên. Được sử dụng để định nghĩa 1 chức năng đơn giản . Thường đc kết hợp với map(), filter(), reduce()

#Lambda dùng riêng lẻ
square = lambda x: x**2
print(square(5))

add = lambda x, y: x + y
print(add(5, 9))

#Lambda dùng với map()
nums = [1, 2, 3, 4, 5]
square_nums = list(map(lambda x: x**2, nums))
print(square_nums)

#Lambda dùng với filter() (lọc)
nums = [1, 2, 3, 4, 5, 6, 7, 8]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)

#Lambda với reduce()
from functools import reduce
nums = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, nums)
print(total)