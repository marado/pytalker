# -*- coding: latin -*-

NO_RULES = "Este talker nao tem regras definidas."
RULES_NA = "O ficheiro de regras para este talker nao esta' definido."
HELP = """Uso: .rules\r
Mostra-te as regras do talker."""

import src.messages
from config.config import RULES_SHOW, RULES_FILE

class Execute:
	def __init__(self,session,message):
                if RULES_SHOW:
                        try:
                                rules = open(RULES_FILE,mode='r')
                                for line in rules: session.handler.request.send(line + "\r")
                                rules.close()
                        except IOError: src.messages.Message(session).User(RULES_NA)
		else: src.messages.Message(session).User(NO_RULES)

class Help:
        def __init__(self,session): src.messages.Message(session).User(HELP)
