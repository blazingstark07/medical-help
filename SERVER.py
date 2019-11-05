import pickle
import os
import socket
import threading
import datetime
#Remedy class to store Problem and Remedy

DOCTOR = []

class Remedy:
    #problem_and_remedy = dict()
    def __init__(self):
        self.problem_and_remedy = dict()
    
    def add_Problem_and_remedy(self,Problem,Remedy=[]):
        self.problem_and_remedy.update({Problem:Remedy})

    def get_Remedy(self,Problem):
        if(Problem not in self.problem_and_remedy):
            return("Problem not found")
            
        return self.problem_and_remedy[Problem]

    def add_Remedy_to_Problem(self,Problem,Remedy):
        if(Problem not in self.problem_and_remedy):
            return("Problem not found")
            
        self.problem_and_remedy[Problem].append(Remedy)
        
    def edit_Remedy(self,Problem):
        if(Problem not in self.problem_and_remedy):
            return("Problem not found")
            
        print("Remedies for Problem available :")
        for i in range(len(self.problem_and_remedy[Problem])):
            print(i+1,")",self.problem_and_remedy[Problem][i])
        
        a = " "
        while(not a.isdigit()):
            a = input("Enter remedy no. to edit")
        new_remedy = input("Enter new remedy: ")
        self.problem_and_remedy[Problem][int(a)-1]=new_remedy
        
    def delete_Remedy(self,Problem):
        if(Problem not in self.problem_and_remedy):
            return ("Problem not found")
            
        print("Remedies for Problem available :")
        for i in range(len(self.problem_and_remedy[Problem])):
            print(i+1,")",self.problem_and_remedy[Problem][i])
        print("\n\n0) ALL")
        
        a = " "
        while(not a.isdigit()):
            a = input("Enter remedy no. to delete")
        
        if(int(a)>=1 and int(a)<=len(self.problem_and_remedy[Problem])):
            del self.problem_and_remedy[Problem][int(a)-1]
        elif(int(a)==0):
            del [self.problem_and_remedy[Problem]]
        else:
            print("INVALID INDEX !!!")

class FirstAid:
    def __init__(self):
        self.problem_and_faid = dict()
        
    def add_Problem_and_faid(self,Problem,Faid=[]):
        self.problem_and_faid.update({Problem:Faid})

    def get_Faid(self,Problem):
        if(Problem not in self.problem_and_faid):
            return("Problem not found")
        return self.problem_and_faid[Problem]

    def add_Faid_to_Problem(self,Problem,Faid):
        if(Problem not in self.problem_and_faid):
            return("Problem not found")
            
        self.problem_and_faid[Problem].append(Faid)
        
    def edit_Faid(self,Problem):
        if(Problem not in self.problem_and_faid):
            return("Problem not found")
            
        print("Remedies for Problem available :")
        for i in range(len(self.problem_and_faid[Problem])):
            print(i+1,")",self.problem_and_faid[Problem][i])
        
        a = " "
        while(not a.isdigit()):
            a = input("Enter faid no. to edit")
        new_faid = input("Enter new faid: ")
        self.problem_and_faid[Problem][int(a)-1]=new_faid
        
    def delete_Faid(self,Problem):
        if(Problem not in self.problem_and_faid):
            return ("Problem not found")
            
        print("Remedies for Problem available :")
        for i in range(len(self.problem_and_faid[Problem])):
            print(i+1,")",self.problem_and_faid[Problem][i])
        print("\n\n0) ALL")
        
        a = " "
        while(not a.isdigit()):
            a = input("Enter faid no. to delete")
        
        if(int(a)>=1 and int(a)<=len(self.problem_and_faid[Problem])):
            del self.problem_and_faid[Problem][int(a)-1]
        elif(int(a)==0):
            self.problem_and_faid[Problem]=[]
        else:
            print("INVALID INDEX !!!")

class DoctorItem:
    def __init__(self,dname,q,hn,ht,sp):
        self.dname = dname
        self.q = q
        self.hn = hn
        self.ht = ht
        self.sp = sp
        
    def modify_Qualification(self,q):
        self.q = q
    def modify_HName(self,hn):
        self.hn = hn
    def modify_HType(self,ht):
        self.ht=ht
    
    def get_detail(self):
        return (self.dname,self.q,self.hn,self.ht,self.sp)
    
