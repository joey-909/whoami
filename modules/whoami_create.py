import os
import glob

try:
    from pathlib import Path
except:
    print("\n[!] Failed To Import Packeges Try To Install It Manually Using The Following Command 'pip install -r requirements.txt'.")
    exit()

def show_payloads_windows():
    
    for p in Path( 'payloads/windows' ).iterdir():
        print( p )
    #else:
        #print("\n[!] There Is No Payloads Right Now.")

def show_payloads_mac():
    
    for p in Path( 'payloads/mac' ).iterdir():
        print( p )
    #else:
        #print("\n[!] There Is No Payloads Right Now.")

def show_payloads_linux():
    
    for p in Path( 'payloads/linux' ).iterdir():
        print( p )
    #else:
        #print("\n[!] There Is No Payloads Right Now.")

def check_payload(payload):
    if os.path.isfile(payload):
        return True
    else:
        return False

def create_payload(payload , payload_name, payload_host, payload_port):
    file = open('paylaod.txt', 'w')
    file.write(f"{payload}")
    file.write(f"\n{payload_name}")
    file.write(f"\n{payload_host}")
    file.write(f"\n{payload_port}")
    print("Created")
