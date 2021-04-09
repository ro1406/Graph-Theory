# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 15:23:47 2021

@author: rohan
"""

# Program to find the value of P. No need any guesses. 
from itertools import permutations
import numpy as np
size=int(input("Enter the value of n for an nxn matrix: "))
A1=[]
A2=[]
print("Enter the matrix A1: ")
for i in range(size):
    A1.append([int(x) for x in input().strip()])   #list(map(int,input().split()))
    
print("\nEnter the matrix A2: ")
for i in range(size):
    A2.append([int(x) for x in input().strip()])

A1=np.array(A1)
A2=np.array(A2)

arr=list(range(size))
perms= list(permutations(arr))
found=False
count=0
for a in perms:
    P=np.zeros((size,size))
    for i in range(len(a)):
        P[i][a[i]]=1
    
    if int((np.dot(P,A1)==np.dot(A2,P)).mean())==1:
        print("\n")
        print("FOUND!!")
        found=True
        print("P = ")
        print(P)
        count+=1
if found:
    print("A1 and A2 are isomorphic!")
    if count>1:
        print("There are "+str(count)+" matrices that could be used as P!")
    else:
        print("There is a unique matrix that could be used as P!")
else:
    print("Error, unable to find such a matrix P!\nPlease check A1 and A2 and make sure they are correct. If they are, then A1 is NOT isomorphic to A2.") 
