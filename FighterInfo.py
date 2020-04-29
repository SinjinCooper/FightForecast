import requests
from bs4 import BeautifulSoup
import Calculations as cal

# input: string of fighters in pairs e.g. "Stipe Miocic, Francis Ngannou;...".
# output: nested list of fighter pairs with underscores between
# first and last names. e.g. [['Stipe_Miocic', 'Francis_Ngannou'],...]
def get_fighters_from_input(names):
    return [[name.replace(' ','_') for name in pairs.split(', ')] for pairs in names.split('; ')]

# input: nested list of fighter name pairs from 'get_fighters_from_input()
# output: nested list of fighter objects (dicts)
def get_fighter_info_from_pairs(list_of_name_pairs):
    # TODO: figure out list comprehension
    list_of_fighter_pairs = []
    for pair in list_of_name_pairs:
        fighters = [get_fighter_info(pair[0]), get_fighter_info(pair[1])]
        list_of_fighter_pairs.append(fighters)
    return list_of_fighter_pairs

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
    # win streak defined by last five fights
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


def display_results(fighter_pair):
    winner = cal.calc_winner(fighter_pair[0], fighter_pair[1])
    streak_winner = cal.calc_streak_winner(fighter_pair[0], fighter_pair[1])
    print("{} will win based on perc ({})".format(winner["name"], winner["percent"]))
    print("{} will win based on perc with streak ({})".format(streak_winner["name"], cal.calc_percent_with_streak(streak_winner)))
