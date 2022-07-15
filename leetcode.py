arr = []
print('Vash spisok: ')
for i in range(1, 21):
    print(i, end=', ')
    arr.append(i)
sum = ''
spisok = []
for i in arr:
    sum += str(i)
for i in sum:
    spisok.append(i)
chislo = int(input('\nВведите число: '))
print(spisok[chislo-1])
