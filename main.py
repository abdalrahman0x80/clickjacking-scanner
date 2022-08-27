#this is tools for Windows
####################################
#                                  #
#      clickjacking scanner        #
#                                  #
####################################
import os

try:
    from requests import get,post
    #import platform
except:
    print("""
        please install lib requests
        pip3 install requests
    """)
def request():
    banner="""
      ______  __       __    ______  __  ___        __       ___       ______  __  ___  __  .__   __.   _______ 
    /      ||  |     |  |  /      ||  |/  /       |  |     /   \     /      ||  |/  / |  | |  \ |  |  /  _____|
    |  ,----'|  |     |  | |  ,----'|  '  /        |  |    /  ^  \   |  ,----'|  '  /  |  | |   \|  | |  |  __  
    |  |     |  |     |  | |  |     |    <   .--.  |  |   /  /_\  \  |  |     |    <   |  | |  . `  | |  | |_ | 
    |  `----.|  `----.|  | |  `----.|  .  \  |  `--'  |  /  _____  \ |  `----.|  .  \  |  | |  |\   | |  |__| | 
    \______||_______||__|  \______||__|\__\  \______/  /__/     \__\ \______||__|\__\ |__| |__| \__|  \______| 
                                                                                                            
    
    """
    """
    if platform.system() == "Windows":

        os.system("color 2")
        print(banner)
    else:

        print("\033[1;31m"+banner)
    """
    print(banner)
    url = input("[url]:~$ ")
    req= get(url).headers
    try:
        if req["X-Frame-Options"] == "SAMEORIGIN":
            print("the website is secure")
    except:
        print("the website is vulnable")

request()
