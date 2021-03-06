# Importing the required moduls

from tkinter import *

import tkinter.messagebox

# Creating the main page
top = Tk()

# Main page dimensions and title
top.title("Acufore Phone Book")

top.geometry("500x450")

top.resizable(width=False,height=False)# cannot change the window size
# if width is True or height is True then window can be changed with size

#top.minsize(600,400) # assigning the minimum size

# Acufore Icon
icon = PhotoImage(file="D:\\Eshwar\\documents\\af_icon.png")

top.iconphoto(True,icon)

# Add member window/page
def openNewWindow1():
    
    # Creating the add a member page
    newWindow = Toplevel(top)
    newWindow.title("New Member Entry")
    newWindow.geometry("600x300")
    newWindow.resizable(width=False,height=False)
    
    # Creating the variables to store the values
    nam_var = StringVar()
    empId_var = StringVar()
    age_var = StringVar()
    phn_var = StringVar()
    emailId_var = StringVar()
    
    # function submit the values and add in the file
    def submit(): 
        
        # checking for emp-id
        flag1 = 0
        flag11 = 0
        
        # Checking emp_id so that duplicate are not entered 
        with open("book_ui.csv","r") as file:
            data1 = file.readlines()
        
        emp_id1 = empId_var.get()
        for i in data1:
            em1 = i.split(",")
            if emp_id1 == em1[1]:
                flag1 = 1
                break
        
        # Retriving the values from Entry 
        name  = nam_var.get()
        emp_id = empId_var.get()
        age_p = age_var.get()
        phone = phn_var.get()
        email = emailId_var.get()   
        
        name = name.lower()
        
        # checking the length of contact number
        if len(phone)>10 or len(phone)<10:
            flag11 = 1
                  
        # Checking if the string is not empty
        if name != '' and emp_id != '' and age_p !='' and phone != '' and email != '':
            
            # emp_ID checking
            if flag1 == 0:
            
                # phone number length checking
                if flag11 == 0:
                    # Displaying the successfully message type 1
                    # msg = Message(newWindow,text="New member is Successfully added",padx = 5,pady = 50).grid(row=10,column=2)
                    # sub11 = Button(newWindow,text="OK",command=newWindow.destroy,bg='red',fg='white').grid(row=11,column=2)
                    
                    # Displaying the successfully message type 2
                    tkinter.messagebox.showinfo("Successfully Message","New member is successfully added")
                    
                    # Adding all values to the file
                    with open("book_ui.csv","a") as file:
                        file.write(name+",")
                        file.write(emp_id+",")
                        file.write(age_p+",")
                        file.write(phone+",")
                        file.write(email+",")
                        file.write("\n")
                    clear1()
                else:
                    tkinter.messagebox.showerror("ERROR","Phone number should be 10 digits ")
            else:
                tkinter.messagebox.showerror("ERROR","Employee ID already present. Please enter the valid one")
        # If string is empty displaying the warning message
        else:
            tkinter.messagebox.showwarning("WARNING","Blank values can not be entered. Please re-check the values")
    
    # Using clear function to clear the values present in entry
    def clear1():
        nam_e.delete(0, 'end')
        empID_e.delete(0, 'end')
        age_e.delete(0, 'end')
        phn_e.delete(0, 'end')
        emailId_e.delete(0, 'end')
    
    # Label and Entry values to read the name from user
    nam = Label(newWindow,text="Enter the Name :",font=('Arial',12,'bold')).place(x=80,y=50)#.grid(row=2,column=1,sticky=tkinter.EW)
    nam_e = Entry(newWindow,textvariable=nam_var,font=('Arial',12,'bold'))
    nam_e.place(x=320,y=50)#.grid(row=2,column=2,sticky=tkinter.EW)
    
    # Label and Entry values to read the Employee-ID from user
    empId = Label(newWindow,text="Enter the Employee-ID :",font=('Arial',12,'bold')).place(x=80,y=80)#.grid(row=4,column=1,sticky=tkinter.EW)
    empID_e = Entry(newWindow,textvariable=empId_var,font=('Arial',12,'bold'))
    empID_e.place(x=320,y=80)#.grid(row=4,column=2,sticky=tkinter.EW)
        
    # Label and Entry values to read the Age from user
    age = Label(newWindow,text="Enter the Age :",font=('Arial',12,'bold')).place(x=80,y=110)#.grid(row=6,column=1,sticky=tkinter.EW)
    age_e = Entry(newWindow,textvariable=age_var,font=('Arial',12,'bold'))
    age_e.place(x=320,y=110)#.grid(row=6,column=2,sticky=tkinter.EW)
    
    # Label and Entry values to read the Contact number from user
    phn = Label(newWindow,text="Enter the Phone Number :",font=('Arial',12,'bold')).place(x=80,y=140)#.grid(row=8,column=1,sticky=tkinter.EW)
    phn_e = Entry(newWindow,textvariable=phn_var,font=('Arial',12,'bold'))
    phn_e.place(x=320,y=140)#.grid(row=8,column=2,sticky=tkinter.EW)
        
    # Label and Entry values to read the Email from user
    emailId = Label(newWindow,text="Enter the Email :",font=('Arial',12,'bold')).place(x=80,y=170)#.grid(row=10,column=1,sticky=tkinter.EW)
    emailId_e = Entry(newWindow,textvariable=emailId_var,font=('Arial',12,'bold'))
    emailId_e.place(x=320,y=170)#.grid(row=10,column=2,sticky=tkinter.EW)
    
    # Submit button to add values to file
    sub = Button(newWindow,text="Submit",command=submit,bg='blue',fg='white',height=1,width=5,font=('Arial',12,'bold')).place(x=80,y=220)#.grid(row=12,column=1,sticky=tkinter.N)
    
    # Clear button to clear the values present in the entry
    clr = Button(newWindow,text="Clear",command=clear1,bg='orange',fg='white',height=1,width=5,font=('Arial',12,'bold')).place(x=265,y=220)#.grid(row=12,column=2,sticky=tkinter.N)
    
    # Exit button to exit from the page and destory it
    ex = Button(newWindow,text="Exit",command=newWindow.destroy,bg='red',fg='white',height=1,width=5,font=('Arial',12,'bold')).place(x=445,y=220)#.grid(row=12,column=3,sticky=tkinter.N)
 
