# -*- coding: utf-8 -*-
"""200901007_Assignment_02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uPOax7AvCEGqwVvkxJGEBYOYwc8qyE5i
"""

#****************QUESTION#1*************

import regex as re
reg = "[\w.+-.*.(.)]"
string1="a + (b*c)"
string2="3+ (5*2)"
result1=re.findall(reg,string1)
result2=re.findall(reg,string2)
print(result1)
print(result2)

#******************QUESTION#2******************
import ast
code = "print('Using AST library!')"
r=ast.parse(code)  
print(r)
exec(compile(code, filename="", mode="exec"))  

expression = '10 * 20 / 40'  
code = ast.parse(expression, mode='eval')  
  
print(eval(compile(code, '', mode='eval')))  
print(ast.dump(code)) 



tree = ast.parse('''  
courses = ['Software Engineering', 'Compiler construction']  
name = 'Imama'  
  
for cor in courses:  
    print('{} learn {}'.format(name, courses))  
''')  
  
print(ast.dump(tree))

#*******************second method of doing QUESTION#2***************************


import ast

expression = '5/3+8'
code = ast.parse(expression, mode='eval')
print(ast.dump(code))
print(eval(compile(code, '', mode='eval')))