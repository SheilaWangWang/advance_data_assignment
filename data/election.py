import csv, mechanize
from bs4 import BeautifulSoup

electionoutput = open('electionoutput.csv','w')
writer = csv.writer(electionoutput)

br = mechanize.Browser()
br.open('http://enr.sos.mo.gov/EnrNet/')

br.select_form(nr=0)

