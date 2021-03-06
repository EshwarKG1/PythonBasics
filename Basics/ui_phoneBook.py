from tkinter import *

from tkinter import ttk

import tkinter.messagebox

top = Tk()

top.title("Phone Book")

top.geometry("500x400")

top.resizable(width=False,height=False)

#top.minsize(600,400)

icon = PhotoImage(file="D:\\Eshwar\\documents\\af_icon.png")

top.iconphoto(True,icon)

nam_var = StringVar()
empId_var = StringVar()
age_var = StringVar()
phn_var = StringVar()
emailId_var = StringVar()

def openNewWindow1():

    newWindow = Toplevel(top)
    newWindow.title("New Member window")
    newWindow.geometry("600x300")
    newWindow.resizable(width=False,height=False)
    
    def submit(): 
    
        name  = nam_var.get()
        emp_id = empId_var.get()
        age_p = age_var.get()
        phone = phn_var.get()
        email = emailId_var.get()       
        
        if name != '' and emp_id != '' and age_p !='' and phone != '' and email != '':
            # msg = Message(newWindow,text="New member is Successfully added",padx = 5,pady = 50).grid(row=10,column=2)
            # sub11 = Button(newWindow,text="OK",command=newWindow.destroy,bg='red',fg='white').grid(row=11,column=2)
            tkinter.messagebox.showinfo("Successfully Message","New member is successfully added")
            
            with open("book_ui.csv","a") as file:
                file.write(name+",")
                file.write(emp_id+",")
                file.write(age_p+",")
                file.write(phone+",")
                file.write(email+",")
                file.write("\n")
            clear1()
        else:
            tkinter.messagebox.showwarning("Warning","Blank values can not be entered. Please re-check the values")
    def clear1():
        nam_e.delete(0, 'end')
        empID_e.delete(0, 'end')
        age_e.delete(0, 'end')
        phn_e.delete(0, 'end')
        emailId_e.delete(0, 'end')
        
    nam = Label(newWindow,text="Enter the Name :",font='bold').place(x=80,y=50)#.grid(row=2,column=1,sticky=tkinter.EW)
    nam_e = Entry(newWindow,textvariable=nam_var,font='bold')
    nam_e.place(x=300,y=50)#.grid(row=2,column=2,sticky=tkinter.EW)
    
    empId = Label(newWindow,text="Enter the Employee-ID :",font='bold').place(x=80,y=80)#.grid(row=4,column=1,sticky=tkinter.EW)
    empID_e = Entry(newWindow,textvariable=empId_var,font='bold')
    empID_e.place(x=300,y=80)#.grid(row=4,column=2,sticky=tkinter.EW)
    
    age = Label(newWindow,text="Enter the Age :",font='bold').place(x=80,y=110)#.grid(row=6,column=1,sticky=tkinter.EW)
    age_e = Entry(newWindow,textvariable=age_var,font='bold')
    age_e.place(x=300,y=110)#.grid(row=6,column=2,sticky=tkinter.EW)
    
    phn = Label(newWindow,text="Enter the Phone Number :",font='bold').place(x=80,y=140)#.grid(row=8,column=1,sticky=tkinter.EW)
    phn_e = Entry(newWindow,textvariable=phn_var,font='bold')
    phn_e.place(x=300,y=140)#.grid(row=8,column=2,sticky=tkinter.EW)
        
    emailId = Label(newWindow,text="Enter the Email :",font='bold').place(x=80,y=170)#.grid(row=10,column=1,sticky=tkinter.EW)
    emailId_e = Entry(newWindow,textvariable=emailId_var,font='bold')
    emailId_e.place(x=300,y=170)#.grid(row=10,column=2,sticky=tkinter.EW)
    
    sub = Button(newWindow,text="Submit",command=submit,bg='blue',fg='white',height=1,width=5,font='bold').place(x=80,y=220)#.grid(row=12,column=1,sticky=tkinter.N)
    
    clr = Button(newWindow,text="Clear",command=clear1,bg='orange',fg='white',height=1,width=5,font='bold').place(x=255,y=220)#.grid(row=12,column=2,sticky=tkinter.N)
    
    ex = Button(newWindow,text="Exit",command=newWindow.destroy,bg='red',fg='white',height=1,width=5,font='bold').place(x=430,y=220)#.grid(row=12,column=3,sticky=tkinter.N)
 
 
