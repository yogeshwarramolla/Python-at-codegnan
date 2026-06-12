Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=19
>>> b=2324
>>> c=a+b
>>> printf(c)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    printf(c)
NameError: name 'printf' is not defined. Did you mean: 'print'?
>>> print c
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> clear
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> num1,num2,num3=10,20,30,
>>> print(num1+num2
...       )
30
>>> print("yogi")
yogi
>>> print(num1)
10
>>> num1=num2=num3=10
>>> num1=num2=num3=10
>>> print(num1)
10
>>> print(id=num1)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(id=num1)
TypeError: print() got an unexpected keyword argument 'id'
>>> print(id(num1,num2))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(id(num1,num2))
TypeError: id() takes exactly one argument (2 given)
>>> print(id(num1))
140721653671112
>>> a,b=257,257
>>> print(id(a),id(b))
1705830243568 1705830243568
>>> bool(10)
True
>>> bool("yogi")
True
>>> bool(True + False)
True
