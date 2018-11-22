import re, sys,math

def Read_File(filename):
    '''Чтение всего файла построчно'''
    with open ('{}'.format(filename), 'r' ) as f:
        fe=f.readlines()
    return fe

z = print

#  -----------------------------------это для fixsdr--------------------------------
patt_NewStation='02TP' #  объявление новой Ст с координатами и Выс инстр.
patt_Hv='03NM'    # объявление высоты наведения
patt_L='09F1'        # Circle L
patt_R ='09F2'        # Circle R

def DiscoverDimLine(ine):
    ameTS = ine[4:20]
    iket = ine[20:36]
    lin = ine[36:52]
    vu = ine[52:68]
    gu = ine[68:-1]
    return ameTS, iket, lin, vu, gu 
	
def MatchingPattLine(patt, line):
    match=re.match(patt, line)
    if match:
        circle ='L' if patt=='09F1' else 'R'
        nameTS, piket, dlin, va, ga = DiscoverDimLine(line)
        if dlin.strip():
            dhc=(math.cos(math.radians(float(va.strip()))))*float(dlin.strip())
            grp=(math.sin(math.radians(float(va.strip()))))*float(dlin.strip())
        else:
            dhc=0 ; grp=0
        z(int(nameTS), int(piket),  circle, ga.strip(), va.strip(), dlin.strip(), ' гор.прол.= ', round(grp, 3),  ' прев.= ', round(dhc, 3))
	