# Modify a member Window/page
def openNewWindow2():
    
    # Creating the variables to store the values for modification 
    modify_nam = StringVar()
    new_modify = StringVar()
    new_modifyemp = StringVar()
    new_modifyage = StringVar()
    new_modifyphone = StringVar()
    new_modifyemail = StringVar()
    
    # Creating the modify page
    newWindow2 = Toplevel(top)
    newWindow2.title("Modify a Member")
    newWindow2.geometry("600x500")
    newWindow2.resizable(width=False,height=False) 
    
    # To modify the changes asked by the user        
    def ok():
        # Storing the values in empty string
        empty=''
        # Retriving the values to modify
        modifying_name = modify_nam.get()
        new_modify_name = new_modify.get()
        new_modify_emp = new_modifyemp.get()
        new_modify_age = new_modifyage.get()
        new_modify_phone = new_modifyphone.get()
        new_modify_email = new_modifyemail.get()
        
        modifying_name = modifying_name.lower()
        new_modify_name = new_modify_name.lower()
        
        # Checking if the string is not empty
        if new_modify_name != '' and new_modify_age != '' and new_modify_email != '' and new_modify_emp != '' and new_modify_phone != '':
            
            # Logic to modify the changes asked by the user
            with open("book_ui.csv","r") as file:
                data = file.readlines()
            for i in data:
                if i.startswith(modifying_name):
                    my_name = i.split(",")
                    if modifying_name == my_name[0]:
                        i = i.replace(my_name[0],new_modify_name)
                        i = i.replace(my_name[1],new_modify_emp)
                        i = i.replace(my_name[2],new_modify_age)
                        i = i.replace(my_name[3],new_modify_phone)
                        i = i.replace(my_name[4],new_modify_email)
                        empty = empty + i
                        my_name = []
                    else:
                        empty = empty + i
                else:
                    empty = empty + i
                
            with open("book_ui.csv","w") as file:
                file.write(empty)
                
            # Displaying successfully message type 1 and type 2
            # msg21 = Message(newWindow2,text="Member is Successfully modified",padx = 5,pady = 50).grid(row=12,column=1)
            tkinter.messagebox.showinfo("Modified message","Member is Successfully modified")
        
        # If string is empty displaying the warning message
        else:
            tkinter.messagebox.showwarning("WARNING","Blank values can not be entered. Please re-check the values")
    
    # Recieving the name to modify 
    def submit2():
        
        # retriving the name
        modifying_name = modify_nam.get()
        modifying_name = modifying_name.lower()
        flag_2 = 0
        # Checking if the string is not empty 
        if modifying_name != '':
            
            # Logic find the name if it present in the file
            with open("book_ui.csv","r") as file:
                data = file.readlines()
            for i in data:
                if i.startswith(modifying_name):
                    my_name22 = i.split(",")
                    #print(modifying_name)
                    #print(my_name2[0])
                    if modifying_name == my_name22[0]:
                        my_name2 = my_name22
                        flag_2 = 1
                    my_name22 = []
            # If it is present
            if flag_2 == 1:
            
                # Label and Entry with previous entered values
                m_nam = Label(newWindow2,text="Full Name :",font=('Arial',12,'bold')).place(x=110,y=150)#.grid(row=4,column=1,sticky=tkinter.EW)
                new_modify.set(my_name2[0])# used intial the values and display to the user
                m_nam_e = Entry(newWindow2,textvariable=new_modify,font=('Arial',12,'bold'))
                m_nam_e.place(x=320,y=150)#.grid(row=4,column=2,sticky=tkinter.EW)
                
                # Label and Entry with previous entered values
                m_nam = Label(newWindow2,text="Employee ID :",font=('Arial',12,'bold')).place(x=110,y=190)#.grid(row=5,column=1,sticky=tkinter.EW)
                new_modifyemp.set(my_name2[1])# used intial the values and display to the user
                me_nam_e = Entry(newWindow2,textvariable=new_modifyemp,font=('Arial',12,'bold'))
                me_nam_e.place(x=320,y=190)#.grid(row=5,column=2,sticky=tkinter.EW)
                
                # Label and Entry with previous entered values
                m_nam = Label(newWindow2,text="Age :",font=('Arial',12,'bold')).place(x=110,y=230)#.grid(row=6,column=1,sticky=tkinter.EW)
                new_modifyage.set(my_name2[2])# used intial the values and display to the user
                ma_nam_e = Entry(newWindow2,textvariable=new_modifyage,font=('Arial',12,'bold'))
                ma_nam_e.place(x=320,y=230)#.grid(row=6,column=2,sticky=tkinter.EW)
                
                # Label and Entry with previous entered values
                m_nam = Label(newWindow2,text="Contact number :",font=('Arial',12,'bold')).place(x=110,y=270)#.grid(row=7,column=1,sticky=tkinter.EW)
                new_modifyphone.set(my_name2[3])# used intial the values and display to the user
                mp_nam_e = Entry(newWindow2,textvariable=new_modifyphone,font=('Arial',12,'bold'))
                mp_nam_e.place(x=320,y=270)#.grid(row=7,column=2,sticky=tkinter.EW)
                
                # Label and Entry with previous entered values
                m_nam = Label(newWindow2,text="Email_Id :",font=('Arial',12,'bold')).place(x=110,y=310)#.grid(row=8,column=1,sticky=tkinter.EW)
                new_modifyemail.set(my_name2[4])# used intial the values and display to the user
                mm_nam_e = Entry(newWindow2,textvariable=new_modifyemail,font=('Arial',12,'bold'))
                mm_nam_e.place(x=320,y=310)#.grid(row=8,column=2,sticky=tkinter.EW)
                
                # Using clear function to clear the values present in entry
                def clear2():
                    m_nam_e.delete(0,'end')
                    me_nam_e.delete(0,'end')
                    ma_nam_e.delete(0,'end')
                    mp_nam_e.delete(0,'end')
                    mm_nam_e.delete(0,'end')
                
                # Modify button to make changes in the file
                bt21 = Button(newWindow2,text="Modify",command=ok,bg='orange',fg='white',font=('Arial',12,'bold')).place(x=110,y=360)#.grid(row=10,column=1,sticky=tkinter.N)
                
                # Clear button to clear all the values in the entry widget
                clr2 = Button(newWindow2,text="Clear",command=clear2,bg='orange',fg='white',height=1,width=5,font=('Arial',12,'bold')).place(x=445,y=360)#.grid(row=10,column=2,sticky=tkinter.N)

            # Displaying the error message if member not found type 1 and type 2
            else:
                # msg22 = Message(newWindow2,text="Error!!! Member not found",pady = 50).place(x=100,y=100)
                tkinter.messagebox.showerror("Error","Member not found")
        
        # Do nothing if the user enters blank values
        else:
            pass          
    
    # Label and entry to take the name to modify
    mnam = Label(newWindow2,text="Enter the name to modify :",font=('Arial',12,'bold')).place(x=110,y=50)#.grid(row=1,column=1,sticky=tkinter.EW)
    mnam_e = Entry(newWindow2,textvariable=modify_nam,font=('Arial',12,'bold'))
    mnam_e.place(x=320,y=50)#.grid(row=1,column=2,sticky=tkinter.EW)
    
    # Submit button check the name and display if it is present
    sub2 = Button(newWindow2,text="Submit",command=submit2,bg='blue',fg='white',height=1,width=5,font=('Arial',12,'bold')).place(x=110,y=90)#.grid(row=2,column=1,sticky=tkinter.N)
    
    # Exit button to exit from the page
    ex2 = Button(newWindow2,text="Exit",command=newWindow2.destroy,bg='red',fg='white',height=1,width=5,font=('Arial',12,'bold')).place(x=445,y=90)#.grid(row=2,column=2,sticky=tkinter.N)

