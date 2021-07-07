c=input("What is the text to decypher ? ")
L_letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
          'o','p','q','r','s','t','u','v','w','x','y','z']
L_nbr=[0]*26
for i in range(len(c)):
    for j in range(len(L_letter)):
        if c[i]==L_letter[j]:
            L_nbr[j]=L_nbr[j]+1
print("Here is how many times each letter appeared in the text: ",L_nbr)
maxi=max(L_nbr)
for i in range(len(L_nbr)):
    if L_nbr[i]==maxi:
        index=i
print("The index of the most present letter is : ",index)
print("The letter that appears the most in the encrypted text is : ",L_letter[index])
shift=ord(L_letter[index])-ord("e")
print("The key is: ",shift)
b=shift
Lc=[]
final=''
k=0
i=0
while i<len(c):
	Lc.append(c[i])
	if 64<ord(Lc[i])<91 :
		val= ord(Lc[i])-65
		val= (val-b)%26
		val=val+65
		Lc[i]=chr(val)
	elif 96<ord(Lc[i])<123:
		val= ord(Lc[i])-97
		val= (val-b)%26
		val=val+97
		Lc[i]=chr(val)		
	i=i+1		
while k<len(Lc):
	final=final+Lc[k]
	k=k+1
print (final)

	
	
