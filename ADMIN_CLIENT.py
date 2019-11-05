import pickle
import socket
import threading

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
            self.problem_and_remedy[Problem]=[]
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
        
    def modify_Name(self,n):
        self.dname = n
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

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('127.0.0.1',100))

while True:
    print("1) Remedies Management")
    print("2) First-Aid Management")
    print("3) Doctor Management")
    print("4) EXIT")
    a = input("Enter your choice : ")
    if a=="1":
        more_remedies = True
        remedies = []
        print("1) Add Problems and Remedies\n")
        print("2) Edit Problems and Remedies\n")
        print("3) Delete Problems and Remedies\n")
        print("4) Exit\n")
        t = input("")
        if(t=="1"):
            prob = input("Enter problem : ")
            while(more_remedies==True):
                remedies.append(input("Enter Remedy : "))
                if(input("Enter more Remedy (Y/N) : ")in ["Y","y"]):
                    pass
                else:
                    more_remedies=False
            file = open("remedy.dat","rb")
            objec = pickle.load(file)
            objec.add_Problem_and_remedy(prob,remedies)
            file.close()
            file = open("remedy.dat","wb")
            pickle.dump(objec,file)
            file.close()


        elif (t=="2"):
            prob = input("Enter problem: ")
            file = open("remedy.dat","rb")
            objec = pickle.load(file)
            objec.edit_Remedy(prob)
            file.close()
            file = open("remedy.dat","wb")
            pickle.dump(objec,file)
            file.close()


        elif(t=="3"):
            prob = input("Enter problem: ")
            file = open("remedy.dat","rb")
            objec = pickle.load(file)
            objec.delete_Remedy(prob)
            file.close()
            file = open("remedy.dat","wb")
            pickle.dump(objec,file)
            file.close()

        else:
            pass
        

    elif a=="2":
        more_aids = True
        aids = []
        print("1) Add Problems and aid\n")
        print("2) Edit Problems and aid\n")
        print("3) Delete Problems and aid\n")
        print("4) Exit\n")
        t = input("")
        if(t=="1"):
            prob = input("Enter problem : ")
            while(more_aids==True):
                aids.append(input("Enter Aim : "))
                if(input("Enter more Aid (Y/N) : ")in ["Y","y"]):
                    pass
                else:
                    more_aids=False
            file = open("aid.dat","rb")
            objec = pickle.load(file)
            objec.add_Problem_and_faid(prob,aids)
            file.close()
            file = open("aid.dat","wb")
            pickle.dump(objec,file)
            file.close()


        elif (t=="2"):
            prob = input("Enter problem: ")
            file = open("aid.dat","rb")
            objec = pickle.load(file)
            objec.edit_Faid(prob)
            file.close()
            file = open("aid.dat","wb")
            pickle.dump(objec,file)
            file.close()


        elif(t=="3"):
            prob = input("Enter problem: ")
            file = open("aid.dat","rb")
            objec = pickle.load(file)
            objec.delete_Faid(prob)
            file.close()
            file = open("aid.dat","wb")
            pickle.dump(objec,file)
            file.close()

        else:
            pass


    elif(a=="3"):
        print("1) Add Doctor detail\n")
        print("2) Edit Doctor detail\n")
        print("3) Delete Doctor detail\n")
        print("4) Exit\n")
        t = input("")
        if(t=="1"):
            file = open("doctor.dat","rb")
            objec = pickle.load(file)
            objec.add_doctor()
            file.close()
            file = open("doctor.dat","wb")
            pickle.dump(objec,file)
            file.close()


        elif (t=="2"):
            file = open("doctor.dat","rb")
            objec = pickle.load(file)
            print("1) Qualification\n")
            print("2) Hospital name\n")
            print("3) Hospital type\n")
            print("4) Exit\n")
            m=input("")
            if m=="1":
                q=input("Enter new qualifications: ")
                objec.modify_Qualification(q)
            elif m=="2":
                hn=input("Enter new hospital name: ")
                objec.modify_HName(hn)
            elif m=="3":
                ht=input("Enter new hospital type: ")
                objec.modify_HType(ht)
            else:
                pass
            file.close()
            file = open("doctor.dat","wb")
            pickle.dump(objec,file)
            file.close()


        elif(t=="3"):
            prob = input("Enter problem: ")
            file = open("doctor.dat","rb")
            objec = pickle.load(file)
            objec.delete_Faid(prob)
            file.close()
            file = open("doctor.dat","wb")
            pickle.dump(objec,file)
            file.close()

        else:
            pass
    elif (a=="4"):
        print ("Thank you")
        break
