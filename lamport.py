# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 09:08:14 2019

@author: ahora
"""
import random
import hashlib

class lamport:
    def __init__(self,name='matin'):
        self.name=name
        
        


    def keygenaration(self):
        privatepair=[]
        publicpair=[]
        for x in range(256):
            a=random.getrandbits(256)
            b=random.getrandbits(256)
            privatepair.append([a,b])
            ha=self.hash_key(a)
            hb=self.hash_key(b)
            publicpair.append([ha,hb])
        return(privatepair,publicpair)
    
    def signature(self,M,privatepair):
        hashm=self.hash_key(M)
        sig=[]
        hashm=int(hashm,16)
        s=bin(hashm)
        s=s.replace('0b', '')
        le=len(s)
        if le<256 :
            count=256-le
            a=''
            for x in range(count):
                a=a+'0'
            s=a+s
        for y in range(256):
            sigpair=privatepair[y]
            if s[y]=='1':
                sig.append(sigpair[1])
            elif s[y]=='0':
                sig.append(sigpair[0])
        return sig
        
    
    def signatureverify(self,M,sig,publicpair):
        hashm=self.hash_key(M)
        hashm=int(hashm,16)
        s=bin(hashm)
        s=s.replace('0b', '')
        le=len(s)
        if le<256 :
            count=256-le
            a=''
            for x in range(count):
                a=a+'0'
            s=a+s
        for z in range(256):
            publicpairs=publicpair[z]
            if s[z]=='1':
                hashsig=self.hash_key(sig[z])
                if hashsig != publicpairs[1]:
                    print(z)
                    return False
            elif s[z]=='0':
                hashsig=self.hash_key(sig[z])
                if hashsig != publicpairs[0]:
                    print(z)
                    return False
        return True
            
        
        
    def hash_key(self,m1):
        m = hashlib.sha256()
        m.update(str(m1).encode('utf-8'))
        M=m.hexdigest()
        return M
        
            
            
            