# Search a member window/page
def openNewWindow3():
    
    # Creating a string variable to store the name to be searched
    search_nam = StringVar()
    
    # creating a page to search a member
    newWindow3 = Toplevel(top)
    newWindow3.title("Search a Member")
    newWindow3.geometry("700x500")
    newWindow3.resizable(width=False,height=False)
    
    # Clear the entry widget
    def clear3():
        snam_e.delete(0,'end')
    
    # To display the name and details asked 
    def submit3():
        # retriving the name 
        searching_name = search_nam.get()
        flag = 0
        searching_name = searching_name.lower()
        # checking if the string is not empty 
        if searching_name != '':
            
            # Logic to display the details 
            with open("book_ui.csv","r") as file:
                data_3 = file.readlines()
            for i in data_3:
                if i.startswith(searching_name):
                    searching_name1 = i.split(",")
                    if searching_name == searching_name1[0] :
                        searching_name1[0] = searching_name1[0].upper()
                        lb31 = Label(newWindow3,text="Name :",font=('Arial',12,'bold')).place(x=140,y=124)#.grid(row=6,column=1,sticky=tkinter.EW)
                        msg31 = Message(newWindow3,text=searching_name1[0],padx=5,pady=35,font=('Arial',12,'bold')).place(x=330,y=90)#.grid(row=6,column=2,sticky=tkinter.N)
                        lb32 = Label(newWindow3,text="Employee ID :",font=('Arial',12,'bold')).place(x=140,y=184)#.grid(row=8,column=1,sticky=tkinter.EW)
                        msg32 = Message(newWindow3,text=searching_name1[1],padx=5,pady=35,font=('Arial',12,'bold')).place(x=330,y=150)#.grid(row=8,column=2,sticky=tkinter.N)
                        lb33 = Label(newWindow3,text="Age :",font=('Arial',12,'bold')).place(x=140,y=244)#.grid(row=9,column=1,sticky=tkinter.EW)
                        msg33 = Message(newWindow3,text=searching_name1[2],padx=5,pady=35,font=('Arial',12,'bold')).place(x=330,y=210)#.grid(row=9,column=2,sticky=tkinter.N)
                        lb34 = Label(newWindow3,text="Phone Number :",font=('Arial',12,'bold')).place(x=140,y=304)#.grid(row=10,column=1,sticky=tkinter.EW)
                        msg34 = Message(newWindow3,text=searching_name1[3],padx=5,pady=35,font=('Arial',12,'bold')).place(x=330,y=270)#.grid(row=10,column=2,sticky=tkinter.N)
                        lb35 = Label(newWindow3,text="Email :",font=('Arial',12,'bold')).place(x=140,y=372)#.grid(row=11,column=1,sticky=tkinter.EW)
                        msg35 = Message(newWindow3,text=searching_name1[4],padx=5,pady=45,font=('Arial',12,'bold')).place(x=330,y=330)#.grid(row=11,column=2,sticky=tkinter.N)
                        # sub31 = Button(newWindow3,text="Ok",command=newWindow3.destroy,bg='red',fg='white',height=1,width=5).place(x=400,y=340)#.grid(row=11,column=2,sticky=tkinter.N)
                        flag = 1
                        break                
            
            # Display the error message if the name not present in the file type 1 and type 2
            if flag == 0:
                # msg32 = Message(newWindow3,text="Error!!! Person not found",pady = 50).place(x=50,y=50)
                tkinter.messagebox.showerror("ERROR","Member not found")
        # do nothing if the search entry widget is blank
        else:
            pass
    
    # Label and entry widget to search a member
    snam = Label(newWindow3,text="Enter the name to search :",font=('Arial',12,'bold')).place(x=140,y=20)#.grid(row=1,column=1,sticky=tkinter.EW)
    snam_e = Entry(newWindow3,textvariable=search_nam,font=('Arial',12,'bold'))
    snam_e.place(x=360,y=20)#.grid(row=1,column=2,sticky=tkinter.EW)
    
    # Submit , clear and exit button functions same as above
    sub3 = Button(newWindow3,text="Submit",command=submit3,bg='blue',fg='white',height=1,width=5,font=('Arial',12,'bold')).place(x=140,y=50)#.grid(row=3,column=1,sticky=tkinter.N)
    clr3 = Button(newWindow3,text="Clear",command=clear3,bg='orange',fg='white',height=1,width=5,font=('Arial',12,'bold')).place(x=315,y=50)#.grid(row=3,column=2,sticky=tkinter.N)
    ex3 = Button(newWindow3,text="Exit",command=newWindow3.destroy,bg='red',fg='white',height=1,width=5,font=('Arial',12,'bold')).place(x=485,y=50)#.grid(row=3,column=3,sticky=tkinter.N)

