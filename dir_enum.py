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
	print(f"Directory Brute-force @ http://{sys.argv[1]}/ with",ext,"extensions")
	
	for i in dir:
		for x in ext:
			dir_enum = f"http://{sys.argv[1]}/{i}.{x}"
			r = requests.get(dir_enum)
			if r.status_code==404:
				pass
			else:
				print("URL:",dir_enum," -->  Status: ",r.status_code)
