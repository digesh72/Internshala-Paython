# main.py

from cricket_point_calculator import calculate_batting_points, calculate_bowling_points, calculate_fielding_points

players = [
    {'name':'Virat Kohali', 'role':'bat', 'runs':112, '4':10, '6':0, 'ball':119, 'field':0},
    {'name':'du Plessis', 'role':'bat', 'runs':120, '4':11, '6':2, 'ball':112, 'field':0},
    {'name':'Bhuvneshwar Kumar', 'role':'bowl', 'wkts':1, 'overs':10, 'runs':71, 'field':1},
    {'name':'Yuzvendra Chahal', 'role':'bowl', 'wkts':2, 'overs':10, 'runs':45, 'field':0},
    {'name':'Kuldeep Yadav', 'role':'bowl', 'wkts':3, 'overs':10, 'runs':34, 'field':0},
]

top = {'name': None, 'points': -1, 'role': None}

for p in players:
    if p['role'] == 'bat':
        total = calculate_batting_points(p) + calculate_fielding_points(p)
        label = 'batscore'
    else:
        total = calculate_bowling_points(p) + calculate_fielding_points(p)
        label = 'bowlscore'

    print({'name': p['name'], label: total})

    if total > top['points']:
        top = {'name': p['name'], 'points': total, 'role': p['role']}

print("\n🏆 Man of the Match:")
if top['role'] == 'bat':
    print(f"{top['name']} with batting points = {top['points']}")
else:
    print(f"{top['name']} with bowling points = {top['points']}")
