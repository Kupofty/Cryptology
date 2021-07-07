a=input("Encryption (E) or Decryption (D) : ")
b=int(input("Key : "))
Lc=[]
final=''
k=0
i=0
if a=='E':
	c=input("What is the text to encrypt? ")
	while i<len(c):
		Lc.append(c[i])
		if 64<ord(Lc[i])<91 :
			val= ord(Lc[i])-65
			val= (val+b)%26
			val=val+65
			Lc[i]=chr(val)
		elif 96<ord(Lc[i])<123:
			val= ord(Lc[i])-97
			val= (val+b)%26
			val=val+97
			Lc[i]=chr(val)	
		i=i+1
	while k<len(Lc):
		final=final+Lc[k]
		k=k+1
	print (final)    
elif a=='D':
	c=input("What is the text to decrypt ? ")
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
