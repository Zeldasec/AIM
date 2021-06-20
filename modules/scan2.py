import os, sys
from colorama import Fore as color 

import subprocess
import requests
from time import sleep

from requests.api import get
from .nslookup import ip_finder


bold = '\033[1m';end = '\033[0m'

def __start__():
    
    try:
        counter = int(input("[#] How many websites you want to Scan ? (MAX => 5)"))
        if counter > 5 or counter < 0:
            print(color.RED+"[*} Input valid Value. 1 2 3 4 5")
            sleep(0.3);sys.exit()
        else:
            websites_list = []
            print(color.CYAN+bold+"\nhttp://www.example.com or https://www.example.com\n"+end)
            for website in range(counter):
                website_address = input(color.WHITE+"[※] Enter The website Address With Http/Https  #>  ")
                websites_list.append(website_address)
        os.system('clear')
        
        for website in websites_list:
            if 'http://' in website:
                website_url = website[7:]
            elif 'https://' in website:
                website_url = website[8:]

            get_Ip = ip_finder(website_url)

            if 'http://' in website.lower():
                command = ['nikto', '-h', get_Ip]
            elif 'https://' in website.lower():
                command = ['nikto', '-h', get_Ip, '-ssl']
            else:
                print(color.RED+"Please Enter Correct Address With Http‌/Https ! .")
                sleep(0.3);sys.exit()
                    
            for i in range(3):
                sleep(1)
                print(color.CYAN+ "[*]Loading....")
                sleep(2)

            try:
                tool_message = subprocess.run(command,capture_output=True)
                tool_message = tool_message.stdout

                with open('reports/Web_Result_Z.sec.txt', 'a+') as file:
                    file.write(website_url+"\n")
                    file.write(str(tool_message[413:]))
                    file.write('\n');
                    print("Scan Finished, You have the result in 'reports/Web Result z.Sec.txt' .")
                    sleep(3) 

            except Exception:
                print(color.RED+ "Something Went Wrong...")
                sleep(0.3); sys.exit()


    except:
        pass

