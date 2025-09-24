# Boolean expression checks for x, y, z = 3, 5, 7
x = 3
y = 5
z = 7

expressions = {
	'(a) x == 3': x == 3,
	'(b) x < y': x < y,
	'(c) x >= y': x >= y,
	'(d) x <= y': x <= y,
	'(e) x != y - 2': x != y - 2,
	'(f) x < 10': x < 10,
	'(g) x >= 0 and x < 10': x >= 0 and x < 10,
	'(h) x < 0 and x < 10': x < 0 and x < 10,
	'(i) x >= 0 and x < 2': x >= 0 and x < 2,
	'(j) x < 0 or x < 10': x < 0 or x < 10,
	'(k) x > 0 or x < 10': x > 0 or x < 10,
	'(l) x < 0 or x > 10': x < 0 or x > 10,
}

for label, result in expressions.items():
	print(f"{label}: {result}")

