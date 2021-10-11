## Important Note: Don't Change Anything In The Script If You Want To Change In The Script Its On Your Own Responsability
from modules.whoami_functions import check_updates, local_ip, machine_os, clear
from modules.whoami_payloads import show_payloads, check_payload, create_payload, payloads_number
from modules.whoami_listener import whoami_listen

version = "1.0"

RED = '\033[91m'
GREEN = '\33[92m'
YELLOW = '\33[93m'
END = '\033[0m'

TRUE = f"{GREEN}[+]{END}"
FALSE = f"{RED}[!]{END}"

def logo():
    clear()

    print(f"""\n{RED}
 __      __ .__                              .__
/  \    /  \|  |__    ____  _____     _____  |__|{END}
\   \/\/   /|  |  \  /  _ \ \__  \   /     \ |  |
 \        / |   Y  \(  <_> ) / __ \_|  Y Y  \|  |
  \__/\  /  |___|  / \____/ (____  /|__|_|  /|__|
       {RED}\/{END}        {RED}\/{END}              {RED}\/{END}       {RED}\/{END}    
                                                \n""")

def main():
    try:

        listener_host = None
        listener_port = None

        payload_name = None
        payload_host = None
        payload_port = None
        
        logo()
        check_updates(version)

        while True:
            command = input(f"\nWhoami: ").lower()
            if len(command) > 0:

                if command == "create":
                    while True:

                        command = input(f"\nWhoami>{GREEN}create_payload{END}: ").lower()
                        if len(command) > 0:

                            if command == "show payloads":
                                show_payloads()

                            elif command == "set payload":
                                command = input(F"\n{YELLOW}[-]{END} Enter Payload Path: ").lower()

                                if check_payload(command) == True:
                                    payload = command
                                    
                                    print(f"\n{TRUE} Payload => {payload}")

                                    while True:
                                        command = input(f"\nWhoami>{GREEN}{payload}{END}: ").lower()
                                        if len(command) > 0:


                                            if command == "set name":
                                                print(f"\n{TRUE} Change Your Payload Name.")
                                                command = input(f"\n{YELLOW}[-]{END} Enter Payload Name: ").lower()
                                                
                                                if command == "":
                                                    print(f"\n{FALSE} Please Enter A Valid Payload Name.")

                                                else:
                                                    payload_name = command
                                                    print(f"\n{TRUE} Payload Name => {payload_name}")

                                            elif command == "set host":
                                                print(f"\n{TRUE} Change Your Payload Host (Ex: {local_ip()}).")
                                                command = input(f"\n{YELLOW}[-]{END} Enter Payload Host: ")

                                                if command == "":
                                                    print(f"\n{FALSE} Please Enter A Valid Payload Host.")

                                                else:
                                                    payload_host = command
                                                    print(f"\n{TRUE} Payload Host => {payload_host}")

                                            elif command == "set port":
                                                print(f"\n{TRUE} Change Your Payload Port (Ex: 4444)")

                                                try:
                                                    payload_port = int(input(f"\n{YELLOW}[-]{END} Enter Payload Port: "))
                                                    print(f"\n{TRUE} Payload Port => {payload_port}")

                                                except:
                                                    print(f"\n{FALSE} Please Enter A Valid Payload Port.")

                                            elif command == "show options":
                                                print(f"\n{TRUE} Payload         : {payload}")

                                                if payload_name == None:
                                                    print(f"{FALSE} Payload Name    : {payload_name}")

                                                else:
                                                    print(f"{TRUE} Payload Name    : {payload_name}")

                                                if payload_host == None:
                                                    print(f"{FALSE} Payload Host    : {payload_host}")

                                                else:
                                                    print(f"{TRUE} Payload Host    : {payload_host}")
                                                
                                                if payload_port == None:
                                                    print(f"{FALSE} Payload Port    : {payload_port}")

                                                else:
                                                    print(f"{TRUE} Payload Port    : {payload_port}")
                                            
                                            elif command == "create":
                                                if payload_name == None:
                                                    print(f"\n{FALSE} Please Add Payload Name.")

                                                elif payload_host == None:
                                                    print(f"\n{FALSE} Please Add Payload Host.")

                                                elif payload_port == None:
                                                    print(f"\n{FALSE} Please Add Payload Port.")
                                                
                                                else:
                                                    create_payload(payload, payload_name, payload_host, payload_port)

                                            elif command == "help":
                                                print(F"\n{TRUE} set name        : Change Your Payload Name\n{TRUE} set host        : Change Your Payload Host (Ex: set host)\n{TRUE} set port        : Change Your Payload Port (Ex: set port)\n{TRUE} show options    : Show Payload Options [Name, Host, Port]\n{TRUE} create          : Build Whoami Payload\n{TRUE} clear           : Clear The Screen\n{TRUE} back            : Move back from the current context")

                                            elif command == "clear":
                                                logo()

                                            elif command == "back":
                                                break

                                            else:
                                                print(f"\n{FALSE} Wrong Command.")
                                        
                                        else:
                                            pass

                                elif check_payload(command) == False:
                                    print(f"\n{FALSE} The Value Specified For Payload Is Not Valid Or The Payload Dosen't Exist.")

                            elif command == "help":
                                            print(f"\n{TRUE} show payloads   : Show Available Whoami Payloads\n{TRUE} set payload     : Set The Payload You Want To Use\n{TRUE} clear           : Clear The Screen\n{TRUE} back            : Move back from the current context")

                            elif command == "clear":
                                logo()

                            elif command == "back":
                                break

                            else:
                                print(f"\n{FALSE} Wrong Command.")
                        
                        else:
                            pass

                elif command == "listen":

                    while True:
                        command = input(f"\nWhoami>{GREEN}listen{END}: ").lower()
                        if len(command) > 0:

                            if command == "set host":
                                print(f"\n{TRUE} Change Your Listening Host (Ex: {local_ip()}) Or Just Type 'l' To Listen On Your Local Network Or Type 'p' To Listen Outside Network.\n")
                    
                                listener_host = input(f"{YELLOW}[-]{END} Enter Listening Host: ")
                                if listener_host == "l":
                                    listener_host = local_ip()

                                elif listener_host == "p":
                                    listener_host = "0.0.0.0"

                                print(f"\n{TRUE} Listening Host => {listener_host}")

                            elif command == "set port":
                                print(f"\n{TRUE} Change Your Listening Port (Ex: 4444).")

                                try:
                                    listener_port = int(input(f"\n{YELLOW}[-]{END} Enter Port: "))
                                    print(f"\n{TRUE} Listen Port => {listener_port}")

                                except:
                                    print(f"\n{FALSE} Please Enter A Valid Listening Port.")

                            elif command == "show options":
                                if listener_host == None:
                                    print(f"\n{FALSE} Listening Host  : {listener_host}")

                                else:
                                    print(f"\n{TRUE} Listening Host  : {listener_host}")

                                if listener_port == None:
                                    print(f"{FALSE} Listening Port  : {listener_port}")

                                else:
                                    print(f"{TRUE} Listening Port  : {listener_port}")

                            elif command == "listen":
                                if listener_host == None:
                                    print(f"\n{FALSE} Please Add Listening Host.")

                                elif listener_port == None:
                                    print(f"\n{FALSE} Please Add Listening Port.")

                                else:
                                    whoami_listen(listener_host, listener_port)
                            
                            elif command == "help":
                                print(f"\n{TRUE} set host		: Change Your Listening Host (Ex: set host) Or Just Type 'l' To Listen On Your Local Network Or Type 'p' To Listen Outside Network\n{TRUE} set port		: Change Your Port (Ex: set port)\n{TRUE} show options	: Show Listening Options [Host,Port]\n{TRUE} listen  		: Start Listeneing\n{TRUE} clear		: Clear\n{TRUE} back		: Move back from the current context")
            
                            elif command == "clear":
                                logo()

                            elif command == "back":
                                break

                            else:
                                print(f"\n{FALSE} Wrong Command.")
                        
                        else:
                            pass
                
                elif command == "tools":
                    print(f"\n{TRUE} Coming Soon :)")

                elif command == "whoami":
                    check_updates(version)
                    print(f"\n{TRUE} Machine Os      : {machine_os()}\n{TRUE} Your Local Ip   : {local_ip()}\n{TRUE} Whoami Version  : {version}\n{TRUE} Payloads        : {payloads_number()}\n{TRUE} Whoami Link     : https://github.com/whoami-99/whoami\n{TRUE} Whoami Authors  : whoami_99 & jason")

                elif command == "help":
                    print(F"\n{TRUE} create  : Create A New Payload\n{TRUE} listen  : Start Listening\n{TRUE} tools   : A Built In Whoami Tools That Will Help You\n{TRUE} whoami  : View Whoami information\n{TRUE} clear   : Clear The Screen\n{TRUE} exit    : Exit Whoami")

                elif command == "clear":
                    logo()

                elif command == "exit":
                    print(f"\n{TRUE} Bye, See You Later.")
                    break

                else:
                    print(f"\n{FALSE} Wrong Command.")
            
            else:
                pass
    
    except KeyboardInterrupt:
            print(f"\n\n{TRUE} Bye, See You Later.")

if __name__ == "__main__":
    main()
