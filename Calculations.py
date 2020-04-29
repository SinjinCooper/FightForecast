
# predicts winner by record
def calc_winner(fighter_a, fighter_b):
    return fighter_a if fighter_a["percent"] > fighter_b["percent"] else fighter_b

# predicts winner by streak record
def calc_streak_winner(fighter_a, fighter_b):
    return fighter_a if calc_percent_with_streak(fighter_a) > calc_percent_with_streak(fighter_b) else fighter_b

# returns win rate (wins/losses)
def calc_percent(wins, losses):
    return 100 if losses == 0 else round((wins / (wins + losses)) * 100)

# returns weighted win rate streak
def calc_percent_with_streak(fighter):
    return (fighter["percent"] + fighter["streak"]) / 2