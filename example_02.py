def sum(n,m):
    if n == 0:
        return m
    else:
        return sum(n - 1, m + 1)

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
print(sum(a,b))