# -*- coding: latin -*-

NO_ARGS = "You should say what's the new password!"
SUCCESS = "You password has been changed."
HELP    = """Usage: .password <new-password>\r
Changes your password to a new one."""

import src.messages,src.userdata
import hashlib

from config.config import *
from config.messages import *

class Execute: 
	def __init__(self,session,password): 
		if not password: src.messages.Message(session).User(NO_ARGS)
		else: 
			if "\xff" in password: password = password[21: ]
			encrypted_password = hashlib.sha512(password).hexdigest()
			src.userdata.SetField(session.user.name.lower(),'passwd',encrypted_password)
			src.messages.Message(session).User(CLS)
			src.messages.Message(session).User(SUCCESS)
class Help:
	def __init__(self,session): src.messages.Message(session).User(HELP)
