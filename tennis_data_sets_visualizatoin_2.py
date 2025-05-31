import pandas as pd
import matplotlib.pyplot as plt

# === FILE AND PLAYER NAME SETUP ===
file_path = "/Users/aditsinsinwal/Downloads/atp_matches_2024.csv"  
df = pd.read_csv(file_path)

player_name = input("Enter player name: ").strip()
player = player_name.lower()

# === FILTER MATCHES ===
matches = df[(df['winner_name'].str.lower() == player) | (df['loser_name'].str.lower() == player)].copy()
matches['match_result'] = matches.apply(lambda row: 'Win' if row['winner_name'].lower() == player else 'Loss', axis=1)
matches['match_date'] = pd.to_datetime(matches['tourney_date'], format='%Y%m%d')

# === Aces vs Double Faults ===
plt.figure()
plt.scatter(matches['w_ace'], matches['w_df'], label='Wins', c='green', alpha=0.6)
plt.scatter(matches['l_ace'], matches['l_df'], label='Losses', c='red', alpha=0.6)
plt.xlabel('Aces')
plt.ylabel('Double Faults')
plt.title(f'{player_name} – Aces vs Double Faults')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# === Match Duration by Surface ===
surface_durations = matches.groupby('surface')['minutes'].mean().dropna()
surface_durations.plot(kind='bar', color='orange', edgecolor='black')
plt.title(f"{player_name} – Avg Match Duration by Surface")
plt.ylabel("Minutes")
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# === Win Rate by Round ===
round_summary = matches.groupby(['round', 'match_result']).size().unstack().fillna(0)
round_summary['Win Rate %'] = 100 * round_summary['Win'] / round_summary.sum(axis=1)
round_summary['Win Rate %'].sort_values(ascending=False).plot(kind='bar', color='skyblue')
plt.title(f"{player_name} – Win Rate by Round")
plt.ylabel("Win Rate (%)")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# === 1st vs 2nd Serve Points Won ===
plt.figure()
plt.scatter(matches['w_1stWon'], matches['w_2ndWon'], c='blue', alpha=0.6, label='Wins')
plt.scatter(matches['l_1stWon'], matches['l_2ndWon'], c='red', alpha=0.6, label='Losses')
plt.xlabel("1st Serve Points Won")
plt.ylabel("2nd Serve Points Won")
plt.title(f"{player_name} – Serve Performance")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# === Top 10 Tournaments by Wins ===
tourney_wins = matches[matches['match_result'] == 'Win']['tourney_name'].value_counts().head(10)
tourney_wins.plot(kind='barh', color='green', edgecolor='black')
plt.title(f"{player_name} – Top 10 Tournaments by Wins")
plt.xlabel("Number of Wins")
plt.gca().invert_yaxis()
plt.grid(axis='x')
plt.tight_layout()
plt.show()

# === Ranking Over Time ===
rank_timeseries = matches[['match_date', 'match_result', 'winner_rank', 'loser_rank']].copy()
rank_timeseries['player_rank'] = rank_timeseries.apply(
    lambda row: row['winner_rank'] if row['match_result'] == 'Win' else row['loser_rank'], axis=1
)
rank_timeseries = rank_timeseries.sort_values('match_date')
plt.figure(figsize=(10, 4))
plt.plot(rank_timeseries['match_date'], rank_timeseries['player_rank'], marker='o', linestyle='-')
plt.gca().invert_yaxis()
plt.title(f"{player_name} – Ranking Progression (2024)")
plt.ylabel("ATP Rank (Lower is Better)")
plt.xlabel("Match Date")
plt.grid(True)
plt.tight_layout()
plt.show()

# === Opponent Ranking Histogram (Win vs Loss) ===
won_ranks = matches[matches['match_result'] == 'Win']['loser_rank'].dropna()
lost_ranks = matches[matches['match_result'] == 'Loss']['winner_rank'].dropna()
plt.figure(figsize=(10, 5))
plt.hist(won_ranks, bins=20, alpha=0.6, label='Beaten Opponents', color='green', edgecolor='black')
plt.hist(lost_ranks, bins=20, alpha=0.6, label='Lost To', color='red', edgecolor='black')
plt.xlabel("Opponent ATP Ranking")
plt.ylabel("Number of Matches")
plt.title(f"{player_name} – Opponent Rankings (Win vs Loss)")
plt.legend()
plt.grid(axis='y')
plt.tight_layout()
plt.show()
