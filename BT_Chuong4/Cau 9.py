def S(n):
    if n == 1:
        return 2 ** 0.5
    return (2 + S(n - 1)) ** 0.5

# Ví dụ:
n = int(input("Nhập n: "))
print(f"S({n}) = {S(n)}")