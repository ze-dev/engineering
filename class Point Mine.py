class Pt:
    def __init__(self, n, x, y, h):
        self.n, self.x, self.y, self.h = n, x, y, h

a=[0,0,0,0] ; a[0]=Pt(1,11,22,33.3)
d={}        ; d[1]=Pt(1,11,22,33.3)

'''
#-------------------Lists
>>> a=[0,0,0,0]
>>> a[0]=Pt(1,11,22,33.3)
>>> a  =>  [<__main__.Pt object at 0x03AB0C70>, 0, 0, 0]
>>> a[0].n  =>  1
>>> a[0].x  =>  11
>>> a[0].y  =>  22
>>> a[0].h  =>  33.3

#---------------Dictionsries
>>> d={}
>>> d[1]=Pt(1,11,22,33.3)
>>> d
{1: <__main__.Pt object at 0x04340FB0>}
>>> d[1].n  =>  1
>>> d[1].x  =>  11
>>> d[1].y  =>  22
>>> d[1].h  =>  33.3

'''
input()