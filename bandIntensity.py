# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 11:35:04 2018

@author: paulk
"""
class bandIntensity:
    """this class take a txt file input and calculates the values
    band intensity and outputs the values"""
    global mean
    bandavg = [46.672, 43.102, 47.29, 109.98, 29.005, 75.975, 69.516, 110.245]
    sum = 0
    
    def getIntensity(array):        
        #create a new array, add zero elements until
        #it reaches the size of the input
        nArray = [0]
        for i in len(array-1):
            nArray.append(0)
            
        for i in array:
            nArray[i] = 255 - array[i]
            print(nArray[i])
    
    def getMeanIntensity(array):
        sum = 0
        for i in array:
            sum += array[i]
            
        mean = sum/len(array)
        
    def outputValue():
        print("Average intensity: {}".format(mean))
