
from tkinter import *

class HelpClass:
    def __init__(self, parentwindow):
        self.parentWindow      = parentwindow
        self.InitializeVariables()                
        return
        
    def InitializeVariables(self):
        self.aboutCallBackWindow = None
        return
    def aboutCallBackWindowOK(self):
        self.aboutCallBackWindow.destroy()
        self.aboutCallBackWindow = None
        return
    def AboutCallBack(self):
    
       if (self.aboutCallBackWindow == None):
           self.aboutCallBackWindow= Toplevel(self.parentWindow)
       else:
           return 
       self.aboutCallBackWindow.attributes('-topmost',True)
       self.aboutCallBackWindow.protocol("WM_DELETE_WINDOW", self.aboutCallBackWindowOK)                            
       self.aboutCallBackWindow.geometry("350x270")
       self.aboutCallBackWindow.resizable(False, False)
       self.aboutCallBackWindow.title("About")
    
       str1 ='Gas Chromatograph \n Peak works 2.0\n'
       str2 ='Copyright PID Analyzers \n' + \
          ' 2 Washington Circle, Unit 4 \n' + \
          ' Sandwich, MA 02563\n' + \
          ' All rights reserved\n\n\n'
    
       str3 = 'For information about this application contact:\n' + \
                       ' Phone:  1-774-413-5281\n' + \
                       ' Fax: 1-774-413-5298\n' + \
		               ' Sales Email: sales@hnu.com\n' + \
		               ' Service Email: bret@hnu.com\n' 
             
       string = str1 + str2 + str3 
       l2 = Label(self.aboutCallBackWindow, text = string)
       l2.pack(side=TOP)
       b2 = Button(self.aboutCallBackWindow, text = "OK",  
                    command = self.aboutCallBackWindowOK).pack(side=TOP)
    
       return