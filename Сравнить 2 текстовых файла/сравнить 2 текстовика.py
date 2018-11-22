'''Использовалась для сравнения  координат из таблиц экселя
для Андреевского и следующих 4х  участков.
basein -  файл - эталон с исходным образом данных,
это из него мы вставляли в конечную таблицу департамента.
(01 вставка в департамент ГрдМинСек.txt)
verifyin - проверяемый файл, берем его из готовой
таблицы экселя простым копированием.
'''

import sys, re, time ; z=lambda z:print(z);zz=lambda z,x:print(z,x)
bb=open('basein.txt','r').readlines()
vv=open('verifyin.txt','r').readlines()
b,v=[],[]
for i in bb:
    ii=i.split() ; b.append( [ float(x) for x in ii ] )
for i in vv:
    ii=i.split() ; v.append( [ float(x) for x in ii ] )
if len(b)!=len(v):
    z('Количества строк в файлах не совпадают...Может быть ошибка выполнения.')
    time.sleep(3)
else:
    z('Размеры файлов одинаковы. Идет проверка...')
    time.sleep(3)
sovp,nesovp=0,0 ; massnesovpav=[]
for i in range(len(b)):
    if b[i]==v[i]:
        z('Строки {} совпадают'.format(i+1)) ; sovp+=1
    if b[i]!=v[i]:
        z('Строки {} НЕ совпадают ---- !'.format(i+1)) ; nesovp+=1
        massnesovpav.append(i+1)
z('Проверка выполнена. Совпавших строк {}. Несовпавших {}.'.format(sovp,nesovp))
if massnesovpav!=[]:
    z('Несовпавшие строки {}'.format(massnesovpav))

input('Press Enter To Exit...')


    
