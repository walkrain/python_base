#!/usr/bin/python
# Filename:str_test.py

def tester(string):
    if len(string) < 10:
	return 'too short'
    elif (len(string) > 10) and (string.find('X') != -1):
	return string
	print 'X stopped'
    else:return string
def main():
    while(True):
        getInput = raw_input('Write sonething(quit ends):')
        if getInput != 'quit':
            print (tester(getInput))
        else:break

if __name__ == '__main__':
    main()
