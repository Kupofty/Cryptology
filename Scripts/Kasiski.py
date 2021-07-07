def PGCD (a,b) : 
    if a <= 0 or b <= 0 :
        print("Error")
    if a == 1 or b == 1 :
        return 1
    if a == b :
        return a
    if a < b :
        return PGCD (a, b-a)
    return PGCD (b, a-b)
#---------------------------------
def KeyLength (text, word = 3) :    
    dictionary = {}
    for i in range (0, len (text)-2) :
        t = text [i:i+word]
        if t in dictionary : dictionnary [t].append (i)
        else : dictionary [t] = [i]      
    distance = []
    for d in dictionary:
        p = dictionary [d]
        if len (p) > 1 :
            for i in range (0, len (p)-1) : 
                distance.append ( p [i+1] - p [i] )          
    length = PGCD (distance [0], distance [1])
    for d in distance :
        length = PGCD (length, d)
    return "The key length is :", length

#-------------------------------------------------------------------------------                          
def FrequencyAnalysis(c):
    L_letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
              'o','p','q','r','s','t','u','v','w','x','y','z']
    L_nbr=[0]*26
    for i in range(len(c)):
        for j in range(len(L_letter)):
            if c[i]==L_letter[j]:
                L_nbr[j]=L_nbr[j]+1 
    maxi=max(L_nbr)
    for i in range(len(L_nbr)):
        if L_nbr[i]==maxi:
            index=i
    return(L_letter[index])

#|---------------------------------
def Key(encryptedtext,keylength): 
    a=""
    key=""
    for j in range(0,keylength):
        for i in range(j,len(encryptedtext),keylength):
            a=a+encryptedtext[i]
            letter=FrequencyAnalysis(a)
            key=key+letter
            a=""  
    print("The key is:",key)
    
    
