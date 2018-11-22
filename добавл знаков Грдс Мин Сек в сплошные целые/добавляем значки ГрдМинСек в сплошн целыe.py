#программа работает с 7ю десятичными знаками в Плк-42
import time
print('Исходные данные должны быть в input.txt')
print('Координаты д.б. с плавющей запятой через пробел')
input('Для продолжения нажмите  Enter ...')
file = open('input.txt','r').readlines() ; dlin=len(file)     # читаем файл координат в переменную 'file'(т.е. создаем объект файла)
print('Файл input.txt прочитан.\nВ нём %s строк.' % dlin)    # печатаем количество строк в файле:
print('Идет выполнение...')
time.sleep(1)
x,y=[],[] ; gx,gy=[],[] ; mx,my=[],[] ; sx,sy=[],[]
for i in range(dlin):
	x.append(file[i].split( )[0])       ##	;print(x)
	y.append(file[i].split( )[1])       ##	;print(y)
for i in range(dlin):
    gx.append(x[i].split(',')[0]+'°')          # ;      print(gx)
    gy.append(y[i].split(',')[0]+'°')          # ;      print(gy)
    mx.append((x[i].split(',')[1])[0:2]+'\'')           #     ;      print(mx)
    my.append((y[i].split(',')[1])[0:2]+'\'')           #     ;      print(my)
    sx.append((x[i].split(',')[1])[2:4]+'.' + (x[i].split(',')[1])[4:7]+'"')         #       ;      print(sx)
    sy.append((y[i].split(',')[1])[2:4]+'.' + (y[i].split(',')[1])[4:7]+'"')         #       ;      print(sy)
file = open('output.txt','w')
for i in range(dlin):
    open  ('output.txt','a').write(gx[i]+mx[i]+sx[i]) #открываем на допись output.txt и нужная строчка дописывается
    open  ('output.txt','a').write(' '+gy[i]+my[i]+sy[i]+'\n')
print('Результирующий файл output.txt создан:')
time.sleep(1)
with open ('output.txt', 'r') as ff:
        for line in ff:
                print(line[:-1])  
                
input()
        

        
