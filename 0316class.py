import csv, mechanize
from bs4 import BeautifulSoup

output = open('output.csv', 'w')
writer = csv.writer(output)

br = mechanize. Browser()
br.open('https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500')
html = br.response().read()


soup = BeautifulSoup(html, 'html.parser')

main_table = soup.find('table',
    {'align': 'center',
    'class': ['collapse','shadow', 'BCSDTable']
    })

for row in main_table.find_all('tr'):
    data = [cell.text for cell in row.find_all('td')]
    writer.writerow(data)



br.select_form(nr=0)
br.form['ctl00$MainContent$cboElectionNames'] = ['750003566']
br.submit('ctl00$MainContent$btnCountyChange')

br.submit('ctl00$MainContent$btnCountyChange')
main_table = soup.find('select',
    {'name': 'ctl00$MainContent$cboCounty',
    'id': 'cboCounty'})

for row in main_table.find_all('option'):
    data = []
    print(row)