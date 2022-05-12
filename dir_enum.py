#!/usr/bin/python3

import requests
import sys

dir_list = open("dir_wordlist.txt").read() # Change directory wordlist name/location
dir = dir_list.splitlines()

ext_list = open("ext_wordlist.txt").read() # Change extensions wordlist name/location
ext = ext_list.splitlines()

if len(sys.argv) == 1 or len(sys.argv) > 2:
	print("Usage: dir_enum.py <URL>")
else:
	if "http://" in sys.argv[1]: 
		print(f"Directory Brute-force @ {sys.argv[1]}/ with",", ".join(ext),"extensions")
		dir_enum = sys.argv[1] + "/{}.{}"
	elif "https://" in sys.argv[1]:
		print(f"Directory Brute-force @ {sys.argv[1]}/ with",", ".join(ext),"extensions")
		dir_enum = sys.argv[1] + "/{}.{}"
	else:	
		dir_enum = "http://" + sys.argv[1] + "/{}.{}"
		print(f"Directory Brute-force @ http://{sys.argv[1]}/ with",", ".join(ext),"extensions")
	for i in dir:
		for x in ext:
			r = requests.get(dir_enum.format(i,x))
			if r.status_code==404:
				pass
			else:
					print("URL:",dir_enum.format(i,x)," -->  Status: ",r.status_code)
