import csv, mechanize, urllib2
from bs4 import BeautifulSoup

output = open('output.csv', 'w')
writer = csv.writer(output)

br = mechanize.Browser()
br.open('http://enr.sos.mo.gov/EnrNet/CountyResults.aspx')
#print br.response().read()

#get HTML so I can then target the countyForm via its HTML tags
html = br.response().read()
#transform HTML into a BeautifulSoup object so I can use soup.find on the countyForm
soup = BeautifulSoup(html, "html.parser")
#print soup

br.select_form(nr=0) #nr = get first (only) form on the page

#first dropdown menu:
br.form['ctl00$MainContent$cboElectionNames'] = ['750003566']
#br.submit('ctl00$MainContent$btnElectionType')
#why does the code not work when I have two br.submits?
#used to get this error: 
#File "countyScraper.py", line 21, in <module>
    #br.form['ctl00$MainContent$cboCounty'] = ['001']
    #TypeError: 'NoneType' object does not support item assignment

#second dropdown menu:

county = soup.find('select',
    {'name': 'ctl00$MainContent$cboCounty',
    'id': 'cboCounty'
})

for row in county.find_all('option'):
    countyValue = row['value']

    br.select_form(nr=0)
    br.form['ctl00$MainContent$cboCounty'] = [countyValue] 
    #why don't I need to do this: ['countyValue']
    br.submit('ctl00$MainContent$btnCountyChange')

    html = br.response().read()

    # print html
    soup = BeautifulSoup(html, "html.parser")

    #select the table
    main_table = soup.find('table',
        {'class': 'electtable'} 
    )

    #extract info from table cells
    for row in main_table.find_all('tr'):
        data = [cell.text.encode('utf-8') for cell in row.find_all('td')]
        
    #select candidates of interest:
        for cell in data:
            candidates = ['Hilary Clinton', 'Bernie Sanders', 'Ted Cruz', 'John R. Kasich','Donald J. Trump']
            if cell in candidates:
                
                writer.writerow(row.text)
                #print row.text