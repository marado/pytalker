# -*- coding: latin -*-

HELP = """Usage: .quit\r
Logs you off of the talker."""

import src.messages

class Execute: 
	def __init__(self,session,message): session.logged = 0
	
class Help:
	def __init__(self,session): src.messages.Message(session).User(HELP)
