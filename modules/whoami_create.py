import os

RED = '\033[91m'
GREEN = '\33[32m'
END = '\033[0m'

try:
    import pathlib
    
except:
    print(f"\n{RED}[!]{END} Failed To Import Packeges Try To Install It Manually Using The Following Command 'pip install -r requirements.txt'.")
    exit()



def show_payloads():
    payloads = pathlib.Path("payloads/").glob("*/*.py")
    
    for file in payloads:
        print(f'\n{GREEN}[+]{END} {file}')
        
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
    print(f"\n{GREEN}[+]{END} Payload Created Succesfully.")