l = []
while len(l) != 10:
    a=int(input('Введите 10 элементов списка(цифровых) ='))
    l.append(a)
print(l)
k=int(input('Индекс элемента,который будет удалён ='))
for c in range(len(l)):
    if c == k:
        for e in range(k,len(l) - 1):
            l[e],l[e+1]=l[e+1],l[e]
print(l)
print('Удалённый элемент = ',l.pop())
print('Конечный список :',l)