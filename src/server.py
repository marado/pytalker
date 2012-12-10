# -*- coding: latin -*-

import SocketServer
from config.config import TALKER_PORT
from config.messages import TALKER_STARTED, TALKER_STOPPED
import handler
import os

class Start(SocketServer.ThreadingTCPServer):
	def __init__(self):
		SocketServer.ThreadingTCPServer.__init__(self,('0.0.0.0',TALKER_PORT),handler.Handle)
		print (TALKER_STARTED % (TALKER_PORT, os.getpid()))

class Stop:
	def __init__(self, message): 
		# TODO: kill the socket here
		print (TALKER_STOPPED % message)
