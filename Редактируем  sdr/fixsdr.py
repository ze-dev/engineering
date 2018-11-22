from JEAmod import *

file=Read_File('02.sdr')

for line in file:
    match=re.match(patt_NewStation, line)
        
    match=re.match(patt_Hv, line)

    MatchingPattLine(patt_L, line)
    MatchingPattLine(patt_R, line)
        

    
    

    
    
