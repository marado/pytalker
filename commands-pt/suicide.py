# -*- coding: latin -*-

NO_ARGS = "Tens de dizer qual e' a tua password!"
SUCCESS = "Adeus, mundo cruel!"
WRONG_PASSWORD = "A password que inseriste nao esta' correcta!"
NOTICE = "Olhas para %s, e ve-lo a suicidar-se!"
HELP = """Uso: .suicide <password>\r
Desliga-te do talker e apaga a tua personagem."""

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
