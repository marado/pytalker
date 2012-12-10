# -*- coding: latin -*-

import common,time
import src.messages
import os
from config.ranks import *
from config.config import DEFAULT_ROOM,ROOMS_DIR
from src.userdata import ROOM_FIELD

class Room:
	def __init__(self,session):
		self.name = src.userdata.GetField(session.username,ROOM_FIELD)
		if ( not self.name ) or ( not os.path.isfile(ROOMS_DIR + "/" + self.name) ):
			self.name = DEFAULT_ROOM
		src.userdata.SetField(session.username,ROOM_FIELD,session.username)

	def Go(self,room):
		#read the room
		self.name=room
