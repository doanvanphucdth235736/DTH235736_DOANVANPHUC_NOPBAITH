print("=== TRÒ CHƠI ĐOÁN SỐ ===")
print("Người 1 nhập số bí mật (1..100): ")
somay = int(input())   # coi như "máy" chọn, thực ra là người 1 nhập
print("\n" * 50)       # xóa màn hình cho người 2 khỏi thấy số bí mật

solandoan = 0
win = False

while solandoan < 7:
    solandoan += 1
    songuoi = int(input("Người 2 đoán số [1..100]: "))
    print("Bạn đoán lần thứ", solandoan)

    if somay == songuoi:
        print("Chúc mừng bạn đoán đúng! Số bí mật là", somay)
        win = True
        break
    elif somay > songuoi:
        print("Sai rồi, số bí mật > số bạn đoán")
    else:
        print("Sai rồi, số bí mật < số bạn đoán")

if not win:
    print("GAME OVER! Số bí mật là", somay)

print("Cám ơn bạn đã chơi game!")
