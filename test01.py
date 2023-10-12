n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

x = "".join(map(str, n[:3]))

s = "(" + "".join(map(str, n[:3])) + ") " + "".join(map(str, n[3:6])) + "-" + "".join(map(str, n[6:]))
print (s)
