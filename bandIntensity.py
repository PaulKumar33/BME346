import tkinter
from pathlib import Path

class bandIntensity:
    """this class take a txt file input and calculates the values
    band intensity and outputs the values"""
    global nArray
    global mean
    global array
    
    array = []
    nArray = []  
    
    def tryText(self, text):
        try_file = Path(text)
        if try_file.is_file():
            return True
        else:
            return False
        
    def readText(self, text): 
        with open(text, 'r') as file:
            tArray = []
            data = file.read().split('\n')
            for element in data: 
                print(element)
                tArray.extend(element.split())
            #elements occur at 2, 7, 12, 17.... (2 + n5) is the index of intrest
            for elm in range(len(tArray)):
                if((elm-1)%5 == 0 or elm == 1):
                    array.extend(tArray[elm].split())
            
            array.remove('mean')
                
        
        
    def getIntensity(self):        
        #create a new array, add zero elements until
        #it reaches the size of the input
        n = len(array)
        #print(n)
        for i in range(n):
            data = 255 - float(array[i])
            nArray.append(data)
            
        print('your intensity array: ', nArray)
        
    def addBackground(self):
        ##changes the nArray by the value of the background intensity
        ##setting the gui object
        print('what is the background intensity?: ')
        background = float(input())
        n = len(array)
        for i in range(n):
            nArray[i] = nArray[i] - background
        return nArray
        
    
    def getMeanIntensity(self):
        sum = 0
        n = len(array)
        print(n)
        for i in range(n):
            sum += nArray[i] 
            
        global mean 
        mean = sum/n
        return mean
    
    def outputValue(self):
        print("Average intensity: {}".format(mean))
        print("The Values of the mean intensity array: ", nArray)
        
        
'''note now i want to add functionallity that can read different columns of data so there should be no processing'''

class getDocument:
    
    global destination
    
    def getFile(self):
        print('please enter the file desintination')
        destination = (input())
        return destination
       
    def process(self, string):
        #thisfunction is essential as it changes the file destination to one which python can read
        s = string
        new_str = s.replace('\\', '/')
        print(new_str)
        return new_str

class gui(tkinter.Tk):
    
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        
    def initializeGUI(self):
        ##this method contains all gui elements
        global pathVar
        self.grid()
        
        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self, textvariable = self.entryVariable)
        #for some reason i must include EW
        #this is simply positioning
        #note column span is a measure of how many active columns the widget spans
        #ie if we had thre columns active and i chose to span 2 columns, it would leave one blank
        self.entry.grid(column = 0, row = 0, columnspan = 1,sticky = 'EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        #self.entryVariable.set(u"enter file destination here: ")
        
        
        ##adds a button object to the window
        ##adding add button click adds event listener
        button = tkinter.Button(self, text=u"Clik here", command = self.OnButtonClick)
        button.grid(column=1, row=0)
        
        #binding to the label widget
        self.labelVariable = tkinter.StringVar()
        self.arrayLabelVar = tkinter.StringVar()
        self.meanLabelVar = tkinter.StringVar()
        #ensures the label is set
        label = tkinter.Label(self, textvariable = self.labelVariable, anchor="w", fg = "white", bg = "blue")
        label.grid(column = 0, row = 1, columnspan = 2, sticky="EW")
        ArrayLabel = tkinter.Label(self, textvariable = self.arrayLabelVar, anchor='w', fg = 'white', bg = 'blue')
        ArrayLabel.grid(column = 0, row = 2, columnspan = 2, sticky = "EW")
        MeanLabel = tkinter.Label(self, textvariable = self.meanLabelVar, anchor ='w', fg = 'white', bg = 'blue')
        MeanLabel.grid(column = 0, row = 3, columnspan = 2, sticky = 'EW')
        self.labelVariable.set(u"Enter the file destination above")
        self.arrayLabelVar.set(u"mean array: empty")
        self.meanLabelVar.set(u"currently no sample mean")
        
        self.grid_columnconfigure(0, weight = 1)        
        ##resizes horizontally but not vertically
        ##first entry is bool for horiz and second is vertical
        self.resizable(True, False)
        self.update()
        self.geometry(self.geometry())
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)     
        
    def OnButtonClick(self):
        pathVar = str(self.entryVariable.get())
        print(self.entryVariable.get())
        self.labelVariable.set(self.entryVariable.get())
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)    
        
    def OnPressEnter(self, event):
        pathVar = 'null'
        gDoc = getDocument()
        bInt = bandIntensity()
        
        pathVar = self.entryVariable.get()
        print(self.entryVariable.get())
        self.labelVariable.set(self.entryVariable.get())
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)
        
        if(pathVar != 'null' or ''):
            parse = gDoc.process(pathVar)
            if(bInt.tryText(parse)):
                bInt.readText(parse)
                self.proccessData()
            else:
                print("this isnt a valid file location")
                self.labelVariable.set("this is not a valid path")
    
    def proccessData(self):
        bI = bandIntensity()
        bI.getIntensity()
        mArray = bI.addBackground()
        total_mean = bI.getMeanIntensity()
        self.outsideInit(mArray, total_mean)
        bI.outputValue()
        
    def outsideInit(self,MeanVar, MeanTot):
        #i didnt end up changing functionality to change the path display because this wouldnt be
        #acessed if i could not
        self.arrayLabelVar.set(MeanVar)
        self.meanLabelVar.set(MeanTot)      
        
class main:
    global pVar
    '''Calls the gui class'''
    guiMain = gui(None)
    guiMain.initializeGUI()        
    guiMain.mainloop()
    
    
    
    
    
    