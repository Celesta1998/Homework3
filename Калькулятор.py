print('Выберите знак!')
while True:
    a = input("Знак(+,-,*,/): ")
    if a == '0':
        break
    if a in ('+','-','*','/'):
        b = float(input("b="))
        c = float(input("c="))
        if a == '+':
            print('Ваша сумма прибавления =',"%.2f" %(b+c))
        elif a == '-':
            print('Ваша сумма вычитания ='"%.2f" %(b-c))
        elif a == '*':
            print('Ваша сумма умножения ='"%.2f" %(b*c))
        elif a == '/':
            if c != 0:
                print('Ваша сумма разделения ='".2f" %(b/c))
            else:
                print('Деление на ноль невозможно!')
    else:
        print('Ты не выбрал знак Олень!!!','\nВведи чёртов знак а не букву или цифру')
