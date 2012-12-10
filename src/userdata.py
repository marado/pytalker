# -*- coding: latin -*-

import os,hashlib,re
from config.config import USERS_DIR

RANK_FIELD="rank"
RANK_FIELD_DESC="desc"
RANK_FIELD_LEVEL="level"
ROOM_FIELD="room"

def GetField(username,field):
	#read from file
	userfile = USERS_DIR + "/" + username.lower()
        f = open(userfile,'r')
	value=''
	for line in f:
		if(line.startswith( '%s:' % field )):
			value = re.search( '^%s:(.*)$' % (field) , line)
        f.close()
	if(value == '' ): return ''
	else: return value.group(1)

def SetField(username, field, value):
	userfile = USERS_DIR + "/" + username.lower()
	#first, read all file, replacing the field
	currcontent = []
	#
	#read file
	if(os.path.isfile(userfile)):
		f = open(userfile,('r'))
		for line in f:
			currcontent.append(line)
	#
	#replace content
	newcontent = []
	found = 0
	for line in currcontent:
		if(line.startswith( '%s:' % field )):
			line=('%s:%s' % ( field, value ))
			found = 1
		newcontent.append(line)
	if( not found ):
		newcontent.append('%s:%s' % (field,value))
	#
	#write the file again
        f = open(userfile,'w')
	for line in newcontent:
		line=line.strip('\r\n')
        	f.write('%s\n' % line)
        f.close()
