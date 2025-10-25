def ln(y, eps=1e-10):
    if y <= 0:
        raise ValueError("Giá trị phải > 0")
    n = 1000  # Số lần lặp càng lớn càng chính xác
    x = y - 1.0
    for _ in range(n):
        x = x - (pow(2.718281828459045, x) - y) / pow(2.718281828459045, x)
    return x

def loga(x, a):
    return ln(x) / ln(a)

a = float(input("Nhập cơ số a: "))
x = float(input("Nhập số x: "))

if a > 0 and a != 1 and x > 0:
    print(f"log_{a}({x}) = {loga(x, a)}")
else:
    print("Dữ liệu không hợp lệ. Yêu cầu: a > 0, a ≠ 1, x > 0")