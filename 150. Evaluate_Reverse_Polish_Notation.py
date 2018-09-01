# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 19:45:19 2018

@author: ustbp
"""

def suanshu(a):
    stack=[]
    for token in a :
        if token in ['+','-','*','/']:
            a,b=stack.pop(),stack.pop()
            if token =='+':
                res=a+b
            elif token=='-':
                res=a-b
            elif token=='*':
                res=a*b
            elif token=='/':
                res=a/b
            stack.append(res)
        else:
            stack.append(int(token))
    return stack.pop()
 
print(suanshu(['2','1','+','3','*']))