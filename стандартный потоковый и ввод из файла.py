                    # for reading from file

with open ('input.txt','r') as file:
    n=int(file.readline())  # first string of file
    fe=file.readlines()     # other strings of file
    print(n,fe)

#for i in range(n):
#    v,k= list(map(int,fe.readline().split()))
#    print(v,k)
                                     # Func
def Into():
    with open('input.txt','r') as file:
        n=int(file.readline())  # first string of file
        fe=file.readlines()     # other strings of file
    return n,fe
#---------------------------------------------------
                     # for standart inputing
import sys
n = int(sys.stdin.readline())
fe= sys.stdin.readlines()

''' Òàê áóäåò ÷èòàòü ïîñòðî÷íî, è íàäî ñðàçó âñòàâëÿòü êîä îáðàáîòêè'''
n = int(sys.stdin.readline())
for i in range(n):
    fe= sys.stdin.readline()
    # ÊÎÄ îáðàáîòêè ïîñòðî÷íîãî ââîäà

for i in range(n):
    v, k = list(map(int,sys.stdin.readline().split()))
    print(v,k)
                            # Func
def IntoS():
    n = int(sys.stdin.readline())
    for i in range(n):
        v,k = list(map(int,sys.stdin.readline().split()))
        return v,k

#---------------------------------------------------

  

    '''  This is file inside and stdin:
8
1 2
16 3
11 2
20 3
3 5
26 4
7 1
22 4
'''
