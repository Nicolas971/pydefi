#!/usr/bin/python



def estPremier(number): 
    for index in xrange(3,number,2):
        if(number%index==0):
            return 1
    return 0


seuil=72
nombre=0
#25k+26

for x in xrange(0,10000):
    if(estPremier(25*x+26)==0):
        nombre+=1
    if(nombre==72):
        print(25*x+26,x)
        




    


      
        
