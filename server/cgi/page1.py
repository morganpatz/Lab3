#!/usr/bin/env python
import cgi
 
form = cgi.FieldStorage()

print "Content-type: text/html"
print 
print "<form method=\"post\" action=\"page2.py\">"
print "First Name: <input type=\"text\" name=\"name\" cols=\"40\" rows=\"1\"><br>"
print "Family Name: <input type=\"text\" name=\"family\" cols=\"40\" rows=\"1\"><br>"
print "<input type=\"checkbox\" name=\"check\" value=\"True\"> Check this if you want <br>"
print "<input type=\"submit\" value=\"Submit\">"
print "</form>"

if form:
    bday = form.getvalue('birthday')
    hobby = form.getvalue('hobby')    
    print
    print "The form input is below...<br/>"
    print "Birthday: " + bday + "<br/>"
    print "Main Hobby: " + hobby + "<br/>"