# delete a member    
def openNewWindow4():
    
    # variable to store the deleted name
    delete_nam = StringVar()
    
    # creating the delete page
    newWindow4 = Toplevel(top)
    newWindow4.title("Delete a Member")
    newWindow4.geometry("550x200")
    newWindow4.resizable(width=False,height=False)
    
    # clearing the entry widget
    def clear4():
        dnam_e.delete(0,'end')
    
    # deleting the name and its related details from the file
    def submit4():
        
        # retriving the name to be deleted
        deleting_name = delete_nam.get()
        deleting_name = deleting_name.lower()
        # checking if string is not empty
        if deleting_name != '':
            count4 = 0
            
            # Logic to delete the name and its respective details
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
            
            # Displaying the successfully deleted message type 1 and type 2
            if count4 == 1:
                #msg41 = Message(newWindow4,text="Successfully deleted",pady = 50).place(x=50,y=50)
                tkinter.messagebox.showinfo("Successfully deleted","Successfully deleted the Member")
                            
            # Displaying the error message if name is not present
            else:
                #msg41 = Message(newWindow4,text="Error!!! Member not found can not be deleted",pady = 100).place(x=50,y=50)
                tkinter.messagebox.showerror("ERROR","Member not found, can not be deleted")
        
        # do nothing if the string is blank
        else:
            pass
    
    # Label and entry widget to delete the name from user
    dnam = Label(newWindow4,text="Enter the name to delete :",font=('Arial',12,'bold')).place(x=50,y=35)#.grid(row=1,column=1,sticky=tkinter.EW)
    dnam_e = Entry(newWindow4,textvariable=delete_nam,font=('Arial',12,'bold'))
    dnam_e.place(x=250,y=35)#.grid(row=1,column=2,sticky=tkinter.EW)
    
    # submit, clear and exit buttons same as above 
    sub4 = Button(newWindow4,text="Submit",command=submit4,bg='blue',fg='white',height=1,width=5,font=('Arial',12,'bold')).place(x=50,y=95)#.grid(row=4,column=1,sticky=tkinter.N)
    clr4 = Button(newWindow4,text="Clear",command=clear4,bg='orange',fg='white',height=1,width=5,font=('Arial',12,'bold')).place(x=215,y=95)#.grid(row=4,column=2,sticky=tkinter.N)
    ex4 = Button(newWindow4,text="Exit",command=newWindow4.destroy,bg='red',fg='white',height=1,width=5,font=('Arial',12,'bold')).place(x=380,y=95)
    
