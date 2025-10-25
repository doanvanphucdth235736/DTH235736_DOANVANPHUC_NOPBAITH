# Hàm tính ROI
def ROI(dt, cp):
    return (dt - cp) / cp

# Hàm gợi ý đầu tư
def GoiYDauTu(roi):
    if roi >= 0.75:
        return "Nên đầu tư"
    else:
        return "Không nên đầu tư"

# Chương trình chính
print("=== Chương trình tính ROI ===")
dt = float(input("Nhập Doanh thu: "))
cp = float(input("Nhập Chi phí: "))

roi = ROI(dt, cp)

print("Tỉ lệ ROI =", roi)
print("==>", GoiYDauTu(roi))
