#!/usr/bin/env python
#-*- coding: utf-8 -*-
import json
import arrow
import requests
from time import sleep

import mysql.connector
from datetime import time, date, timedelta, datetime
import sys
import os, time

from slackclient import SlackClient
import socket
#Disabling warings
import requests
import urllib3
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from traceback import print_exc
from time import sleep, tzset
import math
from math import ceil
from math import floor
import re
import json
import multiprocessing
import requests
from threading import Thread

from requests.auth import HTTPBasicAuth


#S_TOKEN = "xoxp-12755663922-12785724403-62714997894-68a85cd7c8"
S_TOKEN  = "xoxp-206336576021-206236641970-207217348070-d482449e31ceda18e09d0eba217ad2b5"
notifications_channel = "C62BXU6SE"

def s_print (s_text, print_type = "n"):
	#This channel is for test channel
	s_channel_t = "C3NR5R63T"
	#This channel is for simple notifications
	s_channel_n = notifications_channel
	s_channel = s_channel_n
	#This channels is for alarms, that require an immediate action
	s_channel_a =  "C3LL39BQA"
	if print_type == "a": s_channel = s_channel_a
	elif print_type == "n": s_channel = s_channel_n
	elif print_type == "t": s_channel = s_channel_t
	
	elif len (print_type) > 0 or not print_type: 
		print ("A wrong parameter for s_print. Please check. Should be ""n"" or ""a""")
		print ("Proseed without brack as with ""n""") 
		s_channel = s_channel_n
	
	sc = SlackClient(S_TOKEN)
	try:
		#it is an array
		if not(isinstance(s_text, basestring) ):
			for a in s_text:
				a = str(a)
				print ("slack->" + a)
				response = sc.api_call(
					"chat.postMessage", channel=s_channel, text=a,
					username='pybot', icon_emoji=':robot_face:'
					)
		#it is one valua
		else:
			try:
				print ("converting s_text to string...:")
				s_text = str(s_text)
				print ("Succesfully converted")
			except:
				print ("could not convert s_text to string. Continuing as is....")
				pass
			print ("slack->" + s_text)
			response = sc.api_call(
				"chat.postMessage", channel=s_channel, text=s_text,
				username='pybot', icon_emoji=':robot_face:'
				)
	except:
		s_text = ("%s: Have problems to print the text to slack. Check the variable to print.  : " % (sys.argv [0], sys.exc_info()))
		print ("slack->" + s_text)
		try:
			sc.api_call(
				"chat.postMessage", channel=s_channel, text=s_text,
				username='pybot', icon_emoji=':robot_face:'
				)
		except:pass
	try: response = json.loads(json.dumps(response))["ok"]
	except: response = False
	return response

def t_print (t_text, print_type= "t"):
	s_print (t_text, print_type)
