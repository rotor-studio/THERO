#!/usr/bin/env python

import cgi
import cgitb

cgitb.enable()

print "Content-type: text/html\n\n"

form=cgi.FieldStorage()

if "data" not in form:
    print "<h3>Uoops the test field is empty!</h3>"
else:
    text=form["data"].value
    print "<h3>Added to your Blacklist!</h3>"
    print cgi.escape(text)

    file = open("/home/pi/Desktop/blacklistoutput.txt","a+")
    str = text+"\n"
    for line in file.readlines():
        print line.strip()
    file.write(str)
    file.close()


