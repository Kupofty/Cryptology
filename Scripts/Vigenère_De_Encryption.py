from math import *
a=input("Encryption (E) or Decryption (D) : ")
b=input("Key: ")
Lc=[]
Lkey=[]
Lf=[]
final=''
k=0
i=0
if a=='E':
	c=input("What is the text to encrypt? ")
	for p in range(len(b)):
		Lkey.append(b[p])
	while len(Lkey)>len(c):
		del(Lkey[-1])
	while i<len(c):
		Lc.append(c[i])
		if 64<ord(Lc[i])<92:
			val1=ord(Lc[i])-65
			val2=ord(Lkey[i%(len(b))])-97
			val=(val1+val2)%26
			val=val+65
			Lf.append(chr(val))
		elif 96<ord(Lc[i])<123:
			val1=ord(Lc[i])-97
			val2=ord(Lkey[i%(len(b))])-97
			val=(val1+val2)%26
			val=val+97
			Lf.append(chr(val))
		elif Lc[i]==' ':
			Lf.append(' ')
		i=i+1
	while k<len(Lf):
		final=final+Lf[k]
		k=k+1
	print(final)
#-----------------------------------------------------------------------------------------------------------------------	
elif a=='D':
	c=input("What is the text to decrypt ? ")
	for p in range(len(b)):
		Lkey.append(b[p])
	while len(Lkey)>len(c):
		del(Lkey[-1])
	while i<len(c):
		Lc.append(c[i])
		if 64<ord(Lc[i])<92:
			val1=ord(Lc[i])-65
			val2=ord(Lkey[i%(len(b))])-97
			val=(val1-val2)%26
			val=val+65
			Lf.append(chr(val))
		elif 96<ord(Lc[i])<123:
			val1=ord(Lc[i])-97
			val2=ord(Lkey[i%(len(b))])-97
			val=(val1-val2)%26
			val=val+97
			Lf.append(chr(val))
		elif Lc[i]==' ':
			Lf.append(' ')
		i=i+1
	while k<len(Lf):
		final=final+Lf[k]
		k=k+1
	print(final)
















