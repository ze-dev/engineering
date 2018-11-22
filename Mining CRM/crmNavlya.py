from mainmod import day
from tkinter import *
z=print
root=Tk()
root.title('Управление объемами. Сегодня %s' % day())
root.geometry('500x200+100+250')


# вставляем текстовое поле ввода text entry
te = Entry(width=20)
def insert():
    te.insert(0, day())
te.grid(row=0,column=0)

te2 = Entry(width=20)
te2.grid(row=0,column=1)

te3 = Entry(width=20)
te3.grid(row=0,column=2)

n_row = int(input('Количество строк? '))
n_col = int(input('Количество столбцов? '))

for _ in range(n_row):
    for __ in range(n_col):
        print(__, _)

b = Button(text="Вставить", command=insert)
b.grid(row=1,column=2)


root.mainloop()

