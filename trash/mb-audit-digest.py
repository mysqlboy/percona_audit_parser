#!/usr/bin/python
# python script for analysis of percona-audit logs

import json
import sys
from StringIO import StringIO
# import optparse

audit_file = './audit.log'
y=[]
# 	

def process_line():
	data = open(audit_file, 'r')
	for i in data:
		y = json.dumps(i)
		x = json.loads(y)
		print x

process_line()

