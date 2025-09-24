def is_leap_year(year: int) -> bool:
	"""Return True if year is a leap year (Gregorian rules)."""
	return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(month: int, year: int) -> int:
	if month == 2:
		return 29 if is_leap_year(year) else 28
	if month in (1, 3, 5, 7, 8, 10, 12):
		return 31
	if month in (4, 6, 9, 11):
		return 30
	raise ValueError("Invalid month")


def next_day(day: int, month: int, year: int) -> tuple:
	d = day + 1
	mdays = days_in_month(month, year)
	if d > mdays:
		d = 1
		month += 1
		if month > 12:
			month = 1
			year += 1
	return d, month, year


if __name__ == '__main__':
	try:
		s = input("Nhập ngày theo dạng dd mm yyyy (hoặc để trống để chạy ví dụ): ").strip()
		if s == "":
			samples = [
				(28, 2, 2000),  # leap
				(28, 2, 1900),  # not leap
				(31, 12, 1999),
				(30, 4, 2021),
				(29, 2, 2020),
			]
			for d, m, y in samples:
				nd, nm, ny = next_day(d, m, y)
				print(f"{d}/{m}/{y} -> {nd}/{nm}/{ny}")
		else:
			parts = s.split()
			if len(parts) != 3:
				print("Vui lòng nhập 3 số: ngày tháng năm")
			else:
				day, month, year = map(int, parts)
				# basic validation
				if not (1 <= month <= 12):
					print("Tháng không hợp lệ")
				elif not (1 <= day <= days_in_month(month, year)):
					print("Ngày không hợp lệ cho tháng/năm đã cho")
				else:
					nd, nm, ny = next_day(day, month, year)
					print(f"Ngày kế sau: {nd}/{nm}/{ny}")
	except Exception as e:
		print("Lỗi:", e)

