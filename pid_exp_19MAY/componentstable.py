#=====================================================================================    
#  Components Table Edit Pop Up Implementation
#  Top Menu Bar: Menu->Method->Components
#  Author : Girish S Kumar
#  Date 26-Nov-2021
#=====================================================================================    

from tkinter import *
import tkinter as tk
import json
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
from tkinter import ttk
import time
from tkinter import messagebox



import csv

class ComponentsTable:
    def __init__(self, parentwindow):
        self.parentWindow      = parentwindow
        self.InitializeVariables()
        return
#=====================================================================================           
        
    def CreateScrollWindowComponentsDetectorA(self,ParentWindow):
        frame=ParentWindow
        columns = ('component_name', 'on_off', 'peak_rt', 'window', 'resp_fact', 'low_alarm', 'high_alarm')
        self.ComponentsTableA = ttk.Treeview(frame, columns=columns, show='headings',height=5)
        frame.pack(side=TOP)

        # Create Headings
        self.ComponentsTableA.heading('component_name', text='Component Name')
        self.ComponentsTableA.column('component_name', minwidth=0, width=150, stretch=True)
        
        self.ComponentsTableA.heading('on_off', text='on/off')
        self.ComponentsTableA.column('on_off', minwidth=0, width=60,stretch=True)
        self.ComponentsTableA.heading('peak_rt', text='Peak RT')
        self.ComponentsTableA.column('peak_rt', minwidth=0, width=60,stretch=True)
        self.ComponentsTableA.heading('window', text='Window')
        self.ComponentsTableA.column('window', minwidth=0, width=80,stretch=True)
        self.ComponentsTableA.heading('resp_fact', text='Resp Fact')
        self.ComponentsTableA.column('resp_fact', minwidth=0, width=80,stretch=True)
        self.ComponentsTableA.heading('low_alarm', text='Low Alarm')
        self.ComponentsTableA.column('low_alarm', minwidth=0, width=70,stretch=True)
        self.ComponentsTableA.heading('high_alarm', text='High Alarm')
        self.ComponentsTableA.column('high_alarm', minwidth=0, width=70, stretch=True)
        self.ComponentsTableA.bind('<Double-1>', self.ItemSelectedInTableA)
        self.ComponentsTableA.bind('<<TreeviewSelect>>', self.ItemFocusedInTableA)
        self.ComponentsTableA.pack(side=LEFT)
      
        # Create scrollbar
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.ComponentsTableA.yview)
        self.ComponentsTableA.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=LEFT,fill='both', expand=1)
      
        # add data to the treeview
        for component in self.ComponentsTableAData:
           self.ComponentsTableA.insert('', tk.END, values=component)

        return
#=====================================================================================           
    def CreateScrollWindowComponentsDetectorB(self,ParentWindow):
        frame = ParentWindow
        style = ttk.Style(ParentWindow)
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="light grey", foreground="black")
        columns = ('component_name', 'on_off', 'peak_rt', 'window', 'resp_fact', 'low_alarm', 'high_alarm')
        self.ComponentsTableB = ttk.Treeview(frame, columns=columns, show='headings',height=5)
        
        frame.pack(side=TOP)

        # Create Heading 
        self.ComponentsTableB.heading('component_name', text='Component Name')
        self.ComponentsTableB.column('component_name', minwidth=0, width=150, stretch=True)
        
        self.ComponentsTableB.heading('on_off', text='on/off')
        self.ComponentsTableB.column('on_off', minwidth=0, width=60,stretch=True)
        
        self.ComponentsTableB.heading('peak_rt', text='Peak RT')
        self.ComponentsTableB.column('peak_rt', minwidth=0, width=60,stretch=True)
        
        self.ComponentsTableB.heading('window', text='Window')
        self.ComponentsTableB.column('window', minwidth=0, width=80,stretch=True)
        
        self.ComponentsTableB.heading('resp_fact', text='Resp Fact')
        self.ComponentsTableB.column('resp_fact', minwidth=0, width=80,stretch=True)
        
        self.ComponentsTableB.heading('low_alarm', text='Low Alarm')
        self.ComponentsTableB.column('low_alarm', minwidth=0, width=70,stretch=True)
        
        self.ComponentsTableB.heading('high_alarm', text='High Alarm')
        self.ComponentsTableB.column('high_alarm', minwidth=0, width=70, stretch=True)
        
        self.ComponentsTableB.bind('<Double-1>', self.ItemSelectedInTableB)
        
        self.ComponentsTableB.bind('<<TreeviewSelect>>', self.ItemFocusedInTableB)
     
        self.ComponentsTableB.pack(side=LEFT)
       

        #   Create scrollbar
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.ComponentsTableB.yview)
        self.ComponentsTableB.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=LEFT,fill='both', expand=1)
        
        for component in self.ComponentsTableBData:
           self.ComponentsTableB.insert('', tk.END, values=component)
        return
