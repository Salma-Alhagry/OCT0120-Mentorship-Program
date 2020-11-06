>>> #Exercise TWO
>>> 42 = n
SyntaxError: cannot assign to literal
>>> x = y = 1
>>> print(x)
1
>>> print(y)
1
>>> print('semi-colon Test');
semi-colon Test
>>> x = 3;
>>> print(x);
3
>>> print(x*y)
3
>>> print(xy)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    print(xy)
NameError: name 'xy' is not defined
>>> import math
>>> r = 5
>>> volume = math.pi(4/3 * r**3)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    volume = math.pi(4/3 * r**3)
TypeError: 'float' object is not callable
>>> import math*
SyntaxError: invalid syntax
>>> import math
>>> r = 5
>>> volume = math.pi((4/3)*(r**3))
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    volume = math.pi((4/3)*(r**3))
TypeError: 'float' object is not callable
>>> print(5**3)
125
>>> print(4/3)
1.3333333333333333
>>> price_discounted = (24.95*60)/100
>>> print(price_discounted)
14.97
>>> first_book = price_discounted + 3
>>> print(first_book)
17.97
>>> total = ((price_discounted + 0.75)*59 + price_discounted)
>>> print(total)
942.45
>>> print(total , 'LE')
942.45 LE
>>> easy_mile = 2 * 8.25
>>> print(easy_mile)
16.5
>>> tempo_mile = 3 * 7.2
>>> print(tempo_mile)
21.6
>>> total_time = easy_mile + tempo_mile
>>> print(total_time)
38.1
