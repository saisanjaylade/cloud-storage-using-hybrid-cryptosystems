from blowfish import *
from rc6 import *

a="123456781234567812345678123456781234567812345678123456781"
key="abc123abc"

m=0
b1=[]
r1=[]
m=[]

temp1=""
temp2=""
for i in range(len(a)):

    
    if (i%48 < 16 ):
        temp1=temp1+a[i]
        if (len(temp1)==16 or i==len(a)-1):
            b1.append(temp1)
            temp1=""
            if i==len(a)-1:
                break

    if (i%48>=16 and i%48<48):
        temp2=temp2+a[i]
        if len(temp2)==32 or i==len(a)-1:
            r1.append(temp2)
            m.append(len(temp2))
            temp2=""
            if i==len(a)-1:
                break

print(b1)
print(r1)
print("\n")
b=[]
for i in range(len(b1)):
    b.append(blowfish_enc(b1[i]))
    if i%2 != 0:
        b.pop()
        b.append(blowfish_enc(b1[i]))
r=[]
for i in r1:
    r.append(rc6_encrypt(i, key))

print("\n")
print(b)
print(r)

enc=[]
for i in range(len(r)):
    enc.append(b[i]+r[i])
if len(b)>len(r):
    enc.append(b[-1])

encrypted_txt=""
for i in enc:
    encrypted_txt+=i

print("\n")
print(enc)
print("the plane text is :",a)
print("the encrypted txt is:",encrypted_txt)



dec=[]
for i in range(len(enc)-1):
    a=enc[i][16:]
    b=enc[i][0:16]
    dec.append(blowfish_dec(b)+rc6_decrypt(a, key, m[i]))


if len(enc[-1])==16:
    a=enc[-1][10:16]
    dec.append(blowfish_dec(a))
else:
    a=enc[-1][16:]
    b=enc[-1][0:16]
    dec.append(blowfish_dec(b)+rc6_decrypt(a, key, m[-1]))
print("\n")
print(dec)
decrypted_txt=""
for i in dec:
    decrypted_txt+=i
print("\n")
print("the decrypted text is :",decrypted_txt)