#=====================================================================================
    def ItemFocusedInTableA(self,event):
        # If and Item in selected in Table B deselect it
        # We allow only selection of one item 
        # This is to support the edit button    
        
        #print("ItemFocusedInTableA")
        if len(self.ComponentsTableB.selection()) > 0:
               self.ComponentsTableB.selection_remove(self.ComponentsTableB.selection()[0])
               #print("ComponentsTableB DeSelected")    
        return
#=====================================================================================
    def ItemFocusedInTableB(self,event):
        # If and Item in selected in Table B deselect it
        # We allow only selection of one item 
        # This is to support the edit button    
        
        #print("ItemFocusedInTableB")
        if len(self.ComponentsTableA.selection()) > 0:
               self.ComponentsTableA.selection_remove(self.ComponentsTableA.selection()[0])      
               #print("ComponentsTableA DeSelected")    
        return        
#=====================================================================================              
    def ItemSelectedInTableAOKCallBack(self):
        idx = int(self.TableA_selected_item.removeprefix("I"))
        #print(self.TableA_selected_item)
        #print("Selected index = ", idx)        
        self.recordA[0]=self.TableA_componentName.get()   
        flag =  self.TableA_on_off.get()    
        if (flag == True):
           self.recordA[1]="Yes"
        else:
           self.record[1]="No"
        
        self.recordA[2]=float(self.TableA_peakRT.get())
        self.recordA[3]=float(self.TableA_window.get())
        self.recordA[4]=float(self.TableA_respFactor.get())
        self.recordA[5]=float(self.TableA_lowAlarm.get())
        self.recordA[6]=float(self.TableA_highAlarm.get())
        
        # Make Copy of the original Components List
        self.ComponentsTemporaryTableAData = list(self.ComponentsTableAData)
        
        # Make All the changes in temporary List
        # So that later when the final OK button in the main panel is pressed
        # The contents of ComponentsTemporaryTableAData will be copied to
        # to Orinal ComponentsTableAData
        
        self.ComponentsTableA.item(self.TableA_selected_item, values=self.recordA)
        
        self.ComponentsTemporaryTableAData.pop(idx-1)
        
        self.ComponentsTemporaryTableAData.insert(idx-1,self.recordA)
        
        self.ComponentsTemporaryTableADataChangedFlag = True
        
        self.edit_popUpA.destroy()
        
        self.edit_popUpA = None
        
        return
        
#=====================================================================================                   
    def ItemSelectedInTableACancelCallBack(self):
        self.edit_popUpA.destroy()
        self.edit_popUpA = None
        return
        
#=====================================================================================                   
    def ItemSelectedInTableAHelpCallBack(self):
    
        return
#=====================================================================================       
    def ItemSelectedInTableBOKCallBack(self):
        
        idx = int(self.TableB_selected_item.removeprefix("I"))
        
        self.recordB[0]=self.TableB_componentName.get()   
        
        flag =  self.TableB_on_off.get()    
        
        if (flag == True):
           self.recordB[1]="Yes"
        else:
           self.recordB[1]="No"
        
        self.recordB[2]=float(self.TableB_peakRT.get())
        self.recordB[3]=float(self.TableB_window.get())
        self.recordB[4]=float(self.p.get())
        self.recordB[5]=float(self.TableB_lowAlarm.get())
        self.recordB[6]=float(self.TableB_highAlarm.get())
        
        self.ComponentsTableB.item(self.TableB_selected_item, values=self.recordB)
        
        # Make Copy of the original Components List
        self.ComponentsTemporaryTableBData = list(self.ComponentsTableBData)
        
        # Make All the changes in temporary List
        # So that later when the final OK button in the main panel is pressed
        # The contents of ComponentsTemporaryTableAData will be copied to
        # to Orinal ComponentsTableAData
        
        self.ComponentsTemporaryTableBData.pop(idx-1)
        
        self.ComponentsTemporaryTableBData.insert(idx-1,self.recordB)
        
        self.ComponentsTemporaryTableBDataChangedFlag = True
        
        self.edit_popUpB.destroy()
        self.edit_popUpB = None
        return
        
