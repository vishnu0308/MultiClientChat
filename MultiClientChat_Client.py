import socket
import threading
host="127.0.0.1"
port=65532
connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connection.connect((host,port))
user=input("Enter login name:")
connection.send(user.encode("UTF-8"))
def chat():
    while True:
        msg=input()
        connection.send(msg.encode("UTF-8"))
        if msg=="quit":
            print("You have successfully logged out")
            break
def msgFromServer():
    while True:
        servMsg=connection.recv(2040).decode()
        if(servMsg!="qqqqq"):
            print(servMsg)
        else:
            break
t1=threading.Thread(target=msgFromServer)
t2=threading.Thread(target=chat)
t1.start()
t2.start()
t1.join()
t2.join()
connection.close()


        