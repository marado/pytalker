#!/usr/bin/env python
# -*- coding: latin -*-

"""This is the file that starts the talker"""

import src.server
import socket
import sys
from config.config import TALKER_PORT
from config.messages import TALKER_PORT_IN_USE, TALKER_CTRL_C

if __name__ == '__main__':
	try: talker = src.server.Start()
	except socket.error: 
		print (TALKER_PORT_IN_USE % TALKER_PORT)
		sys.exit(0)
	try: talker.serve_forever()
	except KeyboardInterrupt:
		src.server.Stop(TALKER_CTRL_C)
