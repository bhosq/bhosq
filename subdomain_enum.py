import requests
import sys

subd_list = open("wordlist2.txt").read() # Change location/name
subdomains = subd_list.splitlines()

if len(sys.argv) == 1 or len(sys.argv) > 2:
	print("Usage: subdomain_enum.py <DOMAIN>")
	print("Ex: subdomain_enum.py google.com")
else:
	for sub in subdomains:
		sub_domains = f"http://{sub}.{sys.argv[1]}"

		try:
			requests.get(sub_domains)
		
		except requests.ConnectionError:
			pass
		else:
			print("Found! " + sub_domains)