def openNewWindow2():
    
    modify_nam = StringVar()
    new_modify = StringVar()
    new_modifyemp = StringVar()
    new_modifyage = StringVar()
    new_modifyphone = StringVar()
    new_modifyemail = StringVar()
    newWindow2 = Toplevel(top)
    newWindow2.title("Modify a Member")
    newWindow2.geometry("600x500")
    newWindow2.resizable(width=False,height=False)
        
    def ok():
        empty=''
        modifying_name = modify_nam.get()
        new_modify_name = new_modify.get()
        new_modify_emp = new_modifyemp.get()
        new_modify_age = new_modifyage.get()
        new_modify_phone = new_modifyphone.get()
        new_modify_email = new_modifyemail.get()
        
        if new_modify_name != '' and new_modify_age != '' and new_modify_email != '' and new_modify_emp != '' and new_modify_phone != '':
            with open("book_ui.csv","r") as file:
                data = file.readlines()
            for i in data:
                if i.startswith(modifying_name):
                    my_name = i.split(",")
                    i = i.replace(my_name[0],new_modify_name)
                    i = i.replace(my_name[1],new_modify_emp)
                    i = i.replace(my_name[2],new_modify_age)
                    i = i.replace(my_name[3],new_modify_phone)
                    i = i.replace(my_name[4],new_modify_email)
                    empty = empty + i
                else:
                    empty = empty + i
                
            with open("book_ui.csv","w") as file:
                file.write(empty)
                
            # msg21 = Message(newWindow2,text="Member is Successfully modified",padx = 5,pady = 50).grid(row=12,column=1)
            tkinter.messagebox.showinfo("Modified message","Member is Successfully modified")
        else:
            tkinter.messagebox.showwarning("Warning","Blank values can not be entered. Please re-check the values")
    
    def submit2():
        modifying_name = modify_nam.get()
        flag_2 = 0
        if modifying_name != '':
            with open("book_ui.csv","r") as file:
                data = file.readlines()
            for i in data:
                if i.startswith(modifying_name):
                    my_name2 = i.split(",")
                    if modifying_name == my_name2[0]:
                        flag_2 = 1                       
                    
            if flag_2 == 1:
                m_nam = Label(newWindow2,text="Full Name :",font='bold').place(x=110,y=150)#.grid(row=4,column=1,sticky=tkinter.EW)
                new_modify.set(my_name2[0])
                m_nam_e = Entry(newWindow2,textvariable=new_modify,font='bold')
                m_nam_e.place(x=300,y=150)#.grid(row=4,column=2,sticky=tkinter.EW)
                
                m_nam = Label(newWindow2,text="Employee ID :",font='bold').place(x=110,y=190)#.grid(row=5,column=1,sticky=tkinter.EW)
                new_modifyemp.set(my_name2[1])
                me_nam_e = Entry(newWindow2,textvariable=new_modifyemp,font='bold')
                me_nam_e.place(x=300,y=190)#.grid(row=5,column=2,sticky=tkinter.EW)
                
                m_nam = Label(newWindow2,text="Age :",font='bold').place(x=110,y=230)#.grid(row=6,column=1,sticky=tkinter.EW)
                new_modifyage.set(my_name2[2])
                ma_nam_e = Entry(newWindow2,textvariable=new_modifyage,font='bold')
                ma_nam_e.place(x=300,y=230)#.grid(row=6,column=2,sticky=tkinter.EW)
                
                m_nam = Label(newWindow2,text="Contact number :",font='bold').place(x=110,y=270)#.grid(row=7,column=1,sticky=tkinter.EW)
                new_modifyphone.set(my_name2[3])
                mp_nam_e = Entry(newWindow2,textvariable=new_modifyphone,font='bold')
                mp_nam_e.place(x=300,y=270)#.grid(row=7,column=2,sticky=tkinter.EW)
                
                m_nam = Label(newWindow2,text="Email_Id :",font='bold').place(x=110,y=310)#.grid(row=8,column=1,sticky=tkinter.EW)
                new_modifyemail.set(my_name2[4])
                mm_nam_e = Entry(newWindow2,textvariable=new_modifyemail,font='bold')
                mm_nam_e.place(x=300,y=310)#.grid(row=8,column=2,sticky=tkinter.EW)
                
                def clear2():
                    m_nam_e.delete(0,'end')
                    me_nam_e.delete(0,'end')
                    ma_nam_e.delete(0,'end')
                    mp_nam_e.delete(0,'end')
                    mm_nam_e.delete(0,'end')
                
                bt21 = Button(newWindow2,text="Modify",command=ok,bg='orange',fg='white',font='bold').place(x=110,y=360)#.grid(row=10,column=1,sticky=tkinter.N)
                clr2 = Button(newWindow2,text="Clear",command=clear2,bg='orange',fg='white',height=1,width=5,font='bold').place(x=430,y=360)#.grid(row=10,column=2,sticky=tkinter.N)

            else:
                # msg22 = Message(newWindow2,text="Error!!! Member not found",pady = 50).place(x=100,y=100)
                tkinter.messagebox.showerror("Error","Member not found")
        else:
            pass          
    
    mnam = Label(newWindow2,text="Enter the name to modify :",font='bold').place(x=110,y=50)#.grid(row=1,column=1,sticky=tkinter.EW)
    mnam_e = Entry(newWindow2,textvariable=modify_nam,font='bold')
    mnam_e.place(x=300,y=50)#.grid(row=1,column=2,sticky=tkinter.EW)
    
    sub2 = Button(newWindow2,text="Submit",command=submit2,bg='blue',fg='white',height=1,width=5,font='bold').place(x=110,y=90)#.grid(row=2,column=1,sticky=tkinter.N)
    ex2 = Button(newWindow2,text="Exit",command=newWindow2.destroy,bg='red',fg='white',height=1,width=5,font='bold').place(x=430,y=90)#.grid(row=2,column=2,sticky=tkinter.N)


