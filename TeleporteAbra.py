#!/usr/bin/python

def genAleatoire(valeurInitiale, temps):
    val = valeurInitiale
    final = (temps+0.0)/3
    step = 0
    e = 0
    n = 0 
    nbstep=0
    lastdir = ""
    while(step < final):
        nbstep+=1
        val = (137 * val + 187) % 256
        step+=1
        if(int(str(val)[-1])==0):
            n+=1
            #print(val,"n")
            lastdir = "n"
        elif(int(str(val)[-1])==1):
            e+=1
            lastdir = "e"
            #print(val,"e")
        else: 
            if(lastdir=="n"):
                n+=1
                #print(val,"n")
            if(lastdir=="e"):
                e+=1
                #print(val,"e")

    print(nbstep)
    return(n,e)



genAleatoire(30,10*60)
