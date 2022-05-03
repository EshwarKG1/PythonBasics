#=====================================================================================    
#  Standards Table Edit Pop Up Implementation
#  Top Menu Bar: Menu->Method->Standards
#  Author : Girish S Kumar
#  Date 26-Nov-2021
#=====================================================================================    

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import csv

class StandardsTable:
    def __init__(self, parentwindow):
        self.parentWindow      = parentwindow
        self.InitializeVariables()
        return
#=====================================================================================           
        
    def CreateScrollWindowStandardsDetectorA(self,ParentWindow):
        frame=ParentWindow
        columns = ('component_name', 'rel', 'resp_factor', 'stand0', 'stand1', 'stand2', 'stand3')
        self.ComponentsTableA = ttk.Treeview(frame, columns=columns, show='headings',height=5)
        frame.pack(side=TOP)

        # Create Headings
        self.ComponentsTableA.heading('component_name', text='Component Name')
        self.ComponentsTableA.column('component_name', minwidth=0, width=150, stretch=True)
        
        self.ComponentsTableA.heading('rel', text='Rel')
        self.ComponentsTableA.column('rel', minwidth=0, width=60,stretch=True)
        self.ComponentsTableA.heading('resp_factor', text='Resp Factor')
        self.ComponentsTableA.column('resp_factor', minwidth=0, width=60,stretch=True)
        self.ComponentsTableA.heading('stand0', text='Stand 0')
        self.ComponentsTableA.column('stand0', minwidth=0, width=80,stretch=True)
        self.ComponentsTableA.heading('stand1', text='Stand 1')
        self.ComponentsTableA.column('stand1', minwidth=0, width=80,stretch=True)
        self.ComponentsTableA.heading('stand2', text='Stand 2')
        self.ComponentsTableA.column('stand2', minwidth=0, width=70,stretch=True)
        self.ComponentsTableA.heading('stand3', text='Stand 3')
        self.ComponentsTableA.column('stand3', minwidth=0, width=70, stretch=True)
        self.ComponentsTableA.bind('<Double-1>', self.ItemSelectedInTableA)
        self.ComponentsTableA.bind('<<TreeviewSelect>>', self.ItemFocusedInTableA)
        self.ComponentsTableA.pack(side=LEFT)
      
        # Create scrollbar
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.ComponentsTableA.yview)
        self.ComponentsTableA.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=LEFT,fill='both', expand=1)
      
        # add data to the treeview
        for component in self.StandardsTableAData:
           self.ComponentsTableA.insert('', tk.END, values=component)

        return
#=====================================================================================           
    def CreateScrollWindowStandardsDetectorB(self,ParentWindow):
        frame = ParentWindow
        style = ttk.Style(ParentWindow)
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="light grey", foreground="black")
        columns = ('component_name', 'rel', 'resp_factor', 'stand0', 'stand1', 'stand2', 'stand3')
        self.ComponentsTableB = ttk.Treeview(frame, columns=columns, show='headings',height=5)
        
        frame.pack(side=TOP)

        # Create Heading 
        self.ComponentsTableB.heading('component_name', text='Component Name')
        self.ComponentsTableB.column('component_name', minwidth=0, width=150, stretch=True)
        
        self.ComponentsTableB.heading('rel', text='Rel')
        self.ComponentsTableB.column('rel', minwidth=0, width=60,stretch=True)
        
        self.ComponentsTableB.heading('resp_factor', text='Resp Factor')
        self.ComponentsTableB.column('resp_factor', minwidth=0, width=60,stretch=True)
        
        self.ComponentsTableB.heading('stand0', text='Stand 0')
        self.ComponentsTableB.column('stand0', minwidth=0, width=80,stretch=True)
        
        self.ComponentsTableB.heading('stand1', text='Stand 1')
        self.ComponentsTableB.column('stand1', minwidth=0, width=80,stretch=True)
        
        self.ComponentsTableB.heading('stand2', text='Stand 2')
        self.ComponentsTableB.column('stand2', minwidth=0, width=70,stretch=True)
        
        self.ComponentsTableB.heading('stand3', text='Stand 3')
        self.ComponentsTableB.column('stand3', minwidth=0, width=70, stretch=True)
        
        self.ComponentsTableB.bind('<Double-1>', self.ItemSelectedInTableB)
        
        self.ComponentsTableB.bind('<<TreeviewSelect>>', self.ItemFocusedInTableB)
     
        self.ComponentsTableB.pack(side=LEFT)
       

        #   Create scrollbar
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.ComponentsTableB.yview)
        self.ComponentsTableB.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=LEFT,fill='both', expand=1)
        
        for component in self.StandardsTableBData:
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
        self.StandardsTemporaryTableAData = list(self.StandardsTableAData)
        
        # Make All the changes in temporary List
        # So that later when the final OK button in the main panel is pressed
        # The contents of StandardsTemporaryTableAData will be copied to
        # to Orinal StandardsTableAData
        
        self.ComponentsTableA.item(self.TableA_selected_item, values=self.recordA)
        
        self.StandardsTemporaryTableAData.pop(idx-1)
        
        self.StandardsTemporaryTableAData.insert(idx-1,self.recordA)
        
        self.StandardsTemporaryTableADataChangedFlag = True
        
        self.edit_popUpA.destroy()
        
        self.edit_popUpA = None
        
        return
        
