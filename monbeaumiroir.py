#!/usr/bin/python




entree=0

def checkPal(valeur):   
    sequence=str(valeur)
    flag=0
    index=0
    index2=len(sequence)-1
    while(index<=index2):
        if(sequence[index]==sequence[index2]):
            flag=1
        else:
            return 0
        index+=1
        index2-=2
    if(flag==1):
        return 1




for index in xrange(0,len(sequence)):
        print(index)
        for index2 in xrange(len(sequence)-1,-1,-1):
            print(index2)
            if(sequence[index]==sequence[index2]):
                flag=1
                print("ok")
    
    
