import pyperclip
print(
''' Использовался для вычисления отметок труб и колодцев,
используя промеры по вешке максимальной высотой 2,6 на Смоленском известковом заводе'''
         )

o='0'
while o == '0':
    a=float(input('Ввод верх отметка  колодца: '))
    b=float(input('  Ввод отсчет по вешке : '))
    c=2.6-b+1.39
    print('     Глубина точки равна:    ', round( c, 2) )
    print('     Отметка точки равна:    ', round( (a-c), 2) )
    d=str(round( (a-c), 2))
    pyperclip.copy( d )
    print('    Скопировано   в   буфер:  ', pyperclip.paste()  )
    o=input('след. труба: enter,\nновый колодец: 0 + enter: ')

    while o=='':
        b=float(input(' Ввод следующий отсчет по вешке : '))
        c=2.6-b+1.39
        print('   Глубина точки равна:    ', round( c, 2) )
        print('   Отметка точки равна:    ', round( (a-c), 2) )
        d=str(round( (a-c), 2))
        pyperclip.copy( d )
        print('    Скопировано   в   буфер:  ', pyperclip.paste()  )
        o=input('след. труба: enter,\nновый колодец: 0 + enter: ')     
        
input('press enter')


