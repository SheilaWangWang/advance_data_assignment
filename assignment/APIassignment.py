import urllib2, json, urllib

response = urllib2.urlopen('http://openstates.org/api/v1/bills/?apikey=1f366e0712bd4ad6b079afe3bb993434&state=mo&window_search=session&fields=bill_id,sponsors,title,chamber').read()

bills = json.loads(response)

for bill in bills:
    title = (bill['title'])
    sponsors = (bill['sponsors'])
    for sponsor in sponsors:
        name = (sponsor['name'])
        stype = (sponsor['type'])

        output = []
        output.append(title)
        if stype != []:
            if stype in ['primary']:
                output.append(name)
                print output
    