## Important Note: Don't Change Anything In The Script If You Want To Change In The Script Its On Your Own Responsability
from modules.functions import check_updates, local_ip, machine_os, clear
from modules.connect import connect

version = "1.0"

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

        host = " "
        port = " "

        logo()

        check_updates(version)

        while True:
            command = input("\n@Whoami: ").lower()

            if command == "help":
                print("\n[+] create	: Create A New Payload\n[+] listen	: Start Listening\n[+] info        : View The Whoami information\n[+] clear	: Clear\n[+] close	: Exit")

            elif command == "close":
                print("\n[+] Bye, See You Later.")
                break

            elif command == "clear":
                logo()
        
            elif command == "info":
                check_updates(version)
                print(f"\n[+] Machine Os      : {machine_os()}\n[+] Your Local Ip   : {local_ip()}\n[+] Whoami Version  : {version}\n[+] Whoami Link     : https://github.com/whoami-99/whoami\n[+] Whoami Author   : whoami_99")

            elif command == "create":
                command = input("\n@Whoami>create: ")
                pass

            elif command == "listen":
                while True:

                    command = input("\n@Whoami>listen: ").lower()

                    if command == "help":
                        print("\n[+] set host		: Change Your Host (Ex: set host IP Manually) Or Just Type 'l' To Listen On Your Local Network Or Type 'p' To Listen Outside Network\n[+] set port		: Change Your Port (Ex: set port 4444)\n[+] show options	: Show [Host,Port]\n[+] run			: start The Listener\n[+] clear		: Clear\n[+] close		: Back")

                    elif command == "set host":
                        print("\n[+] Change Your Host (Ex: set host IP Manually) Or Just Type 'l' To Listen On Your Local Network Or Type 'p' To Listen Outside Network\n")
                        host = input("[-] Enter Host: ").lower()

                        if host == "l":
                            host = local_ip()
                        elif host == "p":
                            host = "0.0.0.0"

                        print(f"\n[+] Host => {host}")

                    elif command == "set port":
                        print("\n[+] Change Your Port (Ex: set port 4444)\n")
                        port = input("[-] Enter Port: ").lower()
                        print(f"\n[+] Port => {port}")

                    elif command == "show options":
                        if host == " ":
                            print("\n[!] Please Add Host")
                        elif port == " ":
                            print("\n[!] Please Add Port")

                        else:
                            options = (f"\n[+] Your Host: {host}\n[+] Your Port: {port}")
                            print(options)

                    elif command == 'run':
                        if host == " ":
                            print("\n[!] Please Add Host")
                        elif port == " ":
                            print("\n[!] Please Add Port")

                        else:
                            connect(host, port)
                
                    elif command == "clear":
                        logo()

                    elif command == "close":
                        break
                
                    else:
                        print("\n[!] Wrong Command")

            else:
                print("\n[!] Wrong Command")
    
    except KeyboardInterrupt:
        print("\n\n[+] Bye, See You Later.")


if __name__ == "__main__":
    main()