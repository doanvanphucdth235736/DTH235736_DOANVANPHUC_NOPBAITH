cases = {
    "a": (3, 5, 7),
    "b": (3, 7, 5),
    "c": (5, 3, 7),
    "d": (5, 7, 3),
    "e": (7, 3, 5),
    "f": (7, 5, 3),
}

for key, (i, j, k) in cases.items():
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if j > k:
            j = i
        else:
            i = k
    print(f"{key}) i = {i}, j = {j}, k = {k}")