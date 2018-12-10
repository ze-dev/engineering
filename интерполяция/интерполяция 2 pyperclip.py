'''ВВести ф-ию в цикле  или рекурсию при положительном ответе'''
import pyperclip
o=''
while o == '':
    a=float(input(' Ввод     первая   отметка: '))
    b=float(input(' Ввод    вторая    отметка: '))
    c=float(input('Расстояние  между  ними: '))
    d=float(input('Длина от меньш/больш пикета (+/-): '))

    if b>a :
        if d>0:
            dh=a+((b-a)*d)/c
        if d<0:
            dh=b+((b-a)*d)/c
    if a>b :
        if d>0:
            dh=b+((a-b)*d)/c
        if d<0:
            dh=a+((a-b)*d)/c

    pyperclip.copy(str(round(dh,2)))
    print('   Отметка пиkета равна:    ', round( dh, 2) )
    print('    Скопировано в буфер:     ', pyperclip.paste())
          
    o=input('Новая интерполяция: enter,\nпродолжить текущую: 0 + enter: ')

    while o=='0':
        d=float(input('Длина от меньш/больш пикета (+/-): '))
        if b>a :
            if d>0:
                dh=a+((b-a)*d)/c
            if d<0:
                dh=b+((b-a)*d)/c
        if a>b :
            if d>0:
                dh=b+((a-b)*d)/c
            if d<0:
                dh=a+((a-b)*d)/c
        print('   Отметка пиkета равна:    ', round( dh, 2) )
        o=input('Новая интерполяция: enter,\nпродолжить текущую: 0 + enter: ')
    

    
