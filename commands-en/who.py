# -*- coding: latin -*-

IDLE_START = 47
TITLE= """- Who is online? -------------------------------------------------\r
- Name -------------------------------------- Idle Time ----------"""
BODY = "  %s %s %s"
END = "- End of 'who' command -------------------------------------------"
HELP = """Usage: .who\r
Shows you the users currently online in the talker."""

import src.messages
import time,math

class Execute:
	def __init__(self,session,message):
                src.messages.Message(session).User(TITLE)
                for user in session.allusers.userdict:
                        spaces = " " * (IDLE_START - len(session.allusers.userdict[user].name) - 5)
			curr_time=int(time.time() - session.allusers.userdict[user].time)
			#change the unit
			curr_time_s=0
			curr_time_m=0
			curr_time_h=0
			if(curr_time<60):
				curr_time_s=curr_time
			curr_time_m=curr_time/60
			if(curr_time>=60):
				curr_time_m=math.floor(curr_time_m)
				curr_time_s=curr_time%60
			curr_time_h=curr_time/3600
			if(curr_time>=3600):
				curr_time_h=math.floor(curr_time_h)
				curr_time_m=math.floor(curr_time/3600)
				curr_time_s=curr_time%60
			curr_time=("%02d:%02d:%02d" % (curr_time_h,curr_time_m,curr_time_s))
			#end changing the unit
                        src.messages.Message(session).User(BODY % (session.allusers.userdict[user].name, spaces, curr_time))
                src.messages.Message(session).User(END)

class Help:
        def __init__(self,session): src.messages.Message(session).User(HELP)
