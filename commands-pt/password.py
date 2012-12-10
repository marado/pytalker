# -*- coding: latin -*-

NO_ARGS = "Devias dizer qual e' a nova password!"
SUCCESS = "A tua password foi alterada."
HELP    = """Uso: .password <nova password>\r
Muda a tua password para uma nova."""

import src.messages
import hashlib

from config.config import *

class Execute: 
	def __init__(self,session,password): 
		if not password: src.messages.Message(session).User(NO_ARGS)
		else: 
			if "\xff" in password: password = password[21: ]
			userfile = USERS_DIR + "/" + session.user.name.lower()
			f = open(userfile,'w')
			encrypted_password = hashlib.sha512(password).hexdigest()
			f.write(encrypted_password)
			f.close()
			src.messages.Message(session).User(CLS)
			src.messages.Message(session).User(SUCCESS)
class Help:
	def __init__(self,session): src.messages.Message(session).User(HELP)
