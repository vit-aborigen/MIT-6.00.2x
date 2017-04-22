def isInt(value):
    return isinstance(value, int)

a = [1, 2, 'b', 'sdfsd', 3, 'sdf', 4, 5]

b = [value for value in a if isInt(value)]
for i in b:
    b.append(i)
    print(b)