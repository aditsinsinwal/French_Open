import numpy as np 
import pandas as pd

file_path = "/Users/aditsinsinwal/Downloads/atp_matches_2024.csv"

#Load the dataset
df = pd.read_csv(file_path)

# Prompt user for a player name
player_name = input("Enter the player name (e.g., Carlos Alcaraz): ").strip()

# Filter matches where the player is either the winner or the loser
player_matches = df[(df['winner_name'].str.lower() == player_name.lower()) |
                    (df['loser_name'].str.lower() == player_name.lower())]

# Check if any matches found
if not player_matches.empty:
    print(f"\nFound {len(player_matches)} matches for {player_name}:\n")
    print(player_matches[['tourney_name', 'round', 'winner_name', 'loser_name', 'score', 'surface', 'tourney_date']])
else:
    print(f"\nNo matches found for '{player_name}'. Check spelling or try a different name.")
