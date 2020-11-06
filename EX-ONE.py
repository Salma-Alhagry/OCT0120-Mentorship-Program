#Exercies ONE
>>> print('hello world')
hello world
>>> print('hello world)
      
SyntaxError: EOL while scanning string literal
>>> print'hello world'
SyntaxError: invalid syntax
>>> prnt('hello world')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    prnt('hello world')
NameError: name 'prnt' is not defined
>>> print(-2)
-2
>>> print(+2)
2
>>> print(2++2)
4
>>> print(09)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> print(95)
95
>>> print(42*60+42   +'second')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(42*60+42   +'second')
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> second = 42*60+42
>>> print(seond)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(seond)
NameError: name 'seond' is not defined
>>> print(second,  'second')
2562 second
>>> miles = 10/1.61
>>> print(miles, 'miles')
6.211180124223602 miles
>>> average_pace = second/miles
>>> print(average_pace, 'mile in minute and second')
412.482 mile in minute and second
>>> speed = miles/second
>>> min = 42/60 + 42
>>> print(min, 'minutes')
42.7 minutes
>>> hour =min /60
>>> print(hour, 'hours')
0.7116666666666667 hours
>>> speed = miles/hour
>>> print(speed, 'miles per hour')
8.727653570337614 miles per hour
>>> #-----------------------------------------
