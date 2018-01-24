
class bandIntensity:
    """this class take a txt file input and calculates the values
    band intensity and outputs the values"""
    global nArray
    global mean
    global array
    
    array = []
    nArray = []    
    
    def checkNumber(self, s):
        #trys whether an entry is a string or a number
        #true if number flase else
        try:
            float(s)
            return True
        except ValueError:
            pass
     
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass     
        return False
    
    def readText(self, text): 
        with open(text, 'r') as file:
            data = file.readlines()
            for line in data:                
                if self.checkNumber(line) == True:
                    continue
                else:
                    array.extend([float(i) for i in line.split()])                
    
    def getIntensity(self):        
        #create a new array, add zero elements until
        #it reaches the size of the input
        n = len(array)
        #print(n)
        for i in range(n):
            data = 255 - array[i]
            nArray.append(data)
        
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
        
        
'''note now i want to add functionallity that can read different columns of data so there should be no processing'''

class getDocument:
    
    global destination
    
    def getFile(self):
        print('please enter the file desintination')
        destination = (input())
        return destination
        #destination = process(destination)
       
    def process(self, string):
        #thisfunction is essential as it changes the file destination to one which python can read
        s = string
        #n = len(s)
        new_str = s.replace('\\', '/')
        print(new_str)
        return new_str
        

                        

class main:
    """Calls the intensity and getdocument function"""
    document = getDocument()
    location = document.getFile()
    doc = document.process(location)
    
    #calls the intensity class
    inten = bandIntensity()
    inten.readText(doc)
    
    
    '''
    intensity = bandIntensity()
    data = 'C:/Users/paulk/Documents/DNAmean.txt'
    intensity.readText(data)
    intensity.getIntensity()
    intensity.addBackground()
    intensity.getMeanIntensity()
    intensity.outputValue()'''
    
    
    
    