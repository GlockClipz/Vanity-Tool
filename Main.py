import os
from colorama import init, Fore

init()  # initialize colorama

print(Fore.BLUE + r"""
  ___      ___  __      _____  ___    __  ___________  ___  ___  
 |"  \    /"  |/""\    (\"   \|"  \  |" \("     _   ")|"  \/"  | 
  \   \  //  //    \   |.\\   \    | ||  |)__/  \\__/  \   \  /  
   \\  \/. .//' /\  \  |: \.   \\  | |:  |   \\_ /      \\  \/   
    \.    ////  __'  \ |.  \    \. | |.  |   |.  |      /   /    
     \\   //   /  \\  \|    \    \ | /\  |\  \:  |     /   /     
      \__/(___/    \___)\___|\____\)(__\_|_)  \__|    |___/      
""" + Fore.RESET)  # reset color after printing the text

while True:
    choice = input("""
Choose an option:
1. Close Roblox
2. Close Discord

Type the option number you want to select: """)

    if choice == "1":
        os.system("taskkill /IM RobloxPlayerBeta.exe /F")
        print("Roblox has been closed.")
        break
    elif choice == "2":
        os.system("taskkill /IM discord.exe /F")
        print("Discord has been closed.")
        break
    else:
        print("Invalid choice. Please try again.")