# exit from the main page     
def onClick():
    res = tkinter.messagebox.askquestion('EXIT','Do you really want to exit')
    if res == 'yes' :
        top.destroy()
        
# display the members        
def openNewWindow5():
    
    # creating the page to display the members
    newWindow5 = Toplevel(top)
    newWindow5.title("Display Members")
    newWindow5.geometry("1130x500")
    newWindow5.minsize(1130,300)
    newWindow5.resizable(width=False,height=True)
    
    # logic to display the members
    lst = []
 
    with open("book_ui.csv","r") as f:
        data = f.readlines()
    for i in data:
        j = i.split(",")
        lst.append(j)

    total_rows = len(lst)
    total_columns = len(lst[0])
    
    for i in range(total_rows):
        for j in range(total_columns):
            
            if (i==0 and j==0) or (i==0 and j==1) or (i==0 and j==2) or (i==0 and j==3) or (i==0 and j==4):
                e = Entry(newWindow5, width=20, fg='black',font=('Arial',14,'bold'),justify=CENTER)
             
                e.grid(row=i, column=j)
                e.insert(END, lst[i][j])
            else:
                e = Entry(newWindow5, width=20, fg='black',font=('Arial',14))
             
                e.grid(row=i, column=j)
                e.insert(END,lst[i][j])

#l1 = Label(top,text="Select anyone option below",bg='yellow',bd=4).place(x=70,y=20)

# Buttons to do the actions as mentioned
b1 = Button(top,text="Add a New member",command = openNewWindow1,bg='orange',fg='white',height=2,width=15,font=('Arial',12,'bold')).place(x=170,y=30)
b2 = Button(top,text="Modify a member",command = openNewWindow2,bg='orange',fg='white',height=2,width=15,font=('Arial',12,'bold')).place(x=170,y=90)
b3 = Button(top,text="Search a member",command = openNewWindow3,bg='orange',fg='white',height=2,width=15,font=('Arial',12,'bold')).place(x=170,y=150)
b4 = Button(top,text="Delete a member",command = openNewWindow4,bg='orange',fg='white',height=2,width=15,font=('Arial',12,'bold')).place(x=170,y=210)
b4 = Button(top,text="Display members",command = openNewWindow5,bg='orange',fg='white',height=2,width=15,font=('Arial',12,'bold')).place(x=170,y=270)
b5 = Button(top,text="Exit",command = onClick,bg='red',fg='white',height=2,width=15,font=('Arial',12,'bold')).place(x=170,y=330)

# running the main page 
top.mainloop()

