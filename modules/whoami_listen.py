import socket

RED = '\033[91m'
GREEN = '\33[32m'
END = '\033[0m'

def whoami_listen(listen_host, listen_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((listen_host, listen_port))
        s.listen(1)
        print(f"\n{GREEN}[+]{END} Whoami Started Listening On Host {listen_host} And Port {listen_port}, You Can Stop Listening By Pressing CTRL-C.")
        conn, addr = s.accept()
        print(f"\n{GREEN}[+]{END} Whoami New Session Opened {addr}")

    except KeyboardInterrupt:
        print(f"\n{RED}[!]{END} Whoami Listening Stopped.")

    except socket.error:
        print(f"\n{RED}[!]{END} Failed To Start Listening Try To Close Any Active Listeners Or Check Your Host And Your Port.")

    except:
        print (f"\n{RED}[!]{END} Please Check Your Host And Your Port: \n{RED}[!]{END} Host : {listen_host}\n{RED}[!]{END} Port : {listen_port}")