class Doctor:
    def __init__(self):
        self.doctor=[]
    def add_doctor(self):
        a=input("Enter doctor's name: ")
        b=input("Enter qualification: ")
        c=input("Enter hospital name: ")
        d=input("Enter hospital type: ")
        e=input("Enter specialization: ")
        f=DoctorItem(a,b,c,d,e)
        self.doctor.append(f)
        
class AppointItem:
        def __init__(self,a):
            self.currenttime=a[0]
            self.name=a[1]
            self.pno=a[2]
            self.dname=a[3]
            self.dtype=a[4]
            self.hname=a[5]
            self.booktime=a[6]
    
class Appointment:

    def __init__(self):
        self.appointment=[]

    def Add(self,lis):
        z=AppointItem(lis)
        self.appointment.append(z)

        
if not os.path.exists("remedy.dat"):
    fin = open("remedy.dat","xb")
    r = Remedy()
    pickle.dump(r,fin)
    fin.close()

if not os.path.exists("aid.dat"):
    fin = open("aid.dat","xb")
    r = FirstAid()
    pickle.dump(r,fin)
    fin.close()

if not os.path.exists("doctor.dat"):
    fin = open("doctor.dat","xb")
    r = Doctor()
    pickle.dump(r,fin)
    fin.close()

if not os.path.exists("book.dat"):
    fin = open("book.dat","xb")
    r = Appointment()
    pickle.dump(r,fin)
    fin.close()

sock=socket.socket()
sock.bind(('',100))

def listen():
    sock.listen()
    while True:
        s,c=sock.accept()
        print("Accepted connection from ",c)
        receive(s)
thread=threading.Thread(target=listen,args=())
thread.start()


doctor_sock = socket.socket()
doctor_sock.bind(('',101))

def doctor_listen():
    doctor_sock.listen()
    while True:
        s,c=doctor_sock.accept()
        name = s.recv(1024)
        name = name.decode()
        print("Accepted connection (Doctor) from ",c)
        doctor_added((s,c,name))
d_thread=threading.Thread(target=doctor_listen,args=())
d_thread.start()

def doctor_added(a):
    DOCTOR.append([a[0],a[1][0],a[2]])
    

def receive_and_post(sock):
    while(True):  
        a = sock.recv(1024)
        if(len(a.decode())!=0):
            print("Message received from Client: len({})".format(len(a.decode())))
            handle_response(sock,a.decode())

            
def receive(s):
    thd = threading.Thread(target = receive_and_post, args =(s,))
    thd.start()
    

def handle_response(socket,a):
    if(a[0]=="P"):
        print("Problem statement received")
        a = a[2:]
        file = open("remedy.dat","rb")
        objec = pickle.load(file)
        socket.send(str.encode(str(objec.get_Remedy(a))))
        file.close()

    elif(a[0]=="Q"):
        print("Problem statement received")
        a = a[2:]
        file = open("aid.dat","rb")
        objec = pickle.load(file)
        socket.send(str.encode(str(objec.get_Faid(a))))
        file.close()

    elif (a[0]=="R"):
        temp=""
        pat_name = a[2:]
        for i in range(len(DOCTOR)):
            try:
                DOCTOR[i][0].send(str.encode(pat_name))
                t = DOCTOR[i][0].recv(1024)
                t=t.decode()
                if t=="busy":
                    continue
                if t=="ok":
                    temp  = [DOCTOR[i][1],DOCTOR[i][2]]
                    print(str(temp))
                    break
            except:
                for j in DOCTOR:
                    if j[0]==DOCTOR[i][0]:
                        del DOCTOR[i]
            print(str(temp))
        socket.send(str.encode(str(temp)))      
        
    elif (a[0]=="S"):
        print("Appointment received")
        a = a[2:]
        file = open("book.dat","rb")
        objec = pickle.load(file)
        file.close()
        objec.Add(eval(a))
        file = open("book.dat","wb")
        pickle.dump(objec,file)
        socket.send(str.encode(str("Success")))
        file.close()
        
        
    

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
