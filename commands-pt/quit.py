# -*- coding: latin -*-

HELP = """Uso: .quit\r
Desliga-te do talker."""

import src.messages

class Execute: 
	def __init__(self,session,message): session.logged = 0
	
class Help:
	def __init__(self,session): src.messages.Message(session).User(HELP)
