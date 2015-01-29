#!/usr/bin/env python
 
import cgi
 
form = cgi.FieldStorage()
 
name = form.getvalue('name')
family = form.getvalue('family')
 
print "Content-type: text/html"
print
print "The form input is below...<br/>"
print "First name: " + name + "<br/>"
print "Last name: " + family + "<br/>"
if form.getvalue('check') == 'True':
    print "You checked the box!<br/>"
else:
    print "You didn't check the box!<br/>"
print "<br/>"
print "<form method=\"post\" action=\"page1.py\">"
print "Birthday: <input type=\"text\" name=\"birthday\" cols=\"40\" rows=\"1\"><br>"
print "Main Hobby: <input type=\"text\" name=\"hobby\" cols=\"40\" rows=\"1\"><br>"
print "<input type=\"submit\" value=\"Submit\">"
print "</form>"