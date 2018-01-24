
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
       
    def process(self, string):
        #thisfunction is essential as it changes the file destination to one which python can read
        s = string
        new_str = s.replace('\\', '/')
        print(new_str)
        return new_str
        

                        

class main:
    """Calls the intensity and getdocument function"""
    document = getDocument()
    location = document.getFile()
    doc = document.process(location)
    
    
    print("this is the doc: ", doc)
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
    
    
    
    