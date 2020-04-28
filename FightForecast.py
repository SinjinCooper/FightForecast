import FighterInfo as fi
import Calculations as cal

print("Welcome to my MMA prediction machine!\n"
    + "Please enter two fighter names separated by a comma and space "
    + "(e.g. \"Tony Ferguson, Khabib Nurmogamedov\")")
names = input()
fighters = [f.replace(' ','_') for f in names.split(', ')]

fighter_a = fi.get_fighter_info(fighters[0])
fighter_b = fi.get_fighter_info(fighters[1])

winner = cal.calc_winner(fighter_a, fighter_b)

streak_winner = cal.calc_streak_winner(fighter_a, fighter_b)

print("{} will win base of perc ({})".format(winner["name"], winner["percent"]))
print("{} will win based of perc with streak ({})".format(streak_winner["name"], cal.calc_percent_with_streak(streak_winner)))