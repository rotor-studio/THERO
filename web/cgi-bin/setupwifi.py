#!/usr/bin/env python

import cgi
import cgitb

cgitb.enable()

print "Content-type: text/html\n\n"

form=cgi.FieldStorage()

if "data" not in form:
    print "<h3>Uoops the text field is empty!</h3>"
else:
    text=form["data"].value
    text1=form["data1"].value
    print "<h3>Added!</h3>"
    print cgi.escape("SSDI: "+text+"\n"+"PSRWD: "+text1)

    file = open("/home/pi/Desktop/wifioutput.txt","a+")
    str = "SSDI: "+text+"\n"+"PSRWD: "+text1
    for line in file.readlines():
        print line.strip()
    file.write(str)
    file.close()


