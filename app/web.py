import requests
from bs4 import BeautifulSoup
from datetime import date


site = 'https://www.worldometers.info/coronavirus/#countries'

get_html = requests.get(site)

parse = BeautifulSoup(get_html.content, 'html.parser')

element = parse.find(id='main_table_countries_today')

#print(element.prettify())

values  = element.findAll('a')
#print(values)

Countries = []

for value in values:
    Countries.append(value.text)
#print(Countries)

numbers = element.findAll("tr", {"style" : ""})

Affected = []

for num in numbers:
    td = num.find('td', {"style" : "font-weight: bold; text-align:right"})
    if td:
        Affected.append(td.text)

#print(Affected)

new_cases= element.findAll('tr', {"style": ""})

New= []

for new_case in new_cases:
    val = new_case.find('td', {"style" : "font-weight: bold; text-align:right;background-color:#FFEEAA;"}) 
    val2 = new_case.find('td', {"style" : "font-weight: bold; text-align:right;"})
    if val:
        New.append(val.text)
    elif val2:
        New.append(val2.text)


#print(New)


today = date.today()



