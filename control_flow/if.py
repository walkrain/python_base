#!/usr/bin/env python
# Filename:if.py
number = 23
guess = int(input('Enter an interger:'))

if guess == number:
    print 'Congratulations,you guess it.' #New block starts here
    print 'but you do not win any prizes' #New block ends here
elif guess < number:
    print 'No,it is a little hogher than that' #another block start here
    #you can do anything you want in a block
else:
    print 'it is a little lower than that'
print 'Done' #this last statement is always executed,after if this is executed
