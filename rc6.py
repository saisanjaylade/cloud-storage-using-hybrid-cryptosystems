from Key_generation import *
from Raund import *
import random

def encrypt(value, main_key):
   
    K = main_key_generation(main_key)
    
    value_mas = key_parse(value)

    
    value_mas = enc_start_xor(value_mas, K[0], K[1])
    
    for i in range(2, 41, 2):
        value_mas = [int(i) for i in value_mas]
        value_mas = enc_raund(value_mas, K[i], K[i+1])
   
    value_mas = enc_end_xor(value_mas, K[42], K[43])
    
    value_mas = [hex(i)[2:] for i in value_mas]
    for i in range(len(value_mas)):
        value_mas[i] = "".join(["0" for t in range(8 - len(value_mas[i]))]) + value_mas[i]
    value_mas = value_mas[0] + value_mas[1] + value_mas[2] + value_mas[3]
    return value_mas.upper()


def decrypt(value, main_key):
   
    K = main_key_generation(main_key)
    
    value_mas = key_parse(value)
   
    value_mas = dec_start_xor(value_mas, K[42], K[43])
    
    g = [i for i in range(2, 41, 2)][::-1]
    for i in g:
        value_mas = [int(i) for i in value_mas]
        value_mas = dec_raund(value_mas, K[i], K[i+1])
    
    value_mas = dec_end_xor(value_mas, K[0], K[1])
   
    value_mas = [hex(i)[2:] for i in value_mas]
    for i in range(len(value_mas)):
        value_mas[i] = "".join(["0" for t in range(8 - len(value_mas[i]))]) + value_mas[i]
    value_mas = value_mas[0] + value_mas[1] + value_mas[2] + value_mas[3]
    return value_mas.upper()


def enc_start_xor(value_mas, K1, K2):
    A, B, C, D = value_mas[0], value_mas[1], value_mas[2], value_mas[3]
    B = mod(B + K1, 2**32)
    D = mod(D + K2, 2**32)
    return A, B, C, D

def enc_end_xor(value_mas, K1, K2):
    A, B, C, D = value_mas[0], value_mas[1], value_mas[2], value_mas[3]
    A = mod(A + K1, 2**32)
    C = mod(C + K2, 2**32)
    return A, B, C, D


def dec_start_xor(value_mas, K1, K2):
    A, B, C, D = value_mas[0], value_mas[1], value_mas[2], value_mas[3]
    A = mod(A - K1, 2**32)
    C = mod(C - K2, 2**32)
    return A, B, C, D

def dec_end_xor(value_mas, K1, K2):
    A, B, C, D = value_mas[0], value_mas[1], value_mas[2], value_mas[3]
    B = mod(B - K1, 2**32)
    D = mod(D - K2, 2**32)
    return A, B, C, D


def rc6_encrypt(value,key):
    value=value.upper()
    #m=len(value)
    if len(value) != 32:
        for i in range(32-len(value)):
            value=value+"0"
    key=key.upper()
    if len(key) != 32:
        for i in range(32-len(key)):
            key+="0"
    enc = encrypt(value, key)
    return(enc.upper())

def rc6_decrypt(enc,key):
    key=key.upper()
    if len(key) != 32:
        for i in range(32-len(key)):
            key+="0"
    dec = decrypt(enc, key)
    return(dec.upper())

