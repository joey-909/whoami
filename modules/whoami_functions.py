import socket
import platform
import os

RED = '\033[91m'
GREEN = '\33[92m'
END = '\033[0m'

TRUE = f"{GREEN}[+]{END}"
FALSE = f"{RED}[!]{END}"

try:
    import requests

except:
    print(f"\n{FALSE} Failed To Import Packeges Try To Install It Manually Using The Following Command 'pip install -r requirements.txt'.")
    exit()

def check_updates(version):
    try:
        version_update_source = requests.get("https://raw.githubusercontent.com/whoami-99/whoami/main/whoami_version.txt")
        version_update_source = version_update_source.text

        if version_update_source > version:
            print(f"\n{FALSE} New Update Available {version_update_source}, You Can Type 'whoami' And You Will See Our Github Link To Download The Latest Version.")

        elif version_update_source == version:
            print(f"\n{TRUE} Whoami Is Uptodate.")
            
    except:
        print(f"\n{FALSE} Failed To Check For Updates.")
        exit()

def local_ip():
    try:
        local_ip = socket.gethostbyname(socket.gethostname())
        return local_ip
        
    except Exception as ip_error:
        return(f"\n{FALSE} Failed To Get Your Local Ip {ip_error}.")


def machine_os():
    try:
        machine_os = platform.system()
        return machine_os

    except Exception as os_error:
        return(f"\n{FALSE} Failed To Get The Machine Os {os_error}.")

def clear():
    if machine_os() == "Windows":
        clear = os.system("cls")
        
    else:
        clear = os.system("clear")