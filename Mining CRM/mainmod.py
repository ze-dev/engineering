'''Используется для управления подсчетом цифр по отдельным карьерам.
Запись ежедневных данных, суммирование, вычисление плановых процентов потерь
и объемов по каждому виду продукции.
'''
def day():
  '''Возвращает сегодняшнюю дату в виде 2018-09-30, вс
Сделать возможность выбрать, показать вместе дату и день или поодиночке.'''
  from datetime import date
  weekdays = { 1: 'пн', 2: 'вт', 3: 'ср', 4: 'чт', 5: 'пт', 6: 'сб', 7: 'вс' }
  d = date.today()                                   # текущая дата
  wd = weekdays[d.isoweekday()]      # текущий день недели
  return d.strftime('{}, {}'.format(d, wd ))      

  
   
 
if __name__=='__main__':
  import time
  print(day())
  print('The module myTime is started manually.\nWindow will be close in several sec.')     
  #time.sleep(2)  
  input('\npress enter..')
                     


  
  
