import socket

def listen(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        s.listen(1)
        print(f"\n[+] Whoami Started Listening On Host {host} And Port {port}, You Can Stop Listening By Pressing CTRL-C.")
        conn, addr = s.accept()
        print(f"\n[+] Whoami New Session Opened {addr}")

    except KeyboardInterrupt:
        print("\n[!] Whoami Listening Stopped.")

    except socket.error:
        print("\n[!] Error While Lisening Try To Check Your Host And Your Port.")

    except:
        print (f"\n[!] Please Check Your Host And Your Port: \n[!] Host : {host}\n[!] Port : {port}")