N = int(input())
i = 1
s = 0
while i <= N:
    a = 1 / (i**2)
    s = s + a
    i = i + 1
print('{0:.5f}'.format(s))