#=====================================================================================                   
    def ItemSelectedInTableBCancelCallBack(self):
        self.edit_popUpB.destroy()
        self.edit_popUpB = None
        return
        
#=====================================================================================                           
    def edit_popUpBXPressed(self):
        self.ItemSelectedInTableBCancelCallBack()
        return

#=====================================================================================                   
        
    def edit_popUpAXPressed(self):
        self.ItemSelectedInTableACancelCallBack()
        return        
#=====================================================================================            
    def ItemSelectedInTableBHelpCallBack(self):
    
        return
#=====================================================================================           
    def EditSelectedItemInTableA(self):
        for self.TableA_selected_item in self.ComponentsTableA.selection():
        
            if (self.edit_popUpA == None):
                self.edit_popUpA = Toplevel(self.popUpWindow)
            else:
                return
                
            TableA_item = self.ComponentsTableA.item(self.TableA_selected_item)
           
            self.recordA = TableA_item['values']
                       
 
                
            self.edit_popUpA.attributes('-topmost',True)
            self.edit_popUpA.resizable(False, False)
            self.edit_popUpA.protocol("WM_DELETE_WINDOW", self.edit_popUpAXPressed)                                
            frame1 = Frame(self.edit_popUpA,borderwidth=4,relief=FLAT)
            self.TableA_componentName=StringVar()
            self.TableA_componentName.set(self.recordA[0])
            Label(frame1, text='Name').pack(side=LEFT)
            entry= Entry(frame1,relief=SUNKEN, textvariable=self.TableA_componentName,
                                            width= 30).pack(side=LEFT)
            frame1.pack(side=TOP)            
            
            frame2 = Frame(self.edit_popUpA,borderwidth=4,relief=FLAT)
            self.TableA_peakRT =StringVar()
            self.TableA_peakRT.set(str(self.recordA[2]))
            Label(frame2, text='Peak RT').pack(side=LEFT,anchor=W)
            entry= Entry(frame2,relief=SUNKEN, textvariable=self.TableA_peakRT,
                                            width= 6).pack(side=LEFT,anchor=W,padx=4)            
                                            
            self.TableA_lowAlarm = StringVar()
            self.TableA_lowAlarm.set(str(self.recordA[5]))
            Label(frame2, text='Low Alarm').pack(side=LEFT,anchor=E)
            entry= Entry(frame2,relief=SUNKEN, textvariable=self.TableA_lowAlarm,
                                            width= 6).pack(side=LEFT, anchor=E)            
                                            
            frame2.pack(side=TOP)
            
            frame3 = Frame(self.edit_popUpA,borderwidth=4,relief=FLAT)                                
            self.TableA_window = StringVar()
            self.TableA_window.set(str(self.recordA[3]))
            Label(frame3, text='Window').pack(side=LEFT)
            entry= Entry(frame3,relief=SUNKEN, textvariable=self.TableA_window,
                                            width= 6).pack(side=LEFT)            
                                            
            self.TableA_highAlarm = StringVar()
            self.TableA_highAlarm.set(str(self.recordA[6]))
            Label(frame3, text='High Alarm').pack(side=LEFT)
            entry= Entry(frame3,relief=SUNKEN, textvariable=self.TableA_highAlarm,
                                            width= 6).pack(side=LEFT)            
            frame3.pack(side=TOP)
            
            
            frame4 = Frame(self.edit_popUpA,borderwidth=4,relief=FLAT)
            self.TableA_respFactor = StringVar()
            self.TableA_respFactor.set(str(self.recordA[4]))
            Label(frame4, text='Resp Factor').pack(side=LEFT)
            entry= Entry(frame4,relief=SUNKEN, textvariable=self.TableA_respFactor,
                                            width= 6).pack(side=LEFT)            
            self.TableA_on_off = BooleanVar()
            
            if self.recordA[1] == 'Yes':
                self.TableA_on_off.set(True)
            else:
                self.TableA_on_off.set(False)
                
            Checkbutton(frame4, variable=self.TableA_on_off,text='ON/OFF').pack(side=LEFT,ipadx=17)
            frame4.pack(side=TOP)
                        
            ButtonFrame = Frame(self.edit_popUpA,borderwidth=4,relief=FLAT)
            Button(ButtonFrame, text ="  OK  ", command = self.ItemSelectedInTableAOKCallBack).pack(side=LEFT,ipadx=4)
            Button(ButtonFrame, text ="Cancel", command=  self.ItemSelectedInTableACancelCallBack).pack(side=LEFT)
            Button(ButtonFrame, text =" Help ", command = self.ItemSelectedInTableAHelpCallBack).pack(side=LEFT,ipadx=4)
            ButtonFrame.pack(side=TOP)    
        return   
