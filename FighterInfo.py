import requests
from bs4 import BeautifulSoup
import Calculations as cal

# Gets fighter record and returns as dictionary
def get_fighter_info(name):
    wiki_url = "https://en.wikipedia.org/wiki/{}".format(name)
    web_url = requests.get(wiki_url).text
    soup = BeautifulSoup(web_url, "html.parser")

    tables = soup.find_all('table', attrs={'class':'wikitable', 'style':'font-size: 85%;'})
    record_table = tables[0].find_all('tr')
    wins, losses, draws = (0,0,0)

    for row in record_table:
        if ("Win" in str(row.find('td', attrs={'class':'table-yes2'}))):
            wins += 1
        elif ("Loss" in str(row.find('td', attrs={'class':'table-no2'}))):
            losses += 1
        elif ("NC" in str(row.find('td'))):
            draws += 1

    swins, slosses, sdraws = (0,0,0)
    for row in record_table[-5:]:
        if ("Win" in str(row.find('td', attrs={'class':'table-yes2'}))):
            swins += 1
        elif ("Loss" in str(row.find('td', attrs={'class':'table-no2'}))):
            slosses += 1
        elif ("NC" in str(row.find('td'))):
            sdraws += 1

    fighter = {
        "name" : name.replace('_',' '),
        "record" : "{} - {} - {}".format(wins, losses, draws),
        "percent" : cal.calc_percent(wins, losses),
        "streak" : cal.calc_percent(swins, slosses)
    }

    return fighter
