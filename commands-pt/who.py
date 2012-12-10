# -*- coding: latin -*-

IDLE_START = 47
TITLE= """- Quem esta' ligado? ---------------------------------------------\r
- Nome --------------------------- Tempo de inactividade (seg) ---"""
BODY = "  %s %s %s"
END = "- Fim do comando 'who' -------------------------------------------"
HELP = """Uso: .who\r
Mostra-te quem esta' actualmente ligado no talker."""

import src.messages
import time

class Execute:
	def __init__(self,session,message):
                src.messages.Message(session).User(TITLE)
                for user in session.allusers.userdict:
                        spaces = " " * (IDLE_START - len(session.allusers.userdict[user].name) - 5)
                        src.messages.Message(session).User(BODY % (session.allusers.userdict[user].name, spaces, `int(time.time() - session.allusers.userdict[user].time)`))
                src.messages.Message(session).User(END)

class Help:
        def __init__(self,session): src.messages.Message(session).User(HELP)
