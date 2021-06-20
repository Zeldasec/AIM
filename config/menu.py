"""
Creator = Legolas-  'instagram.com/zero_dey'

Label = Zelda

Date = Thursday 17 June 2021

Time = 05:12:54 Pm

"""

####################################################################################

from colorama import Fore as color
from time import sleep



#create a function for put a time lag in the printing


#Function for showing the menu To the User

def banner():
    print(color.RED + """     
                        ++                        
                        %%                        
                     .:-%%-:.                     
                  .+%#*=%%=+#%+:                  
                 +%+.   %%   .=#+.                
               .##.     ++     .#%.               
               +%:              .%#               
          .%%%%%%%%%%:      .%%%%%%%%%%:          
               +%:              .%#               
               .%#.     ++     .#%.               
                 +%=.   %%   .=%*.                
                  .=##*=%%=+#%+:                  
                     .:-%%-:.                     
                        %%                        
                        ++
                      
    """, end=' ')
    sleep(0.5)
    print(color.LIGHTGREEN_EX+""" 
                                               
              `-://:-`                          
           .smMMMMMMMMms:                       
          oMMMMMMMMMMMMMMy                      
          MMMMMMMMMMMMMMMM`                     
          oMMMMMMMMMMMMMMy                      
           hd`-+sMMy+:`ym`                      
           /hs/om/-No/od+`                      
            .o+NNyhmMos-                        
              ssmmmdh+-                         
             .m-````-d:                         
              `+dhyds.                          
                /oo+                                                

         █████╗ ██╗███╗   ███╗
        ██╔══██╗██║████╗ ████║
        ███████║██║██╔████╔██║
        ██╔══██║██║██║╚██╔╝██║
        ██║  ██║██║██║ ╚═╝ ██║
        ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝
    """)
    
    sleep(0.3)

def main_menu():
    sleep(0.3)
    print(color.LIGHTYELLOW_EX + "[1] Use Tool")
    print(color.CYAN+"     ***********************")
    sleep(0.3)
    print(color.LIGHTYELLOW_EX + "[2] About Tool")
    print(color.CYAN+"     ***********************")
    sleep(0.3)
    print(color.LIGHTYELLOW_EX + "[3] Exit")
    print(color.CYAN+"     ***********************")
    
def tool_menu():
  
    print(color.LIGHTYELLOW_EX + "[1] Search On a Single Website")
    print(color.CYAN+"     ***********************")
    sleep(0.3)
    print(color.LIGHTYELLOW_EX + "[2] Search On Multiple Websites")
    print(color.CYAN+"     ***********************")
    sleep(0.3)
    print(color.LIGHTYELLOW_EX + "[3] Back To Main Menu \n")
    print(color.CYAN+"     ***********************")
    sleep(0.3)


