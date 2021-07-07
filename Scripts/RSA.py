from tkinter import *
from math import *


#Functions
def Calc():
    global n
    p1=int(p.get())
    q1=int(q.get())
    n=p1*q1
    chaine.configure(text='n='+str(n))
    global phiden
    phiden=(p1-1)*(q1-1)
    chaine1.configure(text='phi_n='+str(phiden))
    r=0
    global e
    e=0
    i=1
    r=0
    while r==0:
        if((p1<e)and(q1<e)and(e<phiden)and(e/i!=phiden/i)):
            r=1
        i=i+1
        e=e+1
    chaine2.configure(text='Public Key=('+str(e)+','+str(n)+')')
    global d
    d=0
    i=1
    r=0
    while r==0:
        if(e*d%phiden==1):
            r=1
        i=i+1
        d=d+1
    chaine3.configure(text='Private Key=('+str(d-1)+','+str(n)+')')
    
def wordcrypt():
    mot1=str(mot.get(0.,END))
    taille=len(mot1)
    i=0
    crypter = " "
    while i<taille:
        ascii = ord(mot1[i])
        lettre_crypt = ascii**e%n
        crypter = crypter + str(lettre_crypt) + " "
        i = i + 1
    open("message.txt", "w").write(crypter)

#--------------------------------------------------------------------------
 
fen1 = Tk()
fen1.title('RSA PPR')
#Entry positioning
p = Entry(fen1)
q = Entry(fen1)
mot = Text(fen1)
#Display instructions
pt= Label(fen1, text='Enter p prime')
qt= Label(fen1, text='Enter q prime')
mt= Label(fen1, text='Enter the text to encrypt')
mp=Label(fen1, text='PROVOST Mathis')
fac=Label(fen1, text='L2PC University Of Toulon ')
#Text 
chaine= Label()
chaine1= Label()
chaine2= Label()
chaine3= Label()
#Buttons
b1= Button(text='Calculate the keys', command=Calc)
b2= Button(text='Encrypt', command=wordcrypt)
b1.grid(row =3)
b2.grid(row =7)
#Text positioning
chaine.grid(row =2, column =1)
chaine1.grid(row =3, column =1)
chaine2.grid(row =4, column =1)
chaine3.grid(row =5, column =1)
#Instructions positioning
qt.grid(row =0)
pt.grid(row =1)
mt.grid(row =6)
mp.grid(row =1, column =2)
fac.grid(row =2, column =2)
#Entry areas positioning
p.grid(row =0, column =1)
q.grid(row =1, column=1)
mot.grid(row =6, column=1)
fen1.mainloop()
