## Important Note: Don't Change Anything In The Script If You Want To Change In The Script Its On Your Own Responsability
from modules.whoami_functions import check_updates, local_ip, machine_os, clear, payloads_number
from modules.whoami_payloads import show_payloads, check_payload, create_payload
from modules.whoami_listener import whoami_listen

version = "1.2"

RED = '\033[91m'
GREEN = '\33[32m'
YELLOW = '\33[33m'
END = '\033[0m'

def logo():

    clear()

    print("""\n
     __          ___                           _ 
     \ \        / / |                         (_)
      \ \  /\  / /| |__   ___   __ _ _ __ ___  _ 
       \ \/  \/ / | '_ \ / _ \ / _` | '_ ` _ \| |
        \  /\  /  | | | | (_) | (_| | | | | | | |
         \/  \/   |_| |_|\___/ \__,_|_| |_| |_|_|
                                                 Creator: Whoami_99, [!] Beta Version \n""")

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
            command = input("\nWhoami: ").lower()

            if command == "create":
                while True:

                    command = input("\nWhoami>create_payload: ").lower()

                    if command == "show payloads":
                        show_payloads()

                    elif command == "set payload":
                        payload = input(F"\n{YELLOW}[-]{END} Enter Payload Path: ").lower()

                        if check_payload(payload) == True:
                            print(f"\n{GREEN}[+]{END} Payload => {payload}")

                            while True:
                                command = input(f"\nWhoami>{payload}: ").lower()

                                if command == "set name":
                                    print(f"\n{GREEN}[+]{END} Change Your Payload Name.")
                                    command = input(f"\n{YELLOW}[-]{END} Enter Payload Name: ").lower()
                                    
                                    if command == "":
                                        print(f"\n{RED}[!]{END} Please Enter A Valid Payload Name.")

                                    else:
                                        payload_name = command
                                        print(f"\n{GREEN}[+]{END} Payload Name => {payload_name}")

                                elif command == "set host":
                                    print(f"\n{GREEN}[+]{END} Change Your Payload Host (Ex: set host IP Manually).")
                                    command = input(f"\n{YELLOW}[-]{END} Enter Payload Host: ")

                                    if command == "":
                                        print(f"\n{RED}[!]{END} Please Enter A Valid Payload Host")

                                    else:
                                        payload_host = command
                                        print(f"\n{GREEN}[+]{END} Payload Host => {payload_host}")

                                elif command == "set port":
                                    print(f"\n{GREEN}[+]{END} Change Your Payload Port (Ex: set port 4444)")

                                    try:
                                        payload_port = int(input(f"\n{YELLOW}[-]{END} Enter Payload Port: "))
                                        print(f"\n{GREEN}[+]{END} Payload Port => {payload_port}")

                                    except:
                                        print(f"\n{RED}[!]{END} Please Enter A Valid Payload Port.")

                                elif command == "show options":
                                    print(f"\n{GREEN}[+]{END} Payload         : {payload}\n{GREEN}[+]{END} Payload Name    : {payload_name}\n{GREEN}[+]{END} Payload Host    : {payload_host}\n{GREEN}[+]{END} Payload Port    : {payload_port}")
                                
                                elif command == "create":
                                    if payload_name == None:
                                        print(f"\n{RED}[!]{END} Please Add Payload Name.")

                                    elif payload_host == None:
                                        print(f"\n{RED}[!]{END} Please Add Payload Host.")

                                    elif payload_port == None:
                                        print(f"\n{RED}[!]{END} Please Add Payload Port.")
                                    
                                    else:
                                        create_payload(payload, payload_name, payload_host, payload_port)

                                
                                elif command == "help":
                                    print(F"\n{GREEN}[+]{END} set name        : Change Your Payload Name\n{GREEN}[+]{END} set host        : Change Your Payload Host (Ex: set host IP Manually)\n{GREEN}[+]{END} set port        : Change Your Payload Port (Ex: set port 4444)\n{GREEN}[+]{END} show options    : Show Payload Options [Name, Host, Port]\n{GREEN}[+]{END} create          : Build Payload\n{GREEN}[+]{END} clear           : Clear The Screen\n{GREEN}[+]{END} back            : Move back from the current context")
                                
                                elif command == "help":
                                    print(f"\n{GREEN}[+]{END} show payloads   : Show Available Payloads\n{GREEN}[+]{END} set payload     : Use Payload\n{GREEN}[+]{END} clear           : Clear The Screen\n{GREEN}[+]{END} back            : Move back from the current context")

                                elif command == "clear":
                                    logo()

                                elif command == "back":
                                    break

                                else:
                                    print(f"\n{RED}[!]{END} Wrong Command")

                        elif check_payload(payload) == False:
                            print(f"\n{RED}[!]{END} The Value Specified For Payload Is Not Valid Or The Payload Dosen't Exist.")

                    elif command == "clear":
                        logo()

                    elif command == "back":
                        break

                    else:
                        print(f"\n{RED}[!]{END} Wrong Command.")

            elif command == "listen":

                while True:
                    command = input("\nWhoami>listen: ").lower()

                    if command == "set host":
                        print(f"\n{GREEN}[+]{END} Change Your Listening Host (Ex: set host IP Manually) Or Just Type 'l' To Listen On Your Local Network Or Type 'p' To Listen Outside Network.\n")
            
                        listener_host = input(f"{YELLOW}[-]{END} Enter Listening Host: ")
                        if listener_host == "l":
                            listener_host = local_ip()

                        elif listener_host == "p":
                            listener_host = "0.0.0.0"

                        print(f"\n{GREEN}[+]{END} Listening Host => {listener_host}")

                    elif command == "set port":
                        print(f"\n{GREEN}[+]{END} Change Your Listening Port (Ex: set port 4444).")

                        try:
                            listener_port = int(input(f"\n{YELLOW}[-]{END} Enter Port: "))
                            print(f"\n{GREEN}[+]{END} Listen Port => {listener_port}")

                        except:
                            print(f"\n{RED}[!]{END} Please Enter A Valid Listening Port.")

                    elif command == "show options":
                        print(f"\n{GREEN}[+]{END} Listening Host   : {listener_host}\n{GREEN}[+]{END} Listening Port   : {listener_port}")

                    elif command == "listen":
                        if listener_host == None:
                            print(f"\n{RED}[!]{END} Please Add Listening Host.")

                        elif listener_port == None:
                            print(f"\n{RED}[!]{END} Please Add Listening Port.")

                        else:
                            whoami_listen(listener_host, listener_port)
                    
                    elif command == "help":
                        print(f"\n{GREEN}[+]{END} set host		: Change Your Listening Host (Ex: set host IP Manually) Or Just Type 'l' To Listen On Your Local Network Or Type 'p' To Listen Outside Network\n{GREEN}[+]{END} set port		: Change Your Port (Ex: set port 4444)\n{GREEN}[+]{END} show options	: Show Listening Options [Host,Port]\n{GREEN}[+]{END} listen  		: Start Listeneing\n{GREEN}[+]{END} clear		: Clear\n{GREEN}[+]{END} back		: Move back from the current context")
    
                    elif command == "clear":
                        logo()

                    elif command == "back":
                        break

                    else:
                        print(f"\n{RED}[!]{END} Wrong Command.")

            elif command == "help":
                print(F"\n{GREEN}[+]{END} create  : Create A New Payload\n{GREEN}[+]{END} listen  : Start Listening\n{GREEN}[+]{END} whoami  : View Whoami information\n{GREEN}[+]{END} clear   : Clear The Screen\n{GREEN}[+]{END} exit    : Exit Whoami")

            elif command == "whoami":
                check_updates(version)
                print(f"\n{GREEN}[+]{END} Machine Os      : {machine_os()}\n{GREEN}[+]{END} Your Local Ip   : {local_ip()}\n{GREEN}[+]{END} Whoami Version  : {version}\n{GREEN}[+]{END} Payloads        : {payloads_number()}\n{GREEN}[+]{END} Whoami Link     : https://github.com/whoami-99/whoami\n{GREEN}[+]{END} Whoami Author   : whoami_99")

            elif command == "clear":
                logo()

            elif command == "exit":
                print(f"\n{GREEN}[+]{END} Bye, See You Later.")
                break

            else:
                print(f"\n{RED}[!]{END} Wrong Command.")
    
    except KeyboardInterrupt:
        print(f"\n\n{GREEN}[+]{END} Bye, See You Later.")


if __name__ == "__main__":
    main()