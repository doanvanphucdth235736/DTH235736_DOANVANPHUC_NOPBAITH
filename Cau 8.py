# Các loại lỗi khi lập trình Python và cách bắt lỗi

# 1. Lỗi cú pháp (SyntaxError)
# print("Hello"  # Thiếu dấu đóng ngoặc, sẽ gây lỗi cú pháp

# 2. Lỗi thực thi (RuntimeError)
# Ví dụ: chia cho 0
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Lỗi: Chia cho 0!")

# 3. Lỗi logic (LogicError)
# Không gây lỗi chương trình nhưng cho kết quả sai
a = 5
b = 2
print("Kết quả đúng:", a / b)      # Đúng
print("Kết quả sai:", a * b)       # Sai nếu muốn chia

# Cách bắt lỗi bằng try-except
try:
    num = int(input("Nhập một số nguyên: "))
    print("Bạn vừa nhập:", num)
except ValueError:
    print("Lỗi: Bạn phải nhập một số nguyên hợp lệ!")
