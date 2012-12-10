# -*- coding: latin -*-

import SocketServer
import sessions
from config.config import WELCOME_SHOW,WELCOME_FILE

class Handle(SocketServer.BaseRequestHandler):
	def handle(self):
		if WELCOME_SHOW:
			try:
				welcome = open(WELCOME_FILE,mode='r')
				for line in welcome: self.request.send(line + "\r")
				welcome.close()
			except IOError: self.request.send("")
		session = sessions.Session(self)
		alive = 1
		while session.logged:
			message = session.Input()
			if not session.logged: 
				alive = 0
				break
			if not message: break
			session.Process(message)
		if (alive == 1):
			#save user details
			if session.login: session.Logout()
			del(session)
