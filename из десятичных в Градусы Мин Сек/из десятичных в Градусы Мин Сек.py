#Желательно побольше десятичных знаков в Плк-42. Не менее 7ми.
#Трансформация списком выдает только десятичные градусов
#import pyperclip  устанавливать через инет, поискать для питона 3,6
z=print

def InpDec():
    try:
        nn=int(input('Сколько десятичных знаков нужно в секундах? (от 0 до 3х) : '))
        if nn <0 :
            raise ValueError
    except ValueError:
        print('Неправильно... Еще раз : ')
        nn=InpDec()
    return nn

z('Нумерации в исходном "  input.txt "  не должно быть')
z('ВАЖНО : он должен быть создан обычным блокнотом или Bred3 в кодировке Ansi, иначе проблемы с кодировками!!')
z('Координаты Y и X должны быть через запятую. Если нет, поменять или в файле,  или в скрипте.')
z('Скрипт настроен на исходные из Mapbasic Y,X - в выдаче будет X Y.')
z('Количество десятичных знаков  в исходном файле должно быть 6-10.')

n=InpDec()
v='%.'+str(n)+'f'

# 1.
file = open('input.txt','r').readlines()       # читаем файл координат в переменную 'file'(т.е. создаем объект файла)
z('Идет выполнение...')
x,y=[],[] ; gx,gy=[],[] ; dgx,dgy=[],[] ; dmx,dmy=[],[] ; mx,my=[],[] ; dsx,dsy=[],[] ; sx,sy=[],[]
# 2.
for i in range(len(file)):
    x.append(file[i].split(',')[1])       	
    y.append(file[i].split(',')[0])                # ;z(x);z(y)     #x,y full string
# 3
    gx.append(x[i].split('.')[0])               
    gy.append(y[i].split('.')[0])                # ;z(gx);z(gy)   # строковые целые градусы х,у 
# 4
    dgx.append(float(x[i])-int(gx[i]))       
    dgy.append(float(y[i])-int(gy[i]))     # ;z(dgx);z(dgy)  #float десятичные окончания градусов
# 5
    dmx.append(dgx[i]*60)
    dmy.append(dgy[i]*60)                     #;z(dmx);z(dmy)  #float минуты с десятичн секундами
# 6
    mx.append(str(dmx[i]).split('.')[0])
    my.append(str(dmy[i]).split('.')[0])      #;z(cmx);z(cmy) # строковы целые минуты
# 7
    dsx.append(dmx[i]-int(mx[i]))
    dsy.append(dmy[i]-int(my[i]))             # ;z(dsx);z(dsy)   # дробные значения секунд
# 8
    sx.append(str( v % (dsx[i]*60) ))
    sy.append(str( v % (dsy[i]*60) ))        # ;z(sx);z(sy)  #  строковые значения секунд с дробными окончаниями
# 9
ready = open('output.txt','w')
for i in range(len(file)):
    z(gx[i]+'°'+mx[i]+'\''+sx[i]+'"'+' '+gy[i]+'°'+my[i]+'\''+sy[i]+'"')
    ready.write(gx[i]+'°'+mx[i]+'\''+sx[i]+'"'+' '+gy[i]+'°'+my[i]+'\''+sy[i]+'"\n') #открываем на запись output.txt и строчка дописывается
ready.close()

z('\nФайл " input.txt " прочитан.  Обработано %s строк.' % len(file))    # печатаем количество строк в файле:
z('Файл " output.txt " создан. \n')
input('Для завершения нажмите Enter...')

