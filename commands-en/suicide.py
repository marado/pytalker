# -*- coding: latin -*-

NO_ARGS = "You should say what's your password!"
SUCCESS = "Goodbye, cruel world!"
WRONG_PASSWORD = "The password you wrote isn't correct!"
NOTICE = "As you look at %s, you see him commiting suicide!"
HELP = """Usage: .suicide <password>\r
Logs you off of the talker and removes your character."""

import src.messages
import hashlib
import os

from config.config import *

class Execute: 
	def __init__(self,session,password): 
		if not password: src.messages.Message(session).User(NO_ARGS)
		else: 
			if "\xff" in password: password = password[21: ]
			userfile = USERS_DIR + "/" + session.user.name.lower()
			f = open(userfile,'r')
			realpassword = f.read()
			f.close()
			if (not hashlib.sha512(password).hexdigest() == realpassword):
				src.messages.Message(session).User(WRONG_PASSWORD)
			else:
				# TODO apagar o userfile
				src.messages.Message(session).User(SUCCESS)
				session.logged = 0
				src.messages.Message(session).All(NOTICE % (session.user.name))
				os.remove(userfile)
class Help:
	def __init__(self,session): src.messages.Message(session).User(HELP)
