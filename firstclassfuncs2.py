#@first-class functions
#@coreySchafer/YouTube

import random
import sys
import os

def logger (msg):

	def log_message():
		print('Log:',msg)

	return log_message

log_hi = logger('Hi!')
log_hi()



