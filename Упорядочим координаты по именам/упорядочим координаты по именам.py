﻿'''Использовался при создании каталога координат на вынос под строительство новых веток нефтянки возле Переторгов. 
Координат было 400 шт с различными именами, а надо было , чтобы в каталоге они были не по порядковым именам.'''

qwe=''

file = open('input.txt','r').readlines()        # читаем файл координат в переменную 'file'(т.е. создаем объект файла)

dlin=len(file)                                  # определяем количество строк в файле
                                                # печатаем количество строк в файле: 
print('Найдем нужную координаты по имени.\nНе забудьте очистить output.txt. Файл input.txt прочитан.\nВ нём %s строк.' % dlin)     
    
while qwe=='':
    
    imya = input ('Ищем точку : ')       # Вводим искомое имя точки

    for  i in range (dlin):
        
        for element in file[i].split(' '):               # ищем  совпадение имени  в  каждом элементе строки, указываем нужный символ разбиения строки
            if element == imya :                       # искаться будет строковое совпадение , не числовое.
                print ('Найдено в строке: ',(i+1))   # идем до нужной строки, ища нужное имя координаты
                print (file[i])                         # печатается имя и координаты
                open  ('output.txt','a').write(file[i]) #открываем на допись output.txt и нужная строчка дописывается
                print ('Все записано!!!\n') # ну тут все понятно
   
        if imya == 'готово':                # если поиск точек больше не требуется и из программы надо выйти

            qwe=imya
            
input("Ну хорошо.\nЭкипаж прощается с вами и желает приятного полета.\nПрограмма завершена.Нажмите Enter.")

