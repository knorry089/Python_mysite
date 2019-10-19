import keyword

print(keyword.kwlist)

dic = {x: x ** 3 for x in (2, 4, 6)}

print(dic)

print(6 * 6 * 6)

lis = [1, 2, 3, 4]
it = iter(lis)
for x in it:
    print(x, end='')