def openNewWindow3():
    
    search_nam = StringVar()
    newWindow3 = Toplevel(top)
    newWindow3.title("Search a Member")
    newWindow3.geometry("700x500")
    newWindow3.resizable(width=False,height=False)
    
    def clear3():
        snam_e.delete(0,'end')
    
    def submit3():
        searching_name = search_nam.get()
        flag = 0
        if searching_name != '':
            with open("book_ui.csv","r") as file:
                data_3 = file.readlines()
            for i in data_3:
                if i.startswith(searching_name):
                    searching_name1 = i.split(",")
                    if searching_name == searching_name1[0] :
                        lb31 = Label(newWindow3,text="Name :",font='bold').place(x=140,y=124)#.grid(row=6,column=1,sticky=tkinter.EW)
                        msg31 = Message(newWindow3,text=searching_name1[0],padx=5,pady=35,font='bold').place(x=330,y=90)#.grid(row=6,column=2,sticky=tkinter.N)
                        lb32 = Label(newWindow3,text="Employee ID :",font='bold').place(x=140,y=184)#.grid(row=8,column=1,sticky=tkinter.EW)
                        msg32 = Message(newWindow3,text=searching_name1[1],padx=5,pady=35,font='bold').place(x=330,y=150)#.grid(row=8,column=2,sticky=tkinter.N)
                        lb33 = Label(newWindow3,text="Age :",font='bold').place(x=140,y=244)#.grid(row=9,column=1,sticky=tkinter.EW)
                        msg33 = Message(newWindow3,text=searching_name1[2],padx=5,pady=35,font='bold').place(x=330,y=210)#.grid(row=9,column=2,sticky=tkinter.N)
                        lb34 = Label(newWindow3,text="Phone Number :",font='bold').place(x=140,y=304)#.grid(row=10,column=1,sticky=tkinter.EW)
                        msg34 = Message(newWindow3,text=searching_name1[3],padx=5,pady=35,font='bold').place(x=330,y=270)#.grid(row=10,column=2,sticky=tkinter.N)
                        lb35 = Label(newWindow3,text="Email :",font='bold').place(x=140,y=368)#.grid(row=11,column=1,sticky=tkinter.EW)
                        msg35 = Message(newWindow3,text=searching_name1[4],padx=5,pady=40,font='bold').place(x=330,y=330)#.grid(row=11,column=2,sticky=tkinter.N)
                        # sub31 = Button(newWindow3,text="Ok",command=newWindow3.destroy,bg='red',fg='white',height=1,width=5).place(x=400,y=340)#.grid(row=11,column=2,sticky=tkinter.N)
                        flag = 1
                        break                
            if flag == 0:
                # msg32 = Message(newWindow3,text="Error!!! Person not found",pady = 50).place(x=50,y=50)
                tkinter.messagebox.showerror("Error","Member not found")
        else:
            pass
    
    snam = Label(newWindow3,text="Enter the name to search :",font='bold').place(x=140,y=20)#.grid(row=1,column=1,sticky=tkinter.EW)
    snam_e = Entry(newWindow3,textvariable=search_nam,font='bold')
    snam_e.place(x=330,y=20)#.grid(row=1,column=2,sticky=tkinter.EW)
    
    sub3 = Button(newWindow3,text="Submit",command=submit3,bg='blue',fg='white',height=1,width=5,font='bold').place(x=140,y=50)#.grid(row=3,column=1,sticky=tkinter.N)
    clr3 = Button(newWindow3,text="Clear",command=clear3,bg='orange',fg='black',height=1,width=5,font='bold').place(x=300,y=50)#.grid(row=3,column=2,sticky=tkinter.N)
    ex3 = Button(newWindow3,text="Exit",command=newWindow3.destroy,bg='red',fg='white',height=1,width=5,font='bold').place(x=460,y=50)#.grid(row=3,column=3,sticky=tkinter.N)
    
