
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
            data = file.readlines()
            for line in data:
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


class main:
    """Calls the intensity function"""
    intensity = bandIntensity()
    data = 'C:/Users/paulk/Documents/DNAmean.txt'
    intensity.readText(data)
    intensity.getIntensity()
    intensity.addBackground()
    intensity.getMeanIntensity()
    intensity.outputValue()
    
    
    
    