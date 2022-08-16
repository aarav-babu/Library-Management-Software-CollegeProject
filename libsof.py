#changes done:
#changed the variable sid to pid (person id) as it's used for both student and teacher
#pid can be used for librarian too if needed
#request book feature does not take the user back to the login page,it works just as intended now
#simplified code as both students and teachers have same functionality
#so student and teacher sections are done...yayy
#added librarian code for completion
#text file display to terminal and writing in it issue resolved



import sys #exit
import os 
import csv

clear = lambda: os.system('cls') #clear screen
hold = lambda: input()  #shows output on screen for sometime 

F = open("Lib2.csv","r")
L = F.read()
D = L.replace(',',' ')
D = D.strip()  
R = D.split('\n')

main=[]
main.append(R[0].split())

for i in R[1::]: 
    i = i.split() 
    l1 = []
    l1.append(int(i[0]))
    l1.append(i[1])
    l1.append(int(i[2]))
    l1.append(int(i[3]))
    l1.append(i[4])
    main.append(l1)

f2 = open("LG.csv","r")
l = f2.read()
d = l.replace(',',' ')
d = d.strip()  
r = d.split('\n')

d = dict()   #{ lgid:pass} d={"aarav2":12,....}
for f in r[1::]:
    f=f.split()
    d[f[0]]=f[1]

    
def st_home(text):
    
    lgid=input("LOGIN ID: ")
    if(lgid in d):
        
        pas=input("PASSWORD: ")
        
        if(d[lgid]==pas): #pass() #d[lgid]=pass
        
            #prog 
            clear()
            opt=0
            print("\t\t\tWelcome "+text+": ",lgid)
        
            while(opt!=5):
        
                print("\n1.View Available Books\n2.Borrow Book\n3.Return Book\n4.Request Book\n5.Exit")
                opt=int(input("Enter the option: "))
        
                if(opt==1):
                    
                    if text == 'Student':
                        view()
                        hold()
                        clear()

                    else:
                        tview()
                        hold()
                        clear()

                elif(opt==2):
        
                    borrow(lgid)
                    hold()
                    clear()
        
                elif(opt==3):
        
                    ret()
                    hold()
                    clear()
        
                elif(opt==4):
        
                    req(lgid)
                    hold()
                    clear()
        
                elif(opt==5):
        
                    sys.exit()
        
            else:
                print("Enter Valid Option ")            
        else:    
            print("Wrong Password")
            hold()
    else:
        print("LOGIN ID Not Found ")
        hold()

    
def view():
    
    print("\n",main[0][0],main[0][1])
    for i in main:
        if(i[4]=='1'): #if 1 then available
            print(i[0],i[1])

def tview():

    print("\n",main[0][0],main[0][1],'id')
    for i in main[1::]:
        if i[4] == '1':
            print(i[0],i[1],'NIL')
        else:
            print(i[0],i[1],i[4])


def borrow(pid):
    
    view()

    b=int(input("Enter slno of book you want to borrow"))
    res=list(filter(lambda s:s[4]=='1',main))
    flag=0
    
    for u in res:
        if(b==u[0]):
            flag=1
            break
    if(flag==1):
        for i in main:
            if(b==i[0]):
                print("The details of the book you want to borrow are:")
                print(i[0],i[1],i[3])
            break
     
        c=input("Are you sure you want to borrow (Y/N)")
        if(c=='Y' or c=='y'):
            for i in main:
            
                if(b==i[0]):
                    main[main.index(i)][4]=pid
                    with open('Lib2.csv', 'w+', newline='') as file: #w-write(appends,opens a file then appends) #read (reads the file)
                        writer = csv.writer(file)
                        writer.writerows(main) #feeds list            
                    break
        
        elif(c=='N' or c=='n'):
            #clear() #clears the mistake by the user but at the same time the whole screen will get cleared 
                     #leaving only the borrow function on display
            borrow(pid) #try
        
        else:
            print("Enter Valid Input")
          
