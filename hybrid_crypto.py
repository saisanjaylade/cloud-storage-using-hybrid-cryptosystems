from blowfish import *
from rc6 import *

def hybrid_enc(txt,key):
    b1=[]
    r1=[]
    temp1,temp2="",""
    for i in range(len(txt)):
        if (i%48 < 16 ):
            temp1=temp1+txt[i]
            if (len(temp1)==16 or i==len(txt)-1):
                b1.append(temp1)
                temp1=""
                if i==len(txt)-1:
                    break

        if (i%48>=16 and i%48<48):
            temp2=temp2+txt[i]
            if len(temp2)==32 or i==len(txt)-1:
                r1.append(temp2)
                temp2=""
                if i==len(txt)-1:
                    break
    
    b=[]
    for i in b1:
        b.append(blowfish_enc(i))
    r=[]
    for i in r1:
        r.append(rc6_encrypt(i, key))

    enc=[]
    for i in range(len(r)):
        enc.append(b[i]+r[i])
    if len(b)>len(r):
        enc.append(b[-1])
    
    encrypted_txt=""
    for i in enc:
        encrypted_txt+=i
    
    return encrypted_txt

def hybrid_dec(txt,key):
    b1=[]
    r1=[]
    temp1,temp2="",""
    for i in range(len(txt)):
        if (i%48 < 16 ):
            temp1=temp1+txt[i]
            if (len(temp1)==16 or i==len(txt)-1):
                b1.append(temp1)
                temp1=""
                if i==len(txt)-1:
                    break

        if (i%48>=16 and i%48<48):
            temp2=temp2+txt[i]
            if len(temp2)==32 or i==len(txt)-1:
                r1.append(temp2)
                temp2=""
                if i==len(txt)-1:
                    break

    b=[]
    for i in b1:
        b.append(blowfish_dec(i))
    r=[]
    for i in r1:
        r.append(rc6_decrypt(i, key))
    
    dec=[]
    for i in range(len(r)):
        dec.append(b[i]+r[i])
    if len(b)>len(r):
        dec.append(b[-1])

    decrypted_txt=""
    for i in dec:
        decrypted_txt+=i
    return decrypted_txt