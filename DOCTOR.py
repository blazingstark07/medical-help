import socket
from pynput.keyboard import Key,Controller
import threading
busy=False
keyboard = Controller()
patients=[]
doctor_name = input("Enter doctor name : ")
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('127.0.0.1',101))
sock.send(str.encode(doctor_name))

a = sock.recv(1024)
if busy==True:
    sock.send(str.encode("busy"))
patients.append(a.decode())
sock.send(str.encode("ok"))

rec_sock = socket.socket()
rec_sock.bind(('',102))

def Listen_incoming():
    rec_sock.listen()
    while True:
        s,c = rec_sock.accept()
        receive_and_send(s)
thread=threading.Thread(target=Listen_incoming,args=())
thread.start()

def receive_and_post(sock):
    while(True):
        try:
            a = sock.recv(1024)
            if len(a.decode)==0:
                keyboard.press(Key.enter)
        except:
            break
        print("Message from client : " + a.decode())

def send(sock):
    while(True):
        a = input("\nEnter data to send : ")
        try:
            sock.send(str.encode(a))
        except:
            print ("Connection lost")
            break
def receive_and_send(s):
    thd = threading.Thread(target = receive_and_post, args =(s,))
    thd2 = threading.Thread(target=send,args=(s,))
    thd.start()
    thd2.start()
    


