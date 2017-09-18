#!/usr/bin/python
##
###


import urllib2
import prettytable
import json
import prettytable
import optparse
import time
import os


done = 0
key = ""
rrate = 30
url = "https://www.miningpool.co/api/balances?key="


color_green = '\033[92m'
color_red = '\033[91m'
color_off = '\033[0m'


def miningpool_co():
	while done == 0:
		try:
			os.system("clear")
			print "############################### "+color_green+" miningpool.co - user stats "+color_off+" ################################"
			x = prettytable.PrettyTable(["Name", "shortname", "wc", "estimate_raw", "active", "balance", "hashrate"])
			x.align["Name"] = "l"
			response = urllib2.urlopen(url+key)
			data = json.load(response)   
			dataval = data.values()
			dataval = dataval[2]
			for da in dataval:
				x.add_row([da["name"], da["short_code"], da["worker_count"], da["estimate_raw"], da["active"], da["balance"], da["hashrate"]])
			print "using API KEY: \t\t"+color_red+key+color_off+"\n"
			print x
			print "\nrefreshing every "+str(rrate)+" seconds..."
			time.sleep(rrate)
			print "refreshing ..."
		except IOError:
	                pass


if __name__=="__main__":
#	parser = optparse.OptionParser(usage)
	parser = optparse.OptionParser("Usage: %prog -k 048ma8110kla919ka8k10al91ka -r 60")
	parser.add_option("-k", "--key", dest="key", default="", type="string", help="Your miningpool.co API Key")
	parser.add_option("-r", "--refreshrate", dest="rrate", default=30, type="int", help="Refreshrate in seconds")
	(options, args) = parser.parse_args()
	if len(options.key) <= 0:
		parser.error("Incorrect number of arguments")
	key = options.key
	rrate = options.rrate
	miningpool_co()
