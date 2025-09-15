# Một số cách nhập dữ liệu từ bàn phím trong Python

# Nhập một chuỗi
name = input("Nhập tên của bạn: ")
print("Tên bạn vừa nhập là:", name)

# Nhập một số nguyên
age = int(input("Nhập tuổi của bạn: "))
print("Tuổi bạn vừa nhập là:", age)

# Nhập nhiều giá trị trên một dòng, cách nhau bởi dấu cách
numbers = input("Nhập các số, cách nhau bởi dấu cách: ").split()
numbers = [int(num) for num in numbers]
print("Các số bạn vừa nhập là:", numbers)