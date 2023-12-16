#Termicom v.1.0.3-2023.29.11R by filcher2011
import os
import sys
import getpass
import webbrowser
import pickledb

from FakesUsers import Fu

version = '1.0.3'
patch = '2023.29.11R'
fn = 'Termicom CMD 1.0.3-2023.29.11R'
fu = Fu()

standart_path = str(os.getcwd())

db = pickledb.load('setting.db', True)

nameuser = getpass.getuser()
os.system(f'title Termicom@{nameuser}')

def Termicom_RU():
    fu.genRegion('ru')
    print('Добро пожаловать в Termicom v.1.0.3')
    print('Введите \'help\' чтобы получить список команд')
    while True:
        com = input(f'{os.getcwd()}: $')
        com = com.lower()

        if com == 'help':
            print('==============================ПОМОЩЬ==============================')
            print('cls - очистить консоль')
            print('calc - калькулятор')
            print('ls - директории')
            print('new - создать новый файл/директорию')
            print('open = открыть файл')
            print('rename - переименовать файл/директорию')
            print('change - изменить файл')
            print('del - удалить файл/директорию')
            print('cd - изменить путь')
            print('ip - информация о ip')
            print('colt - заменить цвет текста')
            print('run - запуск файла в отдельном окне')
            print('prun - запуск Python файла')
            print('ping - пинг сайта')
            print('img - открыть изображение')
            print('generate - генерация случайных данных')
            print('link - открыть ссылку в браузере')
            print('lang - сменить язык')
            print('user - сменить имя терминала')
            print('server - запустить локальный сервер')
        
        elif com == 'lang':
            os.chdir(standart_path)
            os.system('cls')
            lang_input = input('Ru/En: ').lower()
            if lang_input == 'ru':
                db.set('lang', 'ru')
                Termicom_RU()
            elif lang_input == 'en':
                db.set('lang', 'en')
                Termicom_EN()
            else:
                print('Пожалуйста, введите верные данные!')
                lang_input = input('Ru/En: ').lower()
        
        elif com == 'server':
            os.chdir(standart_path)
            os.system("start Server.exe")
        
        elif 'user' in com:
            name_title = com[5: ]
            os.system(f'title Termicom@{name_title}')

        elif com == 'cls':
            os.system('cls')
        elif com == 'calc':
            print('==============================КАЛЬКУЛЯТОР==============================')
            try:
                first = float(input('Введите первое число: '))
                second = float(input('Введите второе число: '))
                action = input('Введите действие(+,-,*,/,//,%): ')
                if action == '+':
                    print(f'Результат: {first+second}')
                elif action == '-':
                    print(f'Результат: {first-second}')
                elif action == '*':
                    print(f'Результат: {first*second}')
                elif action == '/':
                    print(f'Результат: {first/second}')
                elif action == '//':
                    print(f'Результат: {first//second}')
                elif action == '%':
                    print(f'Результат: {first%second}')
                else:
                    print(f'{action}: Неизвестное действие!')
            except ValueError:
                print('Введены неверные данные!')
            
        elif com == 'ls':
            try:
                print('==============================ДИРЕКТОРИИ==============================')
                print(os.listdir())
            except PermissionError:
                print('Отказано в доступе!')
        
        elif com == 'info':
            print('╔════╗╔═══╗╔═══╗╔╗──╔╗╔══╗╔══╗╔══╗╔╗──╔╗')
            print('╚═╗╔═╝║╔══╝║╔═╗║║║──║║╚╗╔╝║╔═╝║╔╗║║║──║║')
            print('──║║──║╚══╗║╚═╝║║╚╗╔╝║─║║─║║──║║║║║╚╗╔╝║')
            print('──║║──║╔══╝║╔╗╔╝║╔╗╔╗║─║║─║║──║║║║║╔╗╔╗║')
            print('──║║──║╚══╗║║║║─║║╚╝║║╔╝╚╗║╚═╗║╚╝║║║╚╝║║')
            print('──╚╝──╚═══╝╚╝╚╝─╚╝──╚╝╚══╝╚══╝╚══╝╚╝──╚╝')
            print('')
            print('Termicom - это аналог командной строки Windwos, предназначенный для программистов. Эта консоль была написана на языке программирования Python программистом Filcher2011.')
            print(f'Имя консоли: {fn}')
            print(f'Версия: {version}')
            print(f'Патч: {patch}')
        
        elif 'cd' in com:
            try:
                path = com[3:]
                os.chdir(path)
                print(f'Текущая дериктория изменилась, {os.getcwd()} \n')
            except FileNotFoundError:
                print('Такая дериктория не найдена!')
            except OSError:
                print('Вы не указали файл!')
        
        elif com == 'new':
            os.system('cls')
            print('==============================НОВЫЙ ФАЙЛ==============================')
            file_type = input('Введите текст(n/d/pyf): ')
            if file_type == 'n':
                file_name = input('Введите название файла: ')
                text_file = open(f"{file_name}.txt", "w")
                print(f'Файл {text_file} был успешно создан!')
            elif file_type == 'd':
                dir_name = input('Введите название папки: ')
                os.mkdir(dir_name)
                print(f'Папка {dir_name} был успешно создан!')
            elif file_type == 'pyf':
                filepy_name = input('Введите название python файла: ')
                py_file = open(f"{filepy_name}.py", "w")
                print(f'Python файл {py_file} был успешно создан!')
            else:
                print('Введена неверная данная!')
        
        elif 'rename' in com:
            print('==============================ПЕРЕИМЕНОВАНИЕ ФАЙЛА/ДИРЕКТОРИИ==============================')
            try:
                file_ren = com[7: ]
                newfile_name = input('Введите новое имя файла: ')
                os.rename(file_ren, newfile_name)
                print(f'Файл {file_ren} был изменен на {newfile_name}!')
            except FileNotFoundError:
                print('Такой файл для измены не найден!')

        elif 'open' in com:
            try:
                file_open = com[5: ]
                f = open(file_open, 'r')
                print(f.read())
            except FileNotFoundError:
                print('Такой файл для открытия не найден!')
        
        elif 'img' in com:
            try:
                img_open = com[4: ]
                os.startfile(f'{img_open}')
            except FileNotFoundError:
                print('Такого изображения для открытия не найден!')
        
        elif 'change' in com:
            try:
                file_change = com[7: ]
                f = open(file_change, 'w')
                text = input('Введите текст: ')
                f.write(str(text))
                print('Текст успешно заменен!')
                f.close()
                if f.closed == False:
                    f.close()

            except FileNotFoundError:
                print('Такой файл для открытия не найден!')
            except PermissionError:
                print("Нельзя изменить текстовые данные для папки!")
        
        elif 'cmd' in com:
            command_cmd = com[4: ]
            print(os.system(command_cmd))
        
        elif 'del' in com:
            os.system('cls')
            print('==============================УДАЛЕНИЕ ФАЙЛА/ДИРЕКТОРИИ==============================')
            file_type = input('Введите тип(n/d/pyf): ')
            if file_type == 'n':
                try:
                    file_namedel = input('Введите название файла: ')
                    ok = input('Вы уверены что хотите удалить файл? Его вернуть будет нельзя!(y/n): ')
                    if ok == 'y':
                        os.remove(file_namedel)
                        print('Файл был удален!')
                except PermissionError:
                    print('Файл занят другим процессом!')
                except FileNotFoundError:
                    print('Такого файла для удаления нет!')

            elif file_type == 'd':
                try:
                    dir_namedel = input('Введите название директории: ')
                    ok = input('Вы уверены что хотите удалить файл? Его вернуть будет нельзя!(y/n): ')
                    if ok == 'y':
                        print('Директория была удалена!')
                        os.rmdir(dir_namedel)
                except OSError:
                    print('Эта папка не пуста!')

            elif file_type == 'pyi':
                try:
                    filepy_name = input('Введите название python файла: ')
                    ok = input('Вы уверены что хотите удалить файл? Его вернуть будет нельзя!(y/n): ')
                    if ok == 'y':
                        os.remove(filepy_name)
                        print('Python файл был удален!')
                except PermissionError:
                    print('Файл занят другим процессом!')
                except FileNotFoundError:
                    print('Такого файла для удаления нет!')
        
        elif com == 'infopc':
            print(f'Имя пользователя: {nameuser}')
            print('\n\n')
            print(os.system('systeminfo'))

        elif 'colt' in com:
            color = com[5: ]
            if color == 'red':
                os.system('color 4')
            elif color == 'blue':
                os.system('color 1')
            elif color == 'green':
                os.system('color a')
        
        elif 'prun' in com:
            try:
                filepy_run = com[5: ]
                print(os.system(f'python {filepy_run}'))
            except FileNotFoundError:
                print('Такого файла для открытия нету!')
        
        elif 'run' in com:
            try:
                file_run = com[4: ]
                os.system(f'start {file_run}')
            except FileNotFoundError:
                print('Такого файла для открытия нету!')
        
        elif 'link' in com:
            link = com[4: ]
            webbrowser.open(link, new=2)
        
        elif com == 'generate':
            print(f'Имя: {fu.fake_name("male")}')
            print(f'Адрес проживания: {fu.fake_addres(True)}')
            print(f'Номер телефона: {fu.fake_number()}')
        
        elif 'ping' in com:
            site_ping = com[5: ]
            print(os.system(f'ping {site_ping}'))

        elif com == 'ip':
            print(os.system('ipconfig'))

        elif com == '<':
            os.chdir("..")
        
        elif com == 'exit':
            sys.exit()
        
        else:
            print(f'{com}: Неизвестная команда!')

