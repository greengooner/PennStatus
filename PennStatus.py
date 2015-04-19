#================================
#PENN STATION STATUS - To determine global train status for New York Penn Station via NJ Transit DepartureVision - By Ramon Carreras - created 2/23/14'
#================================'

#Import libraries to pull DepartureVision page and parse it for status'

import requests
import bs4

def dvpole():
	#Use REQUESTS library to pull DV page for NYP from the web and BS4 to convert to a text file'
	response = requests.get('http://dv.njtransit.com/mobile/tid-mobile.aspx?sid=NY')
	soup = bs4.BeautifulSoup(response.text)
	outxt = soup.get_text()
	cleanoutxt = outxt.encode('utf-8')
	f = open("dvoutxt.txt", "w")
	f.write(cleanoutxt);
	f.close()

def statuscheck():
	#Looking through dvpole output for key words'
	global success
	global fail
	global statentry
	success = 0
	fail = 0
	statentry = 0
	dvtxt = open("dvoutxt.txt","r")
	textfromfile = dvtxt.readlines()
	for status in textfromfile:
		if 'ON TIME' in status:
			success += 1
			statentry += 1
		if 'BOARDING' in status:
			success += 1
			statentry += 1
		if 'ALL ABOARD'in status:
			success += 1
			statentry += 1
		if 'DELAYED' in status:
			fail += 1
			statentry += 1
		if 'CANCELLED' in status:
			fail += 1
			statentry += 1
		if 'STAND BY' in status:
			fail += 1
			statentry += 1
		if 'LATE' in status:
			fail += 1
			statentry += 1
def supermetric():
	#Calculate train status against service terms'
	if success == statentry:
		print 'ALL SYSTEMS GO'
	else:
		if fail >= 3:
			print 'SOME DELAYS, CHECK DEPARTUREVISION AND TRANSIT ALERTS FOR DETAILS'
			print ' '
			print 'TRAINS WITH LATE/DELAYED/STANDBY/CANCELLED STATUS:', fail
			print 'TOTAL TRAINS:', statentry
			
		elif fail >= 9:
			print 'SIGNFICANT DELAYS, CHECK DEPARTUREVISION AND TRANSIT ALERTS FOR DETAILS'
			print ' '
			print 'TRAINS WITH LATE/DELAYED/STANDBY/CANCELLED STATUS:', fail
			print 'TOTAL TRAINS:', statentry
		else:
			print 'ALL SYSTEMS GO, BUT CHECK DEPARTUREVISION AND TRANSIT ALERTS FOR DETAILS'
			print ' '
			print 'TRAINS WITH LATE/DELAYED/STANDBY/CANCELLED STATUS:', fail
			print 'TOTAL TRAINS:', statentry
dvpole()
statuscheck()
supermetric()
