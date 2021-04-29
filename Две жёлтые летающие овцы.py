print('Угадайте число которое я загадал: ','\nЧтобы угадать я вам дам подсказку','\nЧисла больше 0 и меньше 100',
          '\nУдачи!')
user_number = int(input())
a = 42
b = range(int(40-45))
c = range(46,51)
d = range(35,39)
e = range(0,34)
f = range(51,100)
if user_number == a:
    print('Неревоятно!','\nВы угадали!!!')
elif user_number == b:
    print('Жарко! Вы очень близки к правильному ответу')
elif user_number == d:
    print('Тепло! Вы близки к ответу')
elif user_number == c:
    print('Тёпленько! Вы близки к истинному ответу')
elif user_number == e:
    print('Действительно холодно! Вы очень отдалены от правильного ответа')
elif user_number == f:
    print('Холодно! Вы далеко от правильного ответа')


