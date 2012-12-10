# -*- coding: latin -*-

TITLE= """- User info: -----------------------------------------------------"""
TITLE_LIST= """- Users: ---------------------------------------------------------"""
BODY = """  %-12s: %s"""
BODY_LIST = """   %s (%s)"""
END = """- End of 'user' command ------------------------------------------"""
HELP = """Usage: .user [<user>]|-l\r
Shows user info or users of the talker.\r
Options:\r
    -l                 shows you all the users of the talker.\r
    [<nick>]           shows you the info of a given user.\r
                       If you omit <nick> then it applies to you."""
NO_SUCH_USER=""" No user with that name""" 
CANT_DO_THAT=""" You can't see your info, unless you're an administrator."""

import time,os
import src.messages
import config.ranks
from src.userdata import *
from config.config import USERS_DIR

class Execute:
	def __init__(self,session,message):
		self.message=message.split()
		if(len(self.message)==0):
			"""show my status"""
                	src.messages.Message(session).User(TITLE)
			src.messages.Message(session).User(BODY%('nick',session.user.name))
			src.messages.Message(session).User(BODY%('rank',session.user.rank.name))
                	src.messages.Message(session).User(END)
		else:
			"""show user list"""
			if(self.message[0]=="-l"):
	                	src.messages.Message(session).User(TITLE_LIST)
				#get all
				usr_lst = {}
				for usr in os.listdir(USERS_DIR):
					usr_lst[usr]=config.ranks.RANKS[src.userdata.GetField(usr,RANK_FIELD)]['name']
				#print
				for usr in usr_lst:
					src.messages.Message(session).User(BODY%(usr,usr_lst[usr]))
	                	src.messages.Message(session).User(END)
			else:
                		src.messages.Message(session).User(TITLE)
				src.messages.Message(session).User(BODY%('nick',self.message[0]))
				src.messages.Message(session).User(BODY%('rank',config.ranks.RANKS[src.userdata.GetField(self.message[0],RANK_FIELD)]['name']))
                		src.messages.Message(session).User(END)
				
				

class Help:
        def __init__(self,session): src.messages.Message(session).User(HELP)
