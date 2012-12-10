# -*- coding: latin -*-

NO_RULES = "This talker has no rules policy."
RULES_NA = "The rules file for this talker is not available."
HELP = """Usage: .rules\r
Shows you the talker's rules."""

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
