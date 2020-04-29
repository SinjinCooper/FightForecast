import FighterInfo as fi
import Calculations as cal

# Edit instructions to add semicolon update
print("Welcome to my MMA prediction machine!\n"
    + "Please enter two fighter names separated by a comma and space "
    + "(e.g. \"Tony Ferguson, Khabib Nurmogamedov\")")

names = input()
list_of_name_pairs = fi.get_fighters_from_input(names)
list_of_fighter_pairs = fi.get_fighter_info_from_pairs(list_of_name_pairs)

#do calculations and print results
for pair in list_of_fighter_pairs:
    fi.display_results(pair)
