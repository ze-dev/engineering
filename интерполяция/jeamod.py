import re, sys, math, pyperclip, time

def ReadFileLines(filename):
    with open ('{}'.format(filename), 'r' ) as f:
        fe=f.readlines()
    return fe

def z(*a):
    la=len(a)
    if la==1:
        print(a[0], end='\n')
    if la>1:
        for i in range(la):
            if i < la-1:
                print(a[i], end = ' ')
            if i == la-1:
                print(a[i], end = '\n')

def FloatInput(sms):
    '''We may enter 20.6/2 or 30.5+10.5 and it will be correct'''
    try:
        var=float(eval(input(sms)))  
    except  :
        z('Некорректный ввод. Еще раз : ')
        var = FloatInput(sms)
    return var
