# -*- coding: latin -*-

"""This is the talker configuration file"""

# GENERAL TALKER CONFIGURATION
### This is the port where the talker will be running
TALKER_PORT = 2223
### Maximum length of the TCP packets
TALKER_BLOCK_SIZE = 1024

# LOGIN SCREEN
### Maximum length of usernames
LOGIN_MAX_LENGTH = 20
### Below are the logins which perform some commands, and thus users
### can't use (case insensitive).
LOGIN_COMMANDS = "who, version, rules"
### This is the lower that quits the user from the talker (case insensitive). 
LOGIN_QUIT = "quit"

# WELCOME SCREEN
### If 1 shows the welcome screen (contained in the file config/welcome, by
### default), if any available. To turn off, put 0 instead.
WELCOME_SHOW = 1
### This is the file where the welcome text is located.
WELCOME_FILE = "config/welcome"

# RULES SYSTEM
### If 1 shows the rules of the talker (contained in the file config/rules, 
### by default), if any available. If 2 shows the rules and enforces users 
### to either accept or decline them (thus quitting them of the talker). To 
### turn off, put 0 instead. 
RULES_SHOW = 2
### The users must write what's below (case insensitive) to accept the rules.
RULES_ACCEPT = "YES"
### The users must write what's below (case insensitive) to decline the rules
### and quit the talker.
RULES_DECLINE = "NO"
### This is the file where the rules are located.
RULES_FILE = "config/rules"

# COMMANDS
### The directory where the command files are located.
COMMANDS_DIR = "commands-en"
### Files in the above directory which are not commands
COMMANDS_EXCEPTIONS = "__init__.py"

# MOTD SCREEN
### If 1 shows the message of the day (contained in the file config/motd, by
### default), if any available. To turn off, put 0 instead.
MOTD_SHOW = 1
### This is the file where the motd is located.
MOTD_FILE = "config/motd"
### This is the file where the news are written.
NEWS_FILE = "config/news"

# USERS
### The directory where the user files are located.
USERS_DIR = "userfiles"

# ROOMS
### The directory where all room files stand.
ROOMS_DIR = "roomfiles"
### The room the users enter when not defined.
DEFAULT_ROOM = "lago"
