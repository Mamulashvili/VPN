#imports
import time, random, requests
from selenium import webdriver
from selenium.webdriver.common.proxy import *
from bs4 import BeautifulSoup

site = input("Start page link")
sleep = input("End session after x(seconds): ")
pltim = input ("Time before choosing new proxy: ")
#changing user agents

USER_AGENTS_FILE = './user_agents.txt'
# RUNNING = True

def LoadUserAgents (uafile=USER_AGENTS_FILE):
	uas = []
	with open(uafile, 'rb') as uaf:
		for ua in uaf.readlines():
			if ua:
				uas.append(ua.strip () [1:-1-1])
				print(ua.strip () [1:-1-1])
	random.shuffle(uas)
	# uas.append('Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.9a1) Gecko/20051002 Firefox/1.6a1')
	# uas.append('Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.9a1) Gecko/20060702 SeaMonkey/1.5a')
	# uas.append('Mozilla/5.0 (Linux 2.4.18-18.7.x i686; U) Opera 6.03 [en]')

	uas = LoadUserAgents()

	PROXY = "92.50.155.218:8080" # Free proxy address

	webdriver.DesiredCapabilities.FIREFOX['proxy']={
		"httpProxy":PROXY,
		"ftpProxy":PROXY,
		"sslProxy":PROXY,
			
		"proxyType":"MANUAL",
			
	}
	driver = webdriver.Firefox()

	try:
		driver.get(site)
		# time.sleep(int(sleep))
		# driver.quit()
	except:
		driver.quit()