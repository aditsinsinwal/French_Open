import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = "/Users/aditsinsinwal/Downloads/atp_matches_2024.csv"  
df = pd.read_csv(file_path)

# Get player input
player_name = input("Enter the player name: ").strip()
player = player_name.lower()

# Filter matches
matches = df[(df['winner_name'].str.lower() == player) | (df['loser_name'].str.lower() == player)].copy()

# Determine outcome
matches['match_result'] = matches.apply(lambda row: 'Win' if row['winner_name'].lower() == player else 'Loss', axis=1)

# Parse sets
def parse_sets(row):
    score = row['score']
    sets = score.split()
    clean = []
    for s in sets:
        s = s.replace('(', '').replace(')', '')
        try:
            p1, p2 = map(int, s.split('-')[:2])
        except:
            continue
        if row['winner_name'].lower() == player:
            clean.append('Won' if p1 > p2 else 'Lost')
        else:
            clean.append('Won' if p2 > p1 else 'Lost')
    return clean

matches['set_results'] = matches.apply(parse_sets, axis=1)

# Prepare stacked bar data
from collections import defaultdict

max_sets = max(len(x) for x in matches['set_results'])
categories = ['Win+Won', 'Win+Lost', 'Loss+Won', 'Loss+Lost']
results_by_set = [defaultdict(int) for _ in range(max_sets)]

for _, row in matches.iterrows():
    for i, set_outcome in enumerate(row['set_results']):
        if i >= len(results_by_set): continue
        match_res = row['match_result']
        key = f"{match_res}+{set_outcome}"
        results_by_set[i][key] += 1

# Normalize to percentages
total_by_set = [sum(counts.values()) for counts in results_by_set]
percent_data = {cat: [] for cat in categories}
for i, counts in enumerate(results_by_set):
    total = total_by_set[i] or 1  # avoid zero division
    for cat in categories:
        percent_data[cat].append(100 * counts.get(cat, 0) / total)

# Plot
labels = [f'Set {i+1}' for i in range(max_sets)]
colors = {
    'Win+Won': 'green',
    'Win+Lost': 'blue',
    'Loss+Won': 'orange',
    'Loss+Lost': 'red'
}

bottom = [0] * max_sets
plt.figure(figsize=(10, 6))
for cat in categories:
    plt.bar(labels, percent_data[cat], label=cat.replace('+', ' / '), bottom=bottom, color=colors[cat])
    bottom = [sum(x) for x in zip(bottom, percent_data[cat])]

plt.ylabel('Percentage of Matches')
plt.title(f"{player_name} – Match & Set Outcome Breakdown by Set")
plt.legend(title="Match Result / Set Result")
plt.grid(axis='y')
plt.tight_layout()
plt.show()
