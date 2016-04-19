import urllib2, csv
import mechanize
from bs4 import BeautifulSoup

output = open('result.csv', 'w')
writer = csv.writer(output)

br = mechanize.Browser()
br.open('http://enr.sos.mo.gov/EnrNet/CountyResults.aspx')


br.select_form(nr=0)
br.form['ctl00$MainContent$cboElectionNames'] = ['750003566']

html = br.response().read()

soup = BeautifulSoup(html, 'html.parser')

county = soup.find('select',
    {'name':'ctl00$MainContent$cboCounty',
    'id': 'cboCounty'})

for row in county.find_all('option'):
    countyvalue = row['value']
    br.select_form(nr=0)
    br.form['ctl00$MainContent$cboCounty'] = [countyvalue] 

    br.submit('ctl00$MainContent$btnCountyChange')
    
    html = br.response().read()

    # print html
    soup = BeautifulSoup(html, "html.parser")

    main_table = soup.find('table',
        {'class': 'electtable'} 
    )
    #create an output list and put the values we care about into the list
    #a blank list first to hold our result
    output = []
    output.append(county.text)
    #get the data from each table row
    #for every row in the table do sth
    #find grabs everything between tr or td tags
    for row in main_table.find_all('tr'):
        data = [cell.text for cell in row.find_all('td')]
        # if the lsit is not empty then execute the code(ignore the empty list)
        if data != []:
            if data[0] in ['Hillary Clinton', 'Bernie Sanders','Ted Cruz','John R. Kasich', 'Donald J. Trump']:
                output.append(data[3])
writer.writerow(output)