import csv, mechanize
from bs4 import BeautifulSoup

# Get the output file ready
# datafile = open('output.csv', 'w')
# writer = csv.writer(datafile)

br = mechanize.Browser()
br.open('http://enr.sos.mo.gov/EnrNet/CountyResults.aspx')

html = br.response().read()
soup = BeautifulSoup(html, "html.parser")

county_dropdown = soup.find('select',
    {'name':'ctl00$MainContent$cboCounty',
    'id': 'cboCounty'
})

county_values = county_dropdown.find_all('option')

for county in county_values:
    county_name = county.text
    county_id = county['value']

    # Submit form
    br.select_form(nr=0)
    br.form['ctl00$MainContent$cboElectionNames'] = ['750003566']
    br.form['ctl00$MainContent$cboCounty'] = [county_id]
    br.submit('ctl00$MainContent$btnCountyChange')

    html = br.response().read()

    soup = BeautifulSoup(html, "html.parser")

    main_table = soup.find('table',
        {'id': 'MainContent_dgrdResults'
    })

    output = []
    output.append(county_name)

    # Now get the data from each table row
    for row in main_table.find_all('tr'):
        data = [cell.text for cell in row.find_all('td')]

        if data != []:
            if data[0] in ['Hillary Clinton', 'Bernie Sanders', 'Ted Cruz', 'John R. Kasich', 'Donald J. Trump']:
                output.append(data[3]) # This is the vote percentage

    print output