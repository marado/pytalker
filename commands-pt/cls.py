# -*- coding: latin -*-

HELP = """Uso: .cls\r
Limpa o ecran."""

import src.messages
from config.messages import CLS

class Execute:
	def __init__(self,session,message):
		src.messages.Message(session).User(CLS)

class Help:
	def __init__(self,session): src.messages.Message(session).User(HELP)
