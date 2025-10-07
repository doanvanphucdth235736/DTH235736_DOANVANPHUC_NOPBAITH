
import sys

def compute_S(x: float, n: int) -> float:
    """Compute S(x,n) = sum_{k=1..n} x^k / k! using iterative term."""
    s = 0.0
    term = 1.0
    for k in range(1, n+1):
        term = term * x / k
        s += term
    return s

def parse_args_or_prompt():
    if len(sys.argv) >= 3:
        try:
            x = float(sys.argv[1])
            n = int(sys.argv[2])
            if n < 1:
                raise ValueError
            return x, n
        except ValueError:
            print("Tham số không hợp lệ. Dùng: python Cau 10.py [x] [n]")
            sys.exit(1)

    # Prompt mode
    while True:
        raw_x = input("Nhập x (số thực): ").strip()
        try:
            x = float(raw_x)
            break
        except ValueError:
            print("Giá trị x không hợp lệ. Thử lại.")
    while True:
        raw_n = input("Nhập n (số nguyên dương >=1): ").strip()
        try:
            n = int(raw_n)
            if n < 1:
                raise ValueError
            break
        except ValueError:
            print("Giá trị n không hợp lệ. Thử lại.")
    return x, n

def main():
    x, n = parse_args_or_prompt()
    s = compute_S(x, n)
    print(f"S(x,n) với x={x} và n={n} = {s}")

if __name__ == '__main__':
    main()
