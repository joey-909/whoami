import os

try:
    import pathlib
except:
    print("\n[!] Failed To Import Packeges Try To Install It Manually Using The Following Command 'pip install -r requirements.txt'.")
    exit()

def show_payloads():
    payloads = pathlib.Path().glob("payloads/*/*.py")
    
    for file in payloads:
        return(f"\n[+] {file}")
    else:
        return("\n[!] There Is No Payloads Right Now.")

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