#=====================================================================================           
    def EditSelectedItemInTableB(self):
        for self.TableB_selected_item in self.ComponentsTableB.selection():
        
            if (self.edit_popUpB == None):
                self.edit_popUpB = Toplevel(self.popUpWindow)
            else:
                return
            
            TableB_item = self.ComponentsTableB.item(self.TableB_selected_item)
            self.recordB=[]
            self.recordB = TableB_item['values']
            
                
            self.edit_popUpB.attributes('-topmost',True)
            self.edit_popUpB.protocol("WM_DELETE_WINDOW", self.edit_popUpBXPressed)                                            
            self.edit_popUpB.resizable(False, False)
            frame1 = Frame(self.edit_popUpB,borderwidth=4,relief=FLAT)
            self.TableB_componentName=StringVar()
            self.TableB_componentName.set(self.recordB[0])
            Label(frame1, text='Name').pack(side=LEFT)
            entry= Entry(frame1,relief=SUNKEN, textvariable=self.TableB_componentName,
                                            width= 30).pack(side=LEFT)
            frame1.pack(side=TOP)            
            
            frame2 = Frame(self.edit_popUpB,borderwidth=4,relief=FLAT)
            self.TableB_peakRT =StringVar()
            self.TableB_peakRT.set(str(self.recordB[2]))
            Label(frame2, text='Peak RT').pack(side=LEFT,anchor=W)
            entry= Entry(frame2,relief=SUNKEN, textvariable=self.TableB_peakRT,
                                            width= 6).pack(side=LEFT,anchor=W,padx=4)            
                                            
            self.TableB_lowAlarm = StringVar()
            self.TableB_lowAlarm.set(str(self.recordB[5]))
            Label(frame2, text='Low Alarm').pack(side=LEFT,anchor=E)
            entry= Entry(frame2,relief=SUNKEN, textvariable=self.TableB_lowAlarm,
                                            width= 6).pack(side=LEFT, anchor=E)            
                                            
            frame2.pack(side=TOP)
            
            
            frame3 = Frame(self.edit_popUpB,borderwidth=4,relief=FLAT)                                
            self.TableB_window = StringVar()
            self.TableB_window.set(str(self.recordB[3]))
            Label(frame3, text='Window').pack(side=LEFT)
            entry= Entry(frame3,relief=SUNKEN, textvariable=self.TableB_window,
                                            width= 6).pack(side=LEFT)            
                                            
            self.TableB_highAlarm = StringVar()
            self.TableB_highAlarm.set(str(self.recordB[6]))
            Label(frame3, text='High Alarm').pack(side=LEFT)
            entry= Entry(frame3,relief=SUNKEN, textvariable=self.TableB_highAlarm,
                                            width= 6).pack(side=LEFT)            
            frame3.pack(side=TOP)
            
            
            frame4 = Frame(self.edit_popUpB,borderwidth=4,relief=FLAT)
            self.TableB_respFactor = StringVar()
            self.TableB_respFactor.set(str(self.recordB[4]))
            Label(frame4, text='Resp Factor').pack(side=LEFT)
            entry= Entry(frame4,relief=SUNKEN, textvariable=self.TableB_respFactor,
                                            width= 6).pack(side=LEFT)            
            self.TableB_on_off = BooleanVar()
            
            if self.recordB[1] == 'Yes':
                self.TableB_on_off.set(True)
            else:
                self.TableB_on_off.set(False)
                
            Checkbutton(frame4, variable=self.TableB_on_off,text='ON/OFF').pack(side=LEFT,ipadx=17)
            frame4.pack(side=TOP)
              
            ButtonFrame = Frame(self.edit_popUpB,borderwidth=4,relief=FLAT)
            Button(ButtonFrame, text ="  OK  ", command = self.ItemSelectedInTableBOKCallBack).pack(side=LEFT,ipadx=4)
            Button(ButtonFrame, text ="Cancel", command=  self.ItemSelectedInTableBCancelCallBack).pack(side=LEFT)
            Button(ButtonFrame, text =" Help ", command = self.ItemSelectedInTableBHelpCallBack).pack(side=LEFT,ipadx=4)
            ButtonFrame.pack(side=TOP)
        return
#=====================================================================================                   
    def ItemSelectedInTableA(self,event):
        self.EditSelectedItemInTableA()
        return
#=====================================================================================                       
    def ItemSelectedInTableB(self,event):        
        self.EditSelectedItemInTableB()    
        return
