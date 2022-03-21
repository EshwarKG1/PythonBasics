from tkinter import *

top = Tk()

top.geometry("500x500")

nam_var = StringVar()
empId_var = StringVar()
age_var = StringVar()
phn_var = StringVar()
emailId_var = StringVar()

def openNewWindow1():

    newWindow = Toplevel(top)
    newWindow.title("New Member window")
    newWindow.geometry("400x400")
    
    def submit(): 
    
        name  = nam_var.get()
        emp_id = empId_var.get()
        age_p = age_var.get()
        phone = phn_var.get()
        email = emailId_var.get()       
        
        with open("book_ui.csv","a") as file:
            file.write(name+",")
            file.write(emp_id+",")
            file.write(age_p+",")
            file.write(phone+",")
            file.write(email+",")
            file.write("\n")
          
        msg = Message(newWindow,text="New member is Successfully added",pady = 50).place(x=100,y=100)
        
        
    def clear1():
        nam_e.delete(0, 'end')
        empID_e.delete(0, 'end')
        age_e.delete(0, 'end')
        phn_e.delete(0, 'end')
        emailId_e.delete(0, 'end')
        
    nam = Label(newWindow,text="Enter the name:").grid(row=1,column=1)
    nam_e = Entry(newWindow,textvariable=nam_var)
    nam_e.grid(row=1,column=2)
    
    empId = Label(newWindow,text="Enter the Employee-ID:").grid(row=2,column=1)
    empID_e = Entry(newWindow,textvariable=empId_var)
    empID_e.grid(row=2,column=2)
    
    age = Label(newWindow,text="Enter the age:").grid(row=3,column=1)
    age_e = Entry(newWindow,textvariable=age_var)
    age_e.grid(row=3,column=2)
    
    phn = Label(newWindow,text="Enter the Phone Number:").grid(row=4,column=1)
    phn_e = Entry(newWindow,textvariable=phn_var)
    phn_e.grid(row=4,column=2)
        
    emailId = Label(newWindow,text="Enter the Email_Id:").grid(row=5,column=1)
    emailId_e = Entry(newWindow,textvariable=emailId_var)
    emailId_e.grid(row=5,column=2)
    
    sub = Button(newWindow,text="submit",command=submit).grid(row=8,column=1)
    
    clr = Button(newWindow,text="clear",command=clear1).grid(row=8,column=2)
    
    ex = Button(newWindow,text="exit",command=newWindow.destroy).grid(row=8,column=3)
 
 
def openNewWindow2():
    
    modify_nam = StringVar()
    new_modify = StringVar()
    newWindow2 = Toplevel(top)
    newWindow2.title("Modify a Member")
    newWindow2.geometry("300x300")
    
    def submit2():
        modifying_name = modify_nam.get()
        new_modify_name = new_modify.get()
        empty=''
        flag_2 = 0
        with open("book_ui.csv","r") as file:
            data = file.readlines()
        for i in data:
            if modifying_name in i:
                flag_2 = 1 
        if flag_2 == 1:
            for i in data:
                if i.startswith(modifying_name):
                    i = i.replace(modifying_name,new_modify_name)
                    empty = empty + i
                else:
                    empty = empty + i
                    
            with open("book_ui.csv","w") as file:
                file.write(empty)
        else:
            print("name not found")
    
    mnam = Label(newWindow2,text="Enter the name to modify :").grid(row=1,column=1)
    mnam_e = Entry(newWindow2,textvariable=modify_nam).grid(row=1,column=2)
    
    m_nam = Label(newWindow2,text="Enter the new name to modify :").grid(row=2,column=1)
    m_nam_e = Entry(newWindow2,textvariable=new_modify).grid(row=2,column=2)
    
    sub2 = Button(newWindow2,text="submit",command=submit2).grid(row=4,column=1)
    ex2 = Button(newWindow2,text="exit",command=newWindow2.destroy).grid(row=4,column=2)


def openNewWindow3():
    
    search_nam = StringVar()
    newWindow3 = Toplevel(top)
    newWindow3.title("Search a Member")
    newWindow3.geometry("500x500")
    
    def submit3():
        
        searching_name = search_nam.get()
        flag = 0
        with open("book_ui.csv","r") as file:
            data_3 = file.readlines()
        for i in data_3:
            if i.startswith(searching_name):
                searching_name1 = i
                msg31 = Message(newWindow3,text=searching_name1,pady = 100).place(x=50,y=50)
                flag = 1
                break
        if flag == 0:
            msg32 = Message(newWindow3,text="Person not found",pady = 50).place(x=50,y=50)
    
    snam = Label(newWindow3,text="Enter the name to search :").grid(row=1,column=1)
    snam_e = Entry(newWindow3,textvariable=search_nam).grid(row=1,column=2)
    
    sub3 = Button(newWindow3,text="submit",command=submit3).grid(row=3,column=1)
    ex3 = Button(newWindow3,text="exit",command=newWindow3.destroy).grid(row=3,column=2)
    
def openNewWindow4():
    
    delete_nam = StringVar()
    newWindow4 = Toplevel(top)
    newWindow4.title("Delete a Member")
    newWindow4.geometry("300x300")
    
    def submit4():
        
        deleting_name = delete_nam.get()
        with open("book_ui.csv","r") as file:
            data_4 = file.readlines()
        with open("book1_ui.csv","a") as file:
            for line in data_4:
                if line.startswith(deleting_name):
                    pass
                else:
                    file.write(line)
        with open("book1_ui.csv","r") as file:
            data_4_1 = file.read()
        with open("book_ui.csv","w") as file:
            file.write(data_4_1)
        with open("book1_ui.csv","w") as file:
            file.write('')
    
    dnam = Label(newWindow4,text="Enter the name to delete :").grid(row=1,column=1)
    dnam_e = Entry(newWindow4,textvariable=delete_nam).grid(row=1,column=2)
    
    sub4 = Button(newWindow4,text="submit",command=submit4).grid(row=3,column=1)
    ex4 = Button(newWindow4,text="exit",command=newWindow4.destroy).grid(row=3,column=2)


l1 = Label(top,text="Select anyone option below").place(x=0,y=0)
b1 = Button(top,text=" Add a new member",command = openNewWindow1).place(x=100,y=50)
b2 = Button(top,text="Modify a member",command = openNewWindow2).place(x=100,y=90)
b3 = Button(top,text="Search a member",command = openNewWindow3).place(x=100,y=130)
b4 = Button(top,text="Delete a member",command = openNewWindow4).place(x=100,y=170)

top.mainloop()