import pandas as pd
from ast import literal_eval


df = pd.read_csv('')
goals_wd_list = []
goals = df['goal'].values
for goal in goals:
    goals_wd_list += literal_eval(goal)
goals_wd_set = set(goals_wd_list)
print(goals_wd_set)


def map_goal():
    
    if any(['Olympics']):
        return "strength"
    if any(['bodybuilding']):
        return "muscle"