# cricket_points.py

def calculate_batting_points(player):
    points = 0
    runs = player.get('runs', 0)
    balls = player.get('ball', 0)
    fours = player.get('4', 0)
    sixes = player.get('6', 0)

    # 1 point per 2 runs
    points += runs // 2

    # Milestone bonuses
    if runs >= 100:
        points += 10
    elif runs >= 50:
        points += 5

    # Strike rate bonuses
    if balls > 0:
        sr = (runs / balls) * 100
        if 80 <= sr <= 100:
            points += 2
        elif sr > 100:
            points += 6

    # Boundary points
    points += fours * 1 + sixes * 2

    return points

def calculate_bowling_points(player):
    points = 0
    wkts = int(player.get('wkts', 0))
    overs = player.get('overs', 0)
    runs_conceded = player.get('runs', 0)

    # 10 points per wicket
    points += wkts * 10

    # Wicket milestones
    if wkts >= 5:
        points += 10
    elif wkts >= 3:
        points += 5

    # Economy rate bonuses
    if overs > 0:
        econ = runs_conceded / overs
        if 3.5 <= econ <= 4.5:
            points += 4
        elif 2 <= econ < 3.5:
            points += 7
        elif econ < 2:
            points += 10

    return points

def calculate_fielding_points(player):
    return player.get('field', 0) * 10
