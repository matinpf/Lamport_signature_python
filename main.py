# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 09:08:07 2019

@author: mati fallahi
"""

from lamport import lamport
print('**********************')
print('**********************')
matin = lamport()

#genaration public and private key
print("genaration public and private key:")
private,public=matin.keygenaration()
print(private,public)
print('===========================')
print('===========================')
print('===========================')

#massage Sign up
print("massage Sign up:")
massage="salam khobi"
sigmassage=matin.signature(massage,private)
print(sigmassage)
print('===========================')
print('===========================')
print('===========================')

#Sign vefiry
print("Sign vefiry:")
result=matin.signatureverify(massage,sigmassage,public)
print(result)
print('===========================')


#Sign vefiry false
print("Sign vefiry false:")
sigmassage[22]=sigmassage[22]+1
result=matin.signatureverify(massage,sigmassage,public)
print(result)