def openNewWindow4():
    
    delete_nam = StringVar()
    newWindow4 = Toplevel(top)
    newWindow4.title("Delete a Member")
    newWindow4.geometry("550x200")
    newWindow4.resizable(width=False,height=False)
    
    def clear4():
        dnam_e.delete(0,'end')
    
    def submit4():
        
        deleting_name = delete_nam.get()
        if deleting_name != '':
            count4 = 0
            with open("book_ui.csv","r") as file:
                data_4 = file.readlines()
            with open("book1_ui.csv","a") as file:
                for line in data_4:
                    if line.startswith(deleting_name):
                        line4 = line.split(",")
                        if deleting_name == line4[0]:
                            count4=1
                            pass
                        else:
                            file.write(line)
                    else:
                        file.write(line)
            with open("book1_ui.csv","r") as file:
                data_4_1 = file.read()
            with open("book_ui.csv","w") as file:
                file.write(data_4_1)
            with open("book1_ui.csv","w") as file:
                file.write('')
            
            if count4 == 1:
                #msg41 = Message(newWindow4,text="Successfully deleted",pady = 50).place(x=50,y=50)
                tkinter.messagebox.showinfo("Successfully deleted","Successfully deleted the Member")
            else:
                #msg41 = Message(newWindow4,text="Error!!! Member not found can not be deleted",pady = 100).place(x=50,y=50)
                tkinter.messagebox.showerror("Error","Member not found, can not be deleted")
        else:
            pass
    
    dnam = Label(newWindow4,text="Enter the name to delete :",font='bold').place(x=50,y=35)#.grid(row=1,column=1,sticky=tkinter.EW)
    dnam_e = Entry(newWindow4,textvariable=delete_nam,font='bold')
    dnam_e.place(x=250,y=35)#.grid(row=1,column=2,sticky=tkinter.EW)
    
    sub4 = Button(newWindow4,text="Submit",command=submit4,bg='blue',fg='white',height=1,width=5,font='bold').place(x=50,y=95)#.grid(row=4,column=1,sticky=tkinter.N)
    clr4 = Button(newWindow4,text="Clear",command=clear4,bg='orange',fg='black',height=1,width=5,font='bold').place(x=215,y=95)#.grid(row=4,column=2,sticky=tkinter.N)
    ex4 = Button(newWindow4,text="Exit",command=newWindow4.destroy,bg='red',fg='white',height=1,width=5,font='bold').place(x=380,y=95)

def onClick():
    res = tkinter.messagebox.askquestion('Exit Application','Do you really want to exit')
    if res == 'yes' :
        top.destroy()

#my_font = Font(size=8,weight="bold")
# l1 = Label(top,text="Select anyone option below",bg='yellow',bd=4).place(x=70,y=20)
b1 = Button(top,text="Add a New member",command = openNewWindow1,bg='orange',fg='white',height=2,width=15,font='bold').place(x=170,y=50)
b2 = Button(top,text="Modify a member",command = openNewWindow2,bg='orange',fg='white',height=2,width=15,font='bold').place(x=170,y=110)
b3 = Button(top,text="Search a member",command = openNewWindow3,bg='orange',fg='white',height=2,width=15,font='bold').place(x=170,y=170)
b4 = Button(top,text="Delete a member",command = openNewWindow4,bg='orange',fg='white',height=2,width=15,font='bold').place(x=170,y=230)
b5 = Button(top,text="Exit",command = onClick,bg='red',fg='white',height=2,width=15,font='bold').place(x=170,y=290)

top.mainloop()
