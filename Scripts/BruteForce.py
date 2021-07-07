c=input("What is the text to decypher ? ")
for b in range (1,26):
    final=''
    i=0
    k=0
    Lc=[]
    while i<len(c):
        Lc.append(c[i])

        if 64<ord(Lc[i])<92 :
            val= ord(Lc[i])-65
            val= (val-b)%26
            val=val+65
            Lc[i]=chr(val)

        elif 96<ord(Lc[i])<124:
            val= ord(Lc[i])-97
            val= (val-b)%26
            val=val+97
            Lc[i]=chr(val)
        i=i+1
    
    while k<len(Lc):
        final=final+Lc[k]
        k=k+1

    print ('Decyphering key :',b,final)