#=====================================================================================                       
    def ComponentsTableOKCallBack(self):
    
        if (self.ComponentsTemporaryTableADataChangedFlag == True):
           self.ComponentsTableAData = list(self.ComponentsTemporaryTableAData)
           self.ComponentsTemporaryTableADataChangedFlag = False 
           
        if (self.ComponentsTemporaryTableBDataChangedFlag == True):   
           self.ComponentsTableBData =  list(self.ComponentsTemporaryTableBData)
           self.ComponentsTemporaryTableBDataChangedFlag = False     
        self.popUpWindow.destroy()
        self.popUpWindow = None
        return
#=====================================================================================               
    def ComponentsTableEditCallBack(self):
        # We will not allow selection to rows in both table
        # Either only one can be selected 
        # Need to find out which one user has selected
        # Based on number of selection in each table
        flag=False
        #print("Entry:ComponentsTableEditCallBack")
        if len(self.ComponentsTableA.selection()) > 0:
           #print("Selection is in Table A")
           flag=True
           self.EditSelectedItemInTableA()
            
        if len(self.ComponentsTableB.selection()) > 0:
           #print("Selection is in Table B")
           flag=True
           self.EditSelectedItemInTableB() 
        if (flag==False):
            showinfo(title='Information', message='Select a row from the table')           
        #print("Exit:ComponentsTableEditCallBack ")
        return
#=====================================================================================                   
    def ComponentsTableCancelCallBack(self):
        self.popUpWindow.destroy()
        self.popUpWindow = None
        return
#=====================================================================================                           
    def popUpWindowXPressed(self):
        self.ComponentsTableCancelCallBack()
        return
#=====================================================================================                   
    def ComponentsTableHelpCallBack(self):
        return
#=====================================================================================                   
    def InitializeVariables(self):
        self.edit_popUpA          = None
        self.popUpWindow          = None
        self.edit_popUpB          = None
        self.ComponentsTableAData = self.ReadCSV("ComponentA.csv")
        self.ComponentsTableBData = self.ReadCSV("ComponentB.csv")  
        self.ComponentsTemporaryTableAData = []
        self.ComponentsTemporaryTableBData = []
        self.ComponentsTemporaryTableADataChangedFlag = False
        self.ComponentsTemporaryTableBDataChangedFlag = False
        return
#=====================================================================================                   
    def TablePopUp(self):
        if (self.popUpWindow == None):
            self.popUpWindow= Toplevel(self.parentWindow)
        else:
            return
            
        self.popUpWindow.geometry('600x400')
        self.popUpWindow.title('Methods Components')
        self.popUpWindow.protocol("WM_DELETE_WINDOW", self.popUpWindowXPressed)                                        
        self.popUpWindow.attributes('-topmost',True)
        self.popUpWindow.resizable(False, False)
        
        frameA = LabelFrame(self.popUpWindow,text="Component Table Detector A")
        self.CreateScrollWindowComponentsDetectorA(frameA)

        frameB = LabelFrame(self.popUpWindow,text="Component Table Detector B")
        self.CreateScrollWindowComponentsDetectorB(frameB)

        ButtonFrame = Frame(self.popUpWindow,borderwidth=4,relief=FLAT)

        frameA.pack(side=TOP,anchor=W,padx=4, pady=10)
        frameB.pack(side=TOP,anchor=W,padx=4, pady=10)

        Button(ButtonFrame, text ="  OK  ", command  =  self.ComponentsTableOKCallBack).pack(side=LEFT,padx=5)
        Button(ButtonFrame, text ="Cancel", command  =  self.ComponentsTableCancelCallBack).pack(side=LEFT,padx=5)
        Button(ButtonFrame, text ="Edit  ", command  =  self.ComponentsTableEditCallBack).pack(side=LEFT,padx=5)
        Button(ButtonFrame, text =" Help ", command  =  self.ComponentsTableHelpCallBack).pack(side=LEFT,ipadx=5)
        ButtonFrame.pack(side=TOP,anchor=W,padx=100)
        return
#=====================================================================================                   
    def ReadCSV(self,csvName):
        # initializing the titles and rows list
        fields = []
        rows = []
        # reading csv file
        with open(csvName, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)
            
            # extracting field names through first row
            fields = next(csvreader)

            # extracting each data row one by one
            for row in csvreader:
                rows.append(row)

            # get total number of rows
            #print("Total no. of rows: %d"%(csvreader.line_num))
            return rows
#=====================================================================================                 