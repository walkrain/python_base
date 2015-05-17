#!/usr/bin/env python
# Filename: while.py

number = 23
running = True

while running:
    guess = int(input('Enter an interger:'))
    if guess == number:
	print 'Congratulations,you guess it.'
	running = False; # this cause the while loop stop
    elif guess < number:
	print 'it is higher than that'
    else:
	print 'it is lower than that'
else:
    print 'the while loop is over.'

print 'Done'