#=====================================================================================                   
    def ItemSelectedInTableACancelCallBack(self):
        self.edit_popUpA.destroy()
        self.edit_popUpA = None
        return
    def edit_popUpAXPressed(self):
        self.ItemSelectedInTableACancelCallBack()    
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
        self.recordB[4]=float(self.TableB_respFactor.get())
        self.recordB[5]=float(self.TableB_lowAlarm.get())
        self.recordB[6]=float(self.TableB_highAlarm.get())
        
        self.ComponentsTableB.item(self.TableB_selected_item, values=self.recordB)
        
        # Make Copy of the original Components List
        self.StandardsTemporaryTableBData = list(self.StandardsTableBData)
        
        # Make All the changes in temporary List
        # So that later when the final OK button in the main panel is pressed
        # The contents of StandardsTemporaryTableAData will be copied to
        # to Orinal StandardsTableBData
        
        self.StandardsTemporaryTableBData.pop(idx-1)
        
        self.StandardsTemporaryTableBData.insert(idx-1,self.recordB)
        
        self.StandardsTemporaryTableBDataChangedFlag = True
        
        self.edit_popUpB.destroy()
        
        self.edit_popUpB = None
        
        return
        
#=====================================================================================                   
    def ItemSelectedInTableBCancelCallBack(self):
        self.edit_popUpB.destroy()
        self.edit_popUpB = None
        return
    def edit_popUpBXPressed(self):
        self.ItemSelectedInTableBCancelCallBack()    
        return
#=====================================================================================            
    def ItemSelectedInTableBHelpCallBack(self):
    
        return
#=====================================================================================           
    def EditSelectedItemInTableA(self):
        for self.TableA_selected_item in self.ComponentsTableA.selection():
            #print(self.TableA_selected_item)
            TableA_item = self.ComponentsTableA.item(self.TableA_selected_item)
            #print(TableA_item)
            self.recordA = TableA_item['values']
            #print("Data to be poped up Table-A")
            #print(self.recordA)
            if (self.edit_popUpA == None):
               self.edit_popUpA = Toplevel(self.popUpWindow)
            else:
               self.edit_popUpA = None 
               
            self.edit_popUpA.attributes('-topmost',True)
            self.edit_popUpA.protocol("WM_DELETE_WINDOW", self.edit_popUpAXPressed)                                            
            self.edit_popUpA.resizable(False, False)
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
            
            TableB_item = self.ComponentsTableB.item(self.TableB_selected_item)
            self.recordB=[]
            self.recordB = TableB_item['values']
            
            if (self.edit_popUpB == None):
                self.edit_popUpB = Toplevel(self.popUpWindow)
            else:
                self.edit_popUpB = None
                
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
    def StandardsTableOKCallBack(self):
        if (self.StandardsTemporaryTableADataChangedFlag == True):
           self.StandardsTableAData = list(self.StandardsTemporaryTableAData)
           self.StandardsTemporaryTableADataChangedFlag = False 
           
        if (self.StandardsTemporaryTableBDataChangedFlag == True):   
           self.StandardsTableBData =  list(self.StandardsTemporaryTableBData)
           self.StandardsTemporaryTableBDataChangedFlag = False
           
        self.popUpWindow.destroy()
        self.popUpWindow = None
        return
#=====================================================================================               
    def StandardsTableEditCallBack(self):
        # We will not allow selection to rows in both table
        # Either only one can be selected 
        # Need to find out which one user has selected
        # Based on number of selection in each table
        flag=False
        #print("Entry:StandardsTableEditCallBack")
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
        #print("Exit:StandardTableEditCallBack ")
        return
#=====================================================================================                   
    def StandardsTableCancelCallBack(self):
        self.popUpWindow.destroy()
        self.popUpWindow = None 
        return
    def popUpWindowXPressed(self):
        self.StandardsTableCancelCallBack()
        return
#=====================================================================================                   
    def StandardsTableHelpCallBack(self):
        return
#=====================================================================================                   
    def InitializeVariables(self):
        self.StandardsTableAData = self.ReadCSV("StandardsA.csv")
        self.StandardsTableBData = self.ReadCSV("StandardsB.csv")   
        self.StandardsTemporaryTableAData = []
        self.StandardsTemporaryTableBData = []
        self.StandardsTemporaryTableADataChangedFlag = False
        self.StandardsTemporaryTableBDataChangedFlag = False
        self.popUpWindow  = None
        self.edit_popUpA  = None
        self.edit_popUpB  = None
        
        return
#=====================================================================================                   
    def TablePopUp(self):
        if (self.popUpWindow == None):
            self.popUpWindow= Toplevel(self.parentWindow)
        else:
            return 
        self.popUpWindow.attributes('-topmost',True)
        self.popUpWindow.protocol("WM_DELETE_WINDOW", self.popUpWindowXPressed)                                                
        self.popUpWindow.geometry('600x400')
        self.popUpWindow.resizable(False, False)
        self.popUpWindow.title('Methods Standards')
        frameA = LabelFrame(self.popUpWindow,text="Component Table Detector A")
        self.CreateScrollWindowStandardsDetectorA(frameA)

        frameB = LabelFrame(self.popUpWindow,text="Component Table Detector B")
        self.CreateScrollWindowStandardsDetectorB(frameB)

        ButtonFrame = Frame(self.popUpWindow,borderwidth=4,relief=FLAT)

        frameA.pack(side=TOP,anchor=W,padx=4, pady=10)
        frameB.pack(side=TOP,anchor=W,padx=4, pady=10)

        Button(ButtonFrame, text ="  OK  ", command  =  self.StandardsTableOKCallBack).pack(side=LEFT,padx=5)
        Button(ButtonFrame, text ="Cancel", command  =  self.StandardsTableCancelCallBack).pack(side=LEFT,padx=5)
        Button(ButtonFrame, text ="Edit  ", command  =  self.StandardsTableEditCallBack).pack(side=LEFT,padx=5)
        Button(ButtonFrame, text =" Help ", command  =  self.StandardsTableHelpCallBack).pack(side=LEFT,ipadx=5)
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