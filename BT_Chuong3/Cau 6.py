def read_two_digit_number(n: int) -> str:
	"""Return Vietnamese reading for integer n in range 0..99."""
	if not (0 <= n <= 99):
		raise ValueError("Number must be between 0 and 99")

	units = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]

	if n < 10:
		return units[n]

	tens = n // 10
	u = n % 10

	tens_part = ""
	if tens == 1:
		tens_part = "mười"
	else:
		tens_part = units[tens] + " mươi"

	if u == 0:
		return tens_part

	# Special reading rules for units digit
	if u == 1:
		# after 'mươi', 'một' is often read as 'mốt'
		unit_part = "mốt" if tens >= 2 else "một"
	elif u == 4:
		# in some dialects 'bốn' -> 'tư' after 'mươi' but we'll keep 'bốn'
		unit_part = "bốn"
	elif u == 5:
		# 'năm' -> 'lăm' after 'mươi'
		unit_part = "lăm"
	else:
		unit_part = units[u]

	return f"{tens_part} {unit_part}"


if __name__ == "__main__":
	# Interactive demo: read input or show examples
	try:
		s = input("Nhập số nguyên (0-99): ").strip()
		if s == "":
			samples = [35, 5, 10, 11, 21, 40, 45, 99, 0]
			for n in samples:
				print(f"{n} -> {read_two_digit_number(n).capitalize()}")
		else:
			n = int(s)
			print(read_two_digit_number(n).capitalize())
	except Exception as e:
		print("Lỗi:", e)

