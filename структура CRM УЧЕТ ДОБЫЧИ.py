dbBl = {                         # цифры ближнего карьера
    '21.08.2018': {           # дата
        'client1': {'sand': {'vol':100,'mas':0} ,
                        'gravel5-20':{ 'vol':0,'mas':200} ,
                        'gravel20-40':{'vol':0,'mas':57},
                        'gravel40-70':{'vol':0,'mas':88},
                        'sps': {'vol':0,'mas':300}},
        'client2': {'sand': {'vol':100,'mas':0} ,
                        'gravel5-20':{ 'vol':0,'mas':200} ,
                        'gravel20-40':{'vol':0,'mas':57},
                        'gravel40-70':{'vol':0,'mas':88},
                        'sps': {'vol':0,'mas':300}}}}
        
db = dbBl
sand_vol=0; sand_mas=0; cn =0
for  k in db:              # перебор дат
    for k_ in db[k]:     # перебор клиентов в одной дате
        if k_ == 'client1':  # ищем название нужного клиента
            day_cl = db[k][k_] # дневной клиент
            if 'sand' in day_cl:
                sand_vol += day_cl['sand']['vol']
                sand_mas+= day_cl['sand']['mas']
            cn += 1   # количество дней, в которые была поставка

print(sand_vol, sand_mas)

#форма записи данных должна быть:
#db[date][client][sand][vol] = 100
# и она должна передаваться из строчки опроса

input()
