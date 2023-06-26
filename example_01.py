def func(n,m):
    if m == 0:
        return 1
    if m == 1:
        return n
    return n * func(n, m - 1)

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
print(func(a,b))