#Import Neeeds

import os, sys
import subprocess

from time import sleep
from colorama import Fore as color 

#import Classes 
from config import menu
from modules import scan1, scan2

bold = '\033[1m';end = '\033[0m'

############################################3

try:
    from colorama import Fore as color
except Exception:
    print("Be Sure libraries in the Requirements.txt file are all installed.")
    sleep(0.1); sys.exit()

############################################3

def make_file_empty():
    with open('reports/Web_Result_Z.sec.txt', 'w') as file :
        file.write(' ')
    


while True:
    os.system('clear')
    menu.banner();menu.main_menu();

    try:
        menu_option = int(input("[⁂] What is your choice ? #> "))
        
        if menu_option == 1:

            os.system('clear')
            menu.banner();menu.tool_menu()
            tool_option = int(input(color.WHITE+"[⁂] What is your choice ? #> "))
            
            if tool_option == 1:
                make_file_empty();scan1.__start__()
                continue
            
            elif tool_option == 2:
                make_file_empty();scan2.__start__()
                continue

            elif tool_option == 3:
                sleep(0.3);continue
            
            else:
                print(color.RED+bold+"Input Valid value...")
                sleep(0.3);sys.exit()

        elif menu_option == 2:
            
            try: 
                with open("reports/about_developers.txt", 'r') as file :
                    os.system('clear')
                    about_information = file.read();
                    print(color.GREEN+str(about_information))
                    input(color.WHITE+bold+"Press any key... "+end)
                    continue
            except:
            
                print(color.WHITE+bold+"\nCould Not Find 'reports/about_developers.txt' file...."+end)
                sleep(3);continue
        
        elif menu_option == 3:
            
            print(bold+"Tnx, For Using Aim."+end)
            sleep(2);os.system('clear');sys.exit()
        
        else:
            pass
                
    except ValueError:
        print(color.red + "Please Enter Valid Input (1 2 3)")
        sleep(0.3);sys.exit()
    



