import socket
from pynput.keyboard import Key,Controller
import threading
import datetime

keyboard = Controller()
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('127.0.0.1',100))

def send(s):
    while(True):
        b = input("\nEnter data to send : ")
        try:
            s.send(str.encode(b))
        except:
            break

def receive_and_post(s):
    while(True):
        try:
            a=s.recv(1024)
            if len(a.decode)==0:
                keyboard.press(Key.enter)
        except:
            print("Connection Lost")
            break
        print ("\nMessage from server: "+a.decode())

def talk_to_doctor(a):
    talk_to_doctor_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    talk_to_doctor_socket.connect((a[0],102))
    thd = threading.Thread(target = receive_and_post, args =(talk_to_doctor_socket,))
    thd2 = threading.Thread(target=send,args=(talk_to_doctor_socket,))
    thd2.start()
    thd.start()

while True:
    print("1) Get remedies")
    print("2) Get first-aid")
    print("3) Help Desk")
    print("4) Appointment")
    print("5) Exit")
    a = input("\nEnter your choice : ")
    if a=="1":
        prob = input("\nEnter problem : ")
        try:
            sock.send(str.encode("P:"+ prob))
        except:
            print("\nConnection lost\n")
        try:
            a=sock.recv(1024)
            l = eval(a.decode())
            print("\nRemedies are:" )
            for i in l:
                print(i)
            print ()
        except:
            print("\nNo such disease found\n")

    elif a=="2":
        prob = input("\nEnter problem : \n")
        try:
            sock.send(str.encode("Q:"+ prob))
        except:
            print("\nConnection Lost\n")
        try:
            a=sock.recv(1024)
            l = eval(a.decode())
            print("\nFirst aid is:-" )
            for i in l:
                print(i)
            print ()
        except:
            print("\nNo such first aid found\n")

    elif a=="3":
        name = input("\nEnter your name:\n ")
        try:
            sock.send(str.encode("R:"+ name))
        except:
            print("\nConnection Lost\n")
        try:
            a = sock.recv(1024)
            a=eval(a.decode())
            talk_to_doctor(a)
            break
        except e:
            print(str(e))
            print("\nUnable to carry your request\n")
            
    elif a=="4":
        ctime=datetime.datetime.now()
        pname=input("\nEnter your name:")
        phno=input("Enter your phone number: ")
        dname=input("Enter Doctor's name:")
        dtype=input("Enter Doctor's specialization: ")
        hosp=input("Enter hospital name: ")
        bookdate=input("Enter booking date: ")
        booktime=input("Enter booking time: \n")
        Btime=bookdate+" "+booktime
        
        appoint=[ctime,pname,phno,dname,dtype,hosp,Btime]

        try:
            sock.send(str.encode("S:"+str(appoint)))
        except:
            print("\nConnection lost !!\n")

        try:
            a=sock.recv(1024)
            l=a.decode()
            print ("")
            print ()
            if l=="Success":
                print ("\nAppointment is booked: \n")
            else:
                print ("\nBooking failed :-( \n")
        except:
            print ("\nConnection lost!!\n")
        
    elif a=="5":
        print ("\nThank your for using the program!!\n" )
        break
