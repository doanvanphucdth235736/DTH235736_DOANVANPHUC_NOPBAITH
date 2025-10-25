# Hàm đệ quy trả về số Fibonacci tại vị trí n
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Hàm trả về danh sách dãy số Fibonacci từ 1 đến n
def listfibo(n):
    for i in range(1, n + 1):
        print(fibonacci(i), end='\t')
    print()  # Xuống dòng sau khi in hết

# Thử chạy
print("Fibonacci(9) =", fibonacci(9))   # In ra số Fib tại vị trí thứ 9
print("Dãy Fibonacci tới 9 số:")
listfibo(9)                             # In ra dãy Fibonacci từ 1 đến 9