def ret():
    
    b=int(input("Enter sl.no of book you want to return: "))
    res=list(filter(lambda s:s[4]!='1',main))
    
    flag=0
    for u in res:
        if(b==u[0]):
            flag=1
            break
    
    if(flag==1):
        for i in main:
            if(b==i[0]):
                print("The details of the book you want to return are:")
                print(i[0],i[1],i[3])
                break
        
        c=input("Are you sure you want to return (Y/N)")
        if(c=='Y' or c=='y'):
            for i in main:
                if(b==i[0]):
                    main[main.index(i)][4]='1'
                    # print(main) no problem here
                    with open('Lib2.csv', 'w+', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(main)
                    break
        
        elif(c=='N' or c=='n'):

            #clear() #same reason as borrow fn while putting n/N for borrow.
            ret()
        
        else:
            print("Enter Valid Input")
           
    else:
        print("Enter Valid Input")
    
def req(pid):
    
    c = input("Enter Title of Book you want to request ")
    c = c + "\t"*13 + pid +"\n" 
    f = open("Req.txt","a+")  
    f.write(c)
    f.close()

def lib():
    
    lgi = input("LOGIN ID: ")
    if(lgi in d):
        pasl=input("PASSOWRD: ")
        
        if(d[lgi]==pasl):
            #prog 
            clear()
            lopt=0
            print("\t\t\tWelcome Librarian: ",lgi)
            
            while(lopt!=4):
            
                print("\n1.View Books\n2.Edit Book List\n3.View Requested Books\n4.Exit") 
                lopt=int(input("Enter the option: "))
                
                if(lopt==1):
                    libview()
                    hold()
                    clear()
                
                elif(lopt==2):
                    edit()
                    hold()
                    clear()
                
                elif(lopt==3):
                    viewreq()
                    hold()
                    clear()

                elif(lopt==4):
                    sys.exit()
                else:
                    print("Enter Valid Option ")            
        else:    
            print("Wrong Password")
            hold()
    else:
        print("LOGIN ID Not Found ")
        hold()

def libview():
    
    for i in main:
        print(i[0],i[1],i[2],i[3],i[4])

def edit():
    
    clear() 
    eopt=0
    
    while(eopt!=4):
        print("\n1.Add New Book\n2.Delete Book\n3.Change Books Details\n4.Exit Edit Menu\n5.Exit")
        eopt=int(input("Enter option: "))
    
        if(eopt==1):
            add()
            hold()
            clear()
    
        elif(eopt==2):
            delete()
            hold()
            clear()
    
        elif(eopt==3):
            change()
            hold()
            clear()
    
        elif(eopt==4):
            return
    
        elif(eopt==5):
            sys.exit()
    
        else:
            print("Enter Valid Input")
            hold()

def add():
    
    l1=[]
    print("Enter Details of the New Book")
    l1.append(int(input("Enter the serial number:")))
    l1.append(input("Enter the title of the book: (Add '_' for space) "))
    l1.append(input("Enter the Due Date of the book:"))
    l1.append(input("Enter cost of the book:"))
    l1.append("1")
    print("Details of the book you want to add are:")
    print("\n",main[0])
    print(l1)
    
    c=input("Are you sure you want to add this book (Y/N)?")
    
    if(c=='Y' or c=='y'):
        main.append(l1)
        sort()
        with open('Lib2.csv', 'w+', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(main)
    
    elif(c=='N' or c=='n'):
        add() 
    
    else:
        print("Enter Valid Input")

def delete():
    
    b=int(input("Enter slno of book you want to Delete: "))
    flag=0
    ind=0
    
    for u in main:
        if(b==u[0]):
            flag=1
            break
    
    if(flag==1):
        for i in main:
            if(b==i[0]):
                print("The details of the book you want to delete are:")
                print(i[0],i[1],i[3])
                ind=main.index(i)
                break
        
        c=input("Are you sure you want to Delete (Y/N)")
        if(c=='Y' or c=='y'):
            main.pop(ind)
            with open('Lib2.csv', 'w+', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(main)
        
        elif(c=='N' or c=='n'):
            delete()
        
        else:
            print("Enter a Valid Input")
            hold()
    else:
        print("Enter Valid Serial Number")
        hold()

def change():
    b=int(input("Enter slno of book you want to Change/Edit: "))
    flag=0
    ind=0
    l1=[]
    
    for u in main:
        if(b==u[0]):
            flag=1
            break
    
    if(flag==1):
        for i in main:
             if(b==i[0]):
                print("The details of the book you want to Edit are:")
                print(i[0],i[1],i[3])
                ind=main.index(i)
                break           
        
        print("Enter Details of the Edited Book")
        l1.append(int(input("Enter the serial number:")))
        l1.append(input("Enter the title of the book:"))
        l1.append(input("Enter the Due Date of the book:"))
        l1.append(input("Enter cost of the book:"))
        l1.append("1")   
        
        c=input("Are you sure you want to Edit (Y/N)")
        if(c=='Y' or c=='y'):
            main.pop(ind)
            main.append(l1)
            sort()
            #sort main
            with open('Lib2.csv', 'w+', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(main)
        
        elif(c=='N' or c=='n'):
            change()
        
        else:
            print("Enter a Valid Input")
            hold()
    else:
        print("Enter Valid Serial Number")
        hold()

def sort():
    n=len(main)-1
    for i in range(1,n):
        for j in range(1,n-i+1):
            if(main[j][0]>main[j+1][0]):
                main[j],main[j+1]=main[j+1],main[j]            

def viewreq():
    clear()
    f=open("Req.txt","r")
    for line in f:
        print(line)
    f.close()            

#main has all data
opt=0
while(opt!=4):
    
    clear()
    print("\t\t\tWELCOME TO LIBRARY MANAGEMENT SOFTWARE")
    print("1.Student\n2.Teacher\n3.Librarian\n4.Exit")
    opt=int(input("Enter the option "))
    
    if(opt==1): #student
        clear()
        st_home('Student')
    
    elif(opt==2): #teacher
        clear()
        st_home('Faculty')
    
    elif(opt==3): #librarian
        clear()
        lib()
    
    elif(opt==4):
        sys.exit()
    
    else:
        print("Enter Valid Input")
        hold()
        
        
