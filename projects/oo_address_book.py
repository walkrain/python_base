#!/usr/bin/python
# Filename:oo_address_book.py

import cPickle as p


addrbook = 'addrbook.data'

addrlist = {'jim':'jim@126.com',
            'kate':'kate@126.com',
            'jack':'jack@126.com'
            }

name = raw_input('Enter a name:')
email = raw_input('Enter email:')
addrlist[name] = email

name = raw_input('Del a name:')
if addrlist.has_key(name):
    del addrlist[name]
else:
    print 'Not found %s in addrbook' %name

f = file(addrbook,'w')
p.dump(addrlist,f)
f.close

del addrlist

f = file(addrbook)
storedlist = p.load(f)

for name, address in storedlist.items():
    print '%s email is %s :' %(name,address)

if 'kate' in storedlist:
    print "has found kata her email is %s:" %storedlist['kate']
if storedlist.has_key('kate'):
    print 'has found kate her email is %s:' %storedlist['kate']

