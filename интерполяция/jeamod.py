import re, sys, math, pyperclip, time

def ReadFileLines(filename):
    '''Вернет список строк прочитанного файла'''
    with open ('{}'.format(filename), 'r' ) as f:
        fe=f.readlines()
    return fe

z = print

def FloatInput(sms):
    '''Делалось специально для CRM по первому карьеру,
    чтобы в поле ввода можно было ввести несколько машин суммированием.
    Также использовал для интерполяции, где нужно предварительное деление,
    или ввод выражения деления сразу в поле ввода.
    We may enter 20.6/2 or 30.5+10.5 and it will be correct
    
    !! Предусмотреть проверку, чтоб не подсунуть в евал вредоносный код'''
    try:
        var=float(eval(input(sms)))  
    except  :
        z('Некорректный ввод. Еще раз : ')
        var = FloatInput(sms)
    return var
