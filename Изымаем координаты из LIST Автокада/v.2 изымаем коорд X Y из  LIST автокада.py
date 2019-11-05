# v.2 11.08.208

import re

print('Исходные данные должны быть в файле " in.txt " . . .')
print('На выходе будут через запятую без перестановки без нумерации')
input('\nДля продолжения нажмите Enter ... ')

file = open('in.txt','r')
f=file.readlines()
file.close()

ready = open('out.txt','w')

print('\nВ исходном файле {}  строк.'.format(len(f)))
print('Фрагмент файла :\n')
for i in range(3):
    print(f[i][:-1:])
input('\nДля продолжения нажмите Enter ... ')

number=0

for i in f:
    p=re.search('X=(.*)Y=(.*)Z=',i)
    ready.write(p.group(1).strip()+','+p.group(2).strip()+'\n') if p else None
    print(p.group(1).strip()+','+p.group(2).strip()) if p else None
    number+=1 if p else 0

print('\nФайл " out.txt " создан. Получено {} строк.'.format(number))
print('\nСкопируйте результат  в исходный .txt файл из автокада')
ready.close()

input('\nCompleted. Press enter to exit...')
