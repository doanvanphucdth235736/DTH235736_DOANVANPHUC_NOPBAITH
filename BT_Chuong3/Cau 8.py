def calculate(a, op, b):
	if op == '+':
		return a + b
	if op == '-':
		return a - b
	if op == '*':
		return a * b
	if op == '/':
		if b == 0:
			raise ZeroDivisionError('Chia cho 0')
		return a / b
	raise ValueError('Phép toán không hợp lệ')


if __name__ == '__main__':
	try:
		s = input("Nhập theo dạng: a op b (ví dụ: 3 + 5): ").strip()
		if not s:
			print('Không có dữ liệu nhập, ví dụ: 3 + 5')
		else:
			parts = s.split()
			if len(parts) != 3:
				print('Định dạng sai. Vui lòng nhập: a op b')
			else:
				a = float(parts[0])
				op = parts[1]
				b = float(parts[2])
				res = calculate(a, op, b)
				# If result is integer-valued, print as int
				if isinstance(res, float) and res.is_integer():
					res = int(res)
				print(f'Kết quả: {res}')
	except Exception as e:
		print('Lỗi:', e)


