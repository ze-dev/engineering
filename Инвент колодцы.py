'''v.15.12.18. - использовал рекурсию.
Использовался для вычисления отметок труб и колодцев,
используя промеры по вешке максимальной высотой 2,6
на Смоленском заводе''' 

def manhole_proc(a):
    import pyperclip
    b=float_input('Текущий колодец c отм. %s,  ввод отсчета по вешке > ' % a)
    c=2.6-b+1.39
    print('Глубина точки равна > '.rjust(40), round( c, 2) )
    print('Отметка точки равна > '.rjust(40), round( (a-c), 2) )
    d=str(round( (a-c), 2))
    pyperclip.copy( d )
    print('Скопировано в буфер > '.rjust(40), pyperclip.paste()  )
    validate_answer()

def new_manhole():
    global a_
    a_=float_input('\nНовый колодец, ввод отметки верха >  ')
    manhole_proc(a_)

def validate_answer():
    '''Если далее в этом же колодце - нужен пустой ввод,
    если новый колодец - 0'''
    o =input('\nЕсли след. труба: enter, если новый колодец: 0 + enter > ')
    if o == '':
        manhole_proc(a_)
    if o == '0':
        new_manhole()
    else:
        print('?   Ответ неясен, еще раз >  ')
        validate_answer()

def float_input(messageToUser):
    '''message - str приглашение к вводу данных
    вернет  float или заново запрос к вводу числа.'''
    try:
        an = float(input(messageToUser))
    except ValueError:
        print('\n!   Введенный тип данных неверен, еще раз > ')
        an = float_input(messageToUser)
    return an

try:
    new_manhole()
except:
    print('\n!   Неизвестная ошибка, возможна остановка пользователем.')
            
#input('press enter..')




