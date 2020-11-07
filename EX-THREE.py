#Exercise 3
>>> def right_justify(s):
	print(' ' *65 + 'monty')

>>> right_justify('monty')
                                                                 monty

>>> def do_twice(f):
	f()
	f()

	
>>> def print_spam():
	print('spam')

	
>>> do_twice(print_spam)
spam
spam

>>> def do_twice(func, valu):
	f(valu)
	f(valu)

	
>>> def print_spam():
	print('spam')  #show me ERROR!



>>> def do_four(f,v):
	do_twice(f,v)
	do_twice(f,v)

	
>>> do_twice(f,v)       #show me the same ERROR 'NameError: name 'f' is not defined'





