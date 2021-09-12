import socket

def connect(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, int(port)))
        s.listen(1)
        print(f"\n[+] Whoami Started Listening On Host {host} And Port {port}\n")
        conn, addr = s.accept()
        print(f"\n[+] New Session Opened {addr}\n")

    except KeyboardInterrupt:
        print("\n[!] Stopping Listening.\n")

    except socket.error:
        print("\n[!] Error While Lisening Try To Check Your Host And Your Port.\n")

    except:
        print (f"\n[!] Host : {host}\n[!] Port : {port}\n")