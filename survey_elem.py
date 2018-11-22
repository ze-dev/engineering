class Angle:
    '''Вводим угол в виде ГГГ.ММССсс'''
    def __init__(self,a):
        from math import radians as Rad
        deg = int(a)                                              # нашли целое число градусов
        mts = int((a*100 - deg*100))                 # нашли целое число минут
        sec = ((a*100 - deg*100)*100 - mts*100)    # нашли целое число секунд
        self.str = str(deg)+'°'+str(abs(mts))+'\''+str( abs(round(sec,3)))+'"' 
        self.d= a                                                    #  угол в ГГГ.ММССсс через точку
        self.dec = deg+(mts+sec/60)/60          #  угол в ГГГ.Десятичные
        self.r = Rad(self.dec)                               #   угол в радианах
    def hd(self,other):                                        #  выч. горизонтальное проложение         
        from math import sin as sin                   # other - наклонное расстояние
        return round(sin(self.r)*other, 4)
    def vd(self,other):                                        #  выч. вертикальное превышение         
        from math import cos as cos                 #  между центрами
        return round(cos(self.r)*other, 4)
    def __repr__(self):
        return self.str


    

    
