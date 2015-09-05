#! /usr/bin/env python
"""this module provides functions for authentication users"""

def login(username, password):
	try:
		user_file = open('/etc/users.txt')
		user_buf = user_file.read()
		users = [line.split("|")for line in user_buf.split("\n")]
		if [username, password] in users:
			return True
		else:
			return False
	except:
		print "I can't authenticate you."
		return False

def logout():
	print "this line is not covered by test case"
	print "this line is also not covered by test case"