def Termicom_EN():
    fu.genRegion('en')
    print('Welcome to Termicom 1.0.3')
    print('Enter \'help\' to get help-list')
    while True:
        com = input(f'{os.getcwd()}: $')
        com = com.lower()

        if com == 'help':
            print('==============================HELP==============================')
            print('cls - clean console')
            print('calc - calculator')
            print('ls - directory')
            print('new - create new file/directory')
            print('open = open file')
            print('rename - rename file/directory')
            print('change - change file\'s value')
            print('del - delete file/directory')
            print('cd - change path')
            print('ip - info on ip-address')
            print('colt - change color text')
            print('run - start file in new window')
            print('prun - start Python script')
            print('ping - ping site')
            print('img - open image')
            print('generate - generation raandom information')
            print('link - open  link in browser')
            print('lang - change language')
            print('user - change name terminal')
            print('server - start local server')

        elif com == 'lang':
            os.chdir(standart_path)
            os.system('cls')
            lang_input = input('Ru/En: ').lower()
            if lang_input == 'ru':
                db.set('lang', 'ru')
                Termicom_RU()
            elif lang_input == 'en':
                db.set('lang', 'en')
                Termicom_EN()
            else:
                print('Пожалуйста, введите верные данные!')
                lang_input = input('Ru/En: ').lower()
        
        elif com == 'server':
            os.chdir(standart_path)
            os.system("start Server.exe")
        
        elif 'user' in com:
            name_title = com[5: ]
            os.system(f'title Termicom@{name_title}')

        elif com == 'cls':
            os.system('cls')
        elif com == 'calc':
            print('==============================CALCULATOR==============================')
            try:
                first = float(input('Enter first number: '))
                second = float(input('Enter second number: '))
                action = input('Enter action(+,-,*,/,//,%): ')
                if action == '+':
                    print(f'Result: {first+second}')
                elif action == '-':
                    print(f'Result: {first-second}')
                elif action == '*':
                    print(f'Result: {first*second}')
                elif action == '/':
                    print(f'Result: {first/second}')
                elif action == '//':
                    print(f'Result: {first//second}')
                elif action == '%':
                    print(f'Result: {first%second}')
                else:
                    print(f'{action}: Unknow action!')
            except ValueError:
                print('Enter not true value!')
            
        elif com == 'ls':
            try:
                print('==============================DIRECTORY==============================')
                print(os.listdir())
            except PermissionError:
                print('Access denied')
        
        elif 'cd' in com:
            try:
                path = com[3:]
                os.chdir(path)
                print(f'The current directory has changed, {os.getcwd()} \n')
            except FileNotFoundError:
                print('This directory was not found!')
            except OSError:
                print('You didn\'t specify the file!')
        
        elif com == 'info':
            print('╔════╗╔═══╗╔═══╗╔╗──╔╗╔══╗╔══╗╔══╗╔╗──╔╗')
            print('╚═╗╔═╝║╔══╝║╔═╗║║║──║║╚╗╔╝║╔═╝║╔╗║║║──║║')
            print('──║║──║╚══╗║╚═╝║║╚╗╔╝║─║║─║║──║║║║║╚╗╔╝║')
            print('──║║──║╔══╝║╔╗╔╝║╔╗╔╗║─║║─║║──║║║║║╔╗╔╗║')
            print('──║║──║╚══╗║║║║─║║╚╝║║╔╝╚╗║╚═╗║╚╝║║║╚╝║║')
            print('──╚╝──╚═══╝╚╝╚╝─╚╝──╚╝╚══╝╚══╝╚══╝╚╝──╚╝')
            print('')
            print('Termicom - This is an analogue of the Viknovs command line, which is intended for programmers. This console was written in the Python programming language by programmer filcher2011')
            print(f'Name: {fn}')
            print(f'Version: {version}')
            print(f'Patch: {patch}')
        
        elif com == 'new':
            os.system('cls')
            print('==============================NEW FILE/DIRECTORY==============================')
            file_type = input('Enter type(n/d/pyf): ')
            if file_type == 'n':
                file_name = input('Enter name for file: ')
                text_file = open(f"{file_name}.txt", "w")
                print(f'File {text_file} was successfully created!')
            elif file_type == 'd':
                dir_name = input('Enter name for directory: ')
                os.mkdir(dir_name)
                print(f'Directory {dir_name} was successfully created!')
            elif file_type == 'pyf':
                filepy_name = input('Enter name for python file: ')
                py_file = open(f"{filepy_name}.py", "w")
                print(f'Python file {py_file} was successfully created!')
            else:
                print('Invalid data entered!')
        
        elif 'rename' in com:
            print('==============================RENAME FILE/DIRECTORY==============================')
            try:
                file_ren = com[7: ]
                newfile_name = input('Enter new filename: ')
                os.rename(file_ren, newfile_name)
                print(f'File {file_ren} was changed to {newfile_name}!')
            except FileNotFoundError:
                print('No such file for treason was found!')

        elif 'open' in com:
            try:
                file_open = com[5: ]
                f = open(file_open, 'r')
                print(f.read())
            except FileNotFoundError:
                print('No such file was found to open!')
        
        elif 'img' in com:
            try:
                img_open = com[4: ]
                os.startfile(f'{img_open}')
            except FileNotFoundError:
                print('No such image was found to open!')

        elif 'change' in com:
            try:
                file_change = com[7: ]
                f = open(file_change, 'w')
                text = input('Enter text: ')
                f.write(str(text))
                print('The text has been successfully replaced!')
                f.close()
                if f.closed == False:
                    f.close()

            except FileNotFoundError:
                print('No such file was found to open!')
            except PermissionError:
                print("Нельзя изменить текстовые данные для папки!")
            
        elif 'cmd' in com:
            command_cmd = com[4: ]
            print(os.system(command_cmd))
        
        elif 'del' in com:
            os.system('cls')
            print('==============================DELETE FILE/DIRECTORY==============================')
            file_type = input('Enter type(n/d/pyi): ')
            if file_type == 'n':
                try:
                    file_namedel = input('Enter name for file: ')
                    ok = input('Are you sure you want to delete the file? It will not be possible to return it!(y/n): ')
                    if ok == 'y':
                        os.remove(file_namedel)
                        print('The file has been deleted!')
                except PermissionError:
                    print('The file is in use by another process!')
                except FileNotFoundError:
                    print('No such file was found to open!')

            elif file_type == 'd':
                try:
                    dir_namedel = input('Enter file for directory: ')
                    ok = input('Are you sure you want to delete the directory? It will not be possible to return it!(y/n): ')
                    if ok == 'y':
                        print('The directory has been deleted!')
                        os.rmdir(dir_namedel)
                except OSError:
                    print('This folder is not empty!')

            elif file_type == 'pyi':
                try:
                    filepy_name = input('Enter name for python script: ')
                    ok = input('Are you sure you want to delete the python file? It will not be possible to return it!(y/n): ')
                    if ok == 'y':
                        os.remove(filepy_name)
                        print('The python file has been deleted!')
                except PermissionError:
                    print('The file is in use by another process!')
                except FileNotFoundError:
                    print('No such file was found to open!')
        
        elif com == 'infopc':
            print(f'Nameuser: {nameuser}')
            print('\n\n')
            print(os.system('systeminfo'))

        elif 'colt' in com:
            color = com[5: ]
            if color == 'red':
                os.system('color 4')
            elif color == 'blue':
                os.system('color 1')
            elif color == 'green':
                os.system('color a')
        
        elif 'prun' in com:
            try:
                filepy_run = com[5: ]
                print(os.system(f'python {filepy_run}'))
            except FileNotFoundError:
                print('There is no such file to open!')
        
        elif 'run' in com:
            try:
                file_run = com[4: ]
                os.system(f'start {file_run}')
            except FileNotFoundError:
                print('There is no such file to open!')
        
        elif 'link' in com:
            link = com[4: ]
            webbrowser.open(link, new=2)
        
        elif com == 'generate':
            print(f'Name: {fu.fake_name("male")}')
            print(f'Address: {fu.fake_addres(True)}')
            print(f'Phone number: {fu.fake_number()}')
        
        elif 'ping' in com:
            site_ping = com[5: ]
            print(os.system(f'ping {site_ping}'))

        elif com == 'ip':
            print(os.system('ipconfig'))

        elif com == '<':
            os.chdir("..")
        
        elif com == 'exit':
            sys.exit()
        
        else:
            print(f'{com}: Unknow command!')

if __name__ == '__main__':
    if db.get('lang') == 'ru':
        Termicom_RU()
    elif db.get('lang') == 'en':
        Termicom_EN()
    else:
        lang = input('Ru/En: ').lower()
        if lang == 'ru':
            db.set('lang', 'ru')
            Termicom_RU()
        elif lang == 'en':
            db.set('lang', 'en')
            Termicom_EN()
        else:
            print('Please, enter true value!')
            lang = input('Ru/En: ').lower()