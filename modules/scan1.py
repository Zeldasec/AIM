import os, sys
from colorama import Fore as color 
import subprocess

from time import sleep

bold = '\033[1m'; end = '\033[0m'

def __start__():
    target_Ip = input("[※] Enter The Ip Address #>  ")
    target_switch = input("[※] Is The Website Ssl(Https/443) Y/N ? #> ")
    
    if target_switch.lower() == "n":
        command = ["nikto", '-h', target_Ip]
    
    elif target_switch.lower() == "y":
        command = ['nikto', '-h', target_Ip, '-ssl']
    
    else:
        print("Please Enter valid Input")
        sleep(0.3); sys.exit()
    
    os.system('clear')
    
    for i in range(3):
        sleep(1)
        print(color.CYAN+ "[*]Loading....")
        sleep(2)
    
    
    try:
        tool_message = subprocess.run(command,capture_output=True)
        tool_message = tool_message.stdout

        with open('reports/Web_Result_Z.sec.txt', 'w') as file:
            file.write(str(tool_message[413:]))
            print(bold+"Scan Finished, You have the result in 'reports/Web Result z.Sec.txt' ."+end)
            sleep(3)

    except Exception:
        print(color.RED+ "Something Went Wrong...")
        sleep(0.3); sys.exit()

