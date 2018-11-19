import random

choices = ['r','p','s']

c = random.choice(choices)
p = input('r,p,s')


if c == 'r' and p == 's':
	print(c + ' vs ' + p + ': Computer Wins')
elif c == 'r' and p == 'p':
	print(c + ' vs ' + p + ': You Win')
elif c == 'r' and p == 'r':
	print(c + ' vs ' + p + ': DRAW')
elif c == 'p' and p == 'r':
	print(c + ' vs ' + p + ': Computer Wins')
elif c == 'p' and p == 's':
	print(c + ' vs ' + p + ': You Win')
elif c == 'p' and p == 'p':
	print(c + ' vs ' + p + ': DRAW')
elif c == 's' and p == 'p':
	print(c + ' vs ' + p + ': Computer Wins')
elif c == 's' and p == 'r':
	print(c + ' vs ' + p + ': You Win')
elif c == 's' and p == 's':
	print(c + ' vs ' + p + ': DRAW')