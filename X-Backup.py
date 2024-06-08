from colorama import init, Fore as cc
import shutil as sh
import ctypes
import time
import sys
import os

init()
dr = DR = r = R = cc.LIGHTRED_EX

clear = os.system('cls')

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        exit(0)


def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def Test():
    while True:
        init()
        dr = DR = r = R = cc.LIGHTRED_EX
        g = G = cc.LIGHTGREEN_EX
        b = B = cc.LIGHTBLUE_EX
        m = M = cc.LIGHTMAGENTA_EX
        c = C = cc.LIGHTCYAN_EX
        y = Y = cc.LIGHTYELLOW_EX
        w = W = cc.RESET

        clear = os.system('cls')

        banner = f'''

{r}▒██   ██▒         ▄▄▄▄    ▄▄▄       ▄████▄   ██ ▄█▀ █    ██  ██▓███  
{r}▒▒ █ █ ▒░        ▓█████▄ ▒████▄    ▒██▀ ▀█   ██▄█▒  ██  ▓██▒▓██░  ██▒
{r}░░  █   ░        ▒██▒ ▄██▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▓██  ▒██░▓██░ ██▓▒
{r} ░ █ █ ▒         ▒██░█▀  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▓▓█  ░██░▒██▄█▓▒ ▒
{r}▒██▒ ▒██▒ ██▓    ░▓█  ▀█▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄▒▒█████▓ ▒██▒ ░  ░
{r}▒▒ ░ ░▓ ░ ▒▓▒    ░▒▓███▀▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
{r}░░   ░▒ ░ ░▒     ▒░▒   ░   ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░░░▒░ ░ ░ ░▒ ░     
{r} ░    ░   ░       ░    ░   ░   ▒   ░        ░ ░░ ░  ░░░ ░ ░ ░░       
{r} ░    ░    ░      ░            ░  ░░ ░      ░  ░      ░              
{r}           ░           ░           ░                                 
{r}Type "help" to see all command                     V1.3
        '''

        option = f''' 
{r}help       see all command 
{r}system     Transfers files from a USB to your computer
{r}usb        Transfers files from your computer to a USB
{r}info       Show infos
{r}Version    Show version
        '''

        clear
        print(f'{banner}')

        Type = input(f">>> ")

        print('\n')

        if Type == 'help':
            print(f'{option}')
            print(f"\n")
            input("Press enter to get back in the main screen")

        if Type == 'Help':
            print(f'{option}')
            print(f"\n")
            input("Press enter to get back in the main screen")

        if Type == 'system':
            syshelp = '''
|-----------------------------------------------------------------------------------------------------------------|
|Option          | Copy the metadata | Copy the permissions | can use buffer | The destination can be a directory |
|1 Copy          |        No         |         Yes          |       No       |                Yes                 |
|2 Copyfile      |        No         |         No           |       No       |                No                  |
|3 Copy2         |        Yes        |         Yes          |       No       |                Yes                 |
|4 Copyfileobj   |        No         |         No           |       Yes      |                No                  |
|-----------------------------------------------------------------------------------------------------------------|
        '''
            print(f"{syshelp}")

            askOP = input("Option: ")

            if askOP == '1':
                    Cartella1 = input(r"USB folder address: ")
                    Destinazione1 = input(r"Computer Folder address: ")
                    sh.copy(Cartella1, Destinazione1)
                    print(f"Backup completed successfully!")
                    time.sleep(1)
                    input("Press enter to get back in the main screen")

            if askOP == '2':
                    Cartella2 = input(r"USB folder address: ")
                    Destinazione2 = input(r"Computer Folder address: ")
                    sh.copyfile(Cartella2, Destinazione2)
                    print(f"Backup completed successfully!")
                    time.sleep(1)
                    input("Press enter to get back in the main screen")

            if askOP == '3':
                    Cartella3 = input(r"USB folder address: ")
                    Destinazione3 = input(r"Computer Folder address: ")
                    sh.copy2(Cartella3, Destinazione2)
                    print(f"Backup completed successfully!")
                    time.sleep(1)
                    input("Press enter to get back in the main screen")

            if askOP == '4':
                    Cartella4 = input(r"USB folder address: ")
                    Destinazione4 = input(r"Computer Folder address: ")
                    sh.copyfileobj(Cartella4, Destinazione4)
                    print(f"Backup completed successfully!")
                    time.sleep(1)
                    input("Press enter to get back in the main screen")

        if Type == 'usb':
            syshelp1 = '''
|-----------------------------------------------------------------------------------------------------------------|
|Option          | Copy the metadata | Copy the permissions | can use buffer | The destination can be a directory |
|1 Copy          |        No         |         Yes          |       No       |                Yes                 |
|2 Copyfile      |        No         |         No           |       No       |                No                  |
|3 Copy2         |        Yes        |         Yes          |       No       |                Yes                 |
|4 Copyfileobj   |        No         |         No           |       Yes      |                No                  |
|-----------------------------------------------------------------------------------------------------------------|
        '''
            print(f"{syshelp1}")

            askOP = input("Option: ")

            if askOP == '1':
                    Cartella1 = input(r"Computer Folder address: ")
                    Destinazione1 = input(r"USB folder address: ")
                    sh.copy(Cartella1, Destinazione1)
                    print(f"Backup completed successfully!")
                    time.sleep(1)
                    input("Press enter to get back in the main screen")

            if askOP == '2':
                    Cartella2 = input(r"Computer Folder address:  ")
                    Destinazione2 = input(r"USB folder address: ")
                    sh.copyfile(Cartella2, Destinazione2)
                    print(f"Backup completed successfully!")
                    time.sleep(1)
                    input("Press enter to get back in the main screen")

            if askOP == '3':
                    Cartella3 = input(r"Computer Folder address: ")
                    Destinazione3 = input(r"USB folder address: ")
                    sh.copy2(Cartella3, Destinazione2)
                    print(f"Backup completed successfully!")
                    time.sleep(1)
                    input("Press enter to get back in the main screen")

            if askOP == '4':
                    Cartella4 = input(r"Computer Folder address: ")
                    Destinazione4 = input(r"USB folder address: ")
                    sh.copyfileobj(Cartella4, Destinazione4)
                    print(f"Backup completed successfully!")
                    time.sleep(1)
                    input("Press enter to get back in the main screen")

        if Type == 'System':
            syshelp = '''
|-----------------------------------------------------------------------------------------------------------------|
|Option          | Copy the metadata | Copy the permissions | can use buffer | The destination can be a directory |
|1 Copy          |        No         |         Yes          |       No       |                Yes                 |
|2 Copyfile      |        No         |         No           |       No       |                No                  |
|3 Copy2         |        Yes        |         Yes          |       No       |                Yes                 |
|4 Copyfileobj   |        No         |         No           |       Yes      |                No                  |
|-----------------------------------------------------------------------------------------------------------------|
        '''
            print(f"{syshelp}")

            askOP = input("Option: ")

            if askOP == '1':
                    Cartella1 = input(r"USB folder address: ")
                    Destinazione1 = input(r"Computer Folder address: ")
                    sh.copy(Cartella1, Destinazione1)
                    print(f"Backup completed successfully!")
                    time.sleep(1)
                    input("Press enter to get back in the main screen")

            if askOP == '2':
                    Cartella2 = input(r"USB folder address: ")
                    Destinazione2 = input(r"Computer Folder address: ")
                    sh.copyfile(Cartella2, Destinazione2)
                    print(f"Backup completed successfully!")
                    time.sleep(1)
                    input("Press enter to get back in the main screen")

            if askOP == '3':
                    Cartella3 = input(r"USB folder address: ")
                    Destinazione3 = input(r"Computer Folder address: ")
                    sh.copy2(Cartella3, Destinazione2)
                    print(f"Backup completed successfully!")
                    time.sleep(1)
                    input("Press enter to get back in the main screen")

            if askOP == '4':
                    Cartella4 = input(r"USB folder address: ")
                    Destinazione4 = input(r"Computer Folder address: ")
                    sh.copyfileobj(Cartella4, Destinazione4)
                    print(f"Backup completed successfully!")
                    time.sleep(1)
                    input("Press enter to get back in the main screen")

        if Type == 'Usb':
            syshelp1 = '''
|-----------------------------------------------------------------------------------------------------------------|
|Option          | Copy the metadata | Copy the permissions | can use buffer | The destination can be a directory |
|1 Copy          |        No         |         Yes          |       No       |                Yes                 |
|2 Copyfile      |        No         |         No           |       No       |                No                  |
|3 Copy2         |        Yes        |         Yes          |       No       |                Yes                 |
|4 Copyfileobj   |        No         |         No           |       Yes      |                No                  |
|-----------------------------------------------------------------------------------------------------------------|
        '''
            print(f"{syshelp1}")

            askOP = input("Option: ")

            if askOP == '1':
                    Cartella1 = input(r"Computer Folder address: ")
                    Destinazione1 = input(r"USB folder address: ")
                    sh.copy(Cartella1, Destinazione1)
                    print(f"Backup completed successfully!")
                    time.sleep(1)
                    input("Press enter to get back in the main screen")

            if askOP == '2':
                    Cartella2 = input(r"Computer Folder address:  ")
                    Destinazione2 = input(r"USB folder address: ")
                    sh.copyfile(Cartella2, Destinazione2)
                    print(f"Backup completed successfully!")
                    time.sleep(1)
                    input("Press enter to get back in the main screen")

            if askOP == '3':
                    Cartella3 = input(r"Computer Folder address: ")
                    Destinazione3 = input(r"USB folder address: ")
                    sh.copy2(Cartella3, Destinazione2)
                    print(f"Backup completed successfully!")
                    time.sleep(1)
                    input("Press enter to get back in the main screen")

            if askOP == '4':
                    Cartella4 = input(r"Computer Folder address: ")
                    Destinazione4 = input(r"USB folder address: ")
                    sh.copyfileobj(Cartella4, Destinazione4)
                    print(f"Backup completed successfully!")
                    time.sleep(1)
                    input("Press enter to get back in the main screen")


        if Type == 'info':
            print(f"|Author: Fedi6431                        |")
            print(f"|----------------------------------------|")
            print(f"|GitHub: Https://www.github.com/fedi6431 |")
            print(f"|----------------------------------------|")
            print(f"\n")
            input("Press enter to get back in the main screen")

        if Type == 'version':
            print(f"|Verion type: Beta        |")
            print(f"|-------------------------|")
            print(f"|Version number: 1.3      |")
            print(f"|-------------------------|")
            print(f"\n")
            input("Press enter to get back in the main screen")

        if Type == 'Info':
            print(f"|Author: Fedi6431                        |")
            print(f"|----------------------------------------|")
            print(f"|GitHub: Https://www.github.com/fedi6431 |")
            print(f"|----------------------------------------|")
            print(f"\n")
            input("Press enter to get back in the main screen")

        if Type == 'Version':
            print(f"|Verion type: Beta        |")
            print(f"|-------------------------|")
            print(f"|Version number: 1.3      |")
            print(f"|-------------------------|")
            print(f"\n")
            input("Press enter to get back in the main screen")

if __name__ == '__main__':
    run_as_admin()
    Test()
