import csv, mechanize
from bs4 import BeautifulSoup

output = open('deseoutput.csv', 'w')
writer = csv.writer(deseoutput)

br = mechanize. Browser()
br.open('http://mcds.dese.mo.gov/guidedinquiry/District%20and%20Building%20Student%20Indicators/District%20Discipline%20Incidents.aspx')
html = br.response().read()

print html

