# Nhập x và n, tính S(x,n)
def compute_S(x, n):
    if n < 0:
        raise ValueError("n phải là số nguyên >= 0")
    # hạng đầu tiên T0 = x (k = 0)
    term = x
    S = term
    # lặp k = 1..n để cộng các hạng tiếp theo
    for k in range(1, n + 1):
        term *= (x * x) / (2 * k * (2 * k + 1))
        S += term
    return S

if __name__ == "__main__":
    try:
        x = float(input("Nhập x: "))
        n = int(input("Nhập n (số nguyên không âm): "))
        result = compute_S(x, n)
        print("S(x,n) =", result)
    except Exception as e:
        print("Lỗi:", e)
# Câu 19: Viết hàm tính S(x,n) = x + x^3/3! + x^5/5! + ... + x^(2n+1)/(2n+1)!