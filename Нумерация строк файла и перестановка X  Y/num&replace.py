'''version 16.05.2017. Нумеруем строки файла и меняем  X  и Y при необходимости.'''

def DefSep(string):
    """ Определяем по первой строке, какой разделитель используется -
           запятая или пробел. Если не они,  потом введем вручную"""
    char = []
    try:
        sub1,sub2=string.split(' ') 
    except ValueError:
        char.append(  [ 'не пробел' , 'запятая?', ',' ]  )  
        
    try:
        sub21,sub22=string.split(',') 
    except ValueError:
        char.append(  [ 'не запятая' , 'пробел?' , ' ' ]  )

    if len(char)==1:
        return char
    else:
        return None
 #-----------------------------------------------------------------------
 
print('Данный скрипт для работы только с плановыми координатами. ')
print('Мы можем пронумеровать файл и поменять местами X и Y.')

with open('input.txt','r') as file :
    f=file.readlines()
    
print('Читаем файл " input.txt ". В нем {}  строк.\n    Начальный фрагмент: '.format(len( f ) ) )

if len(f) >= 4:
    for i in range(4):
        print(f[i][:-1:])
else:
    for i in f:
        print(i[:-1:])

char = DefSep(f[0])
print('                        Обработка файла - 4 шага : ')

if char:
    print('1. Разделитель, определённый системой по первой строке - {}'.format(char[0][1] ) )
    beginChar=char[0][2]
else :
    print('1. Разделитель не определен автоматически - это не пробел и не запятая.')
    beginChar=input('   Так что же это ? Введите его с клавиатуры вручную : ')

endChar=input('2. Введите разделитель выходного файла : ')
print('3. Нумерацию строк начинаем по умолчанию с 1.')
nn=input('   Начать с 1 ? Если Да - жмем Enter, если с другого номера - вводим его : ')
if not nn:
    n,nn=1,1
else:
    n=int(nn)
        
re=open('output.txt','w')
rock = input('4. Менять местами X и Y  ? Если Да - жмем Enter, если  Нет - то нет : ')

for i in f:
    '''разбиваем по начальному разделителю, склеиваем по конечному'''
    x,y=list(map(str,i.split( beginChar ) ) )
    if not rock:
        y,x=x,y[:-1:]
    else:
        x,y=x,y[:-1:]
    p=str(n) + endChar + x + endChar + y
    re.write(p+'\n')
    n+=1
    print(p)

re.close()

print('Результат записан в "output.txt". Обработано {}  строк.'.format( n- (int( nn ) ) ) )
input('Все готово! \nНажать  enter для завершения программы ...')


