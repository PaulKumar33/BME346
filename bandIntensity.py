import tkinter


class bandIntensity:
    """this class take a txt file input and calculates the values
    band intensity and outputs the values"""
    global nArray
    global mean
    global array
    
    array = []
    nArray = []    
    
    
        
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
        print('what is the background intensity?: ')
        background = float(input())
        n = len(array)
        for i in range(n):
            nArray[i] = nArray[i] - background
    
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
        self.grid()
        
        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self, textvariable = self.entryVariable)
        #for some reason i must include EW
        #this is simply positioning
        self.entry.grid(column = 0, row = 0, sticky = 'EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        #self.entryVariable.set(u"enter text here: ")
        
        
        ##adds a button object to the window
        ##adding add button click adds event listener
        button = tkinter.Button(self, text=u"Clik here", command = self.OnButtonClick)
        button.grid(column=1, row=0)
        
        #binding to the label widget
        self.labelVariable = tkinter.StringVar()
        #ensures the label is set
        label = tkinter.Label(self, textvariable = self.labelVariable, anchor="w", fg = "white", bg = "blue")
        label.grid(column = 0, row = 1, columnspan = 2, sticky="EW")
        self.labelVariable.set(u"hello !")
        
        self.grid_columnconfigure(0, weight = 1)        
        ##resizes horizontally but not vertically
        ##first entry is bool for horiz and second is vertical
        self.resizable(True, False)
        self.update()
        self.geometry(self.geometry())
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)
        
        
        
    def OnButtonClick(self): 
        #self.entryVariable.set("")
        print(self.entryVariable)
        self.labelVariable.set(self.entryVariable.get())
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)        
        
    def OnPressEnter(self, event):
        #self.entryVariable.set("")
        print(self.entryVariable.get())
        self.labelVariable.set(self.entryVariable.get())
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

class main:
    '''Calls the gui class'''
    guiMain = gui(None)
    guiMain.title("Band Intensity Widget")
    guiMain.initializeGUI()
    ##allows each portion of the gui to loop indefinately
    guiMain.mainloop()
    
    """Calls the intensity and getdocument function"""
    document = getDocument()
    location = document.getFile()
    doc = document.process(location)
    
    
    print("this is the doc: ", doc)
    #calls the intensity class
    inten = bandIntensity()
    inten.readText(doc)
    inten.getIntensity()
    inten.addBackground()
    inten.getMeanIntensity()
    inten.outputValue()
    
    
    
    
    