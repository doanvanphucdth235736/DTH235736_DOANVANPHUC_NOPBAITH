def month_to_quarter(month: int) -> str:
	if not 1 <= month <= 12:
		raise ValueError("Tháng phải nằm trong 1..12")
	if 1 <= month <= 3:
		return "Quý 1"
	if 4 <= month <= 6:
		return "Quý 2"
	if 7 <= month <= 9:
		return "Quý 3"
	return "Quý 4"


if __name__ == "__main__":
	import sys

	try:
		if len(sys.argv) >= 2:
			m = int(sys.argv[1])
		else:
			s = input("Nhập tháng (1-12): ").strip()
			m = int(s)

		print(month_to_quarter(m))
	except Exception as e:
		print("Lỗi:", e)

