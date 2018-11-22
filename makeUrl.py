def makeUrl():
    '''Скрипт должен быть там, куда прописан path,
    или в директории назначения.
    Перед запуском скопировать из браузера адрес.
    Вызывается из TC в нужной папке 
    правой кнопкой 'открыть командную строку',
    далее простой командой makeUrl (этот модуль)'''

    import os

    url  = input('\nВведите УРЛ (вставить ПРАВОЙ кнопкой) >>>')
    name = input('\nВведите название ярлыка >>>')
    # получили путь к папке, откуда запущен скрипт:
    dir_path=os.getcwd() 
    whole_path = '{}\{}.url'.format(dir_path, name)

    with open (whole_path, 'w') as file:
        file.write('[InternetShortcut]\nURL={}'.format(url))      
        
    print('\nЯрлык интернета создан:\n\n'+whole_path)
    input('\nQuest completed! . . ')

if __name__ == '__main__':
    makeUrl()
    
    
