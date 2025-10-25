def tong_uoc_so(n):
    """Tính tổng các ước số của n (không kể n)"""
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong

def la_so_hoan_thien(n):
    """Kiểm tra n có phải số hoàn thiện không"""
    return tong_uoc_so(n) == n

def la_so_thinh_vuong(n):
    """Kiểm tra n có phải số thịnh vượng không"""
    return tong_uoc_so(n) > n

# Ví dụ sử dụng:
n = int(input("Nhập số nguyên dương n: "))
if la_so_hoan_thien(n):
    print(f"{n} là số hoàn thiện")
elif la_so_thinh_vuong(n):
    print(f"{n} là số thịnh vượng")
else:
    print(f"{n} không phải là số hoàn thiện hay thịnh vượng")