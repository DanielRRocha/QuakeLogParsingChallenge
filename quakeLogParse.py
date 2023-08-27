# quakeLogParse.py
import re
from collections import defaultdict

# URL of the quake.log file
log_url = "https://gist.githubusercontent.com/cloudwalk-tests/be1b636e58abff14088c8b5309f575d8/raw/df6ef4a9c0b326ce3760233ef24ae8bfa8e33940/qgames.log"

# Regular expression patterns
player_kill_pattern = re.compile(r'Kill: \d+ \d+ \d+: (.+?) killed (.+?) by (.+)')
game_start_pattern = re.compile(r'InitGame:')
game_end_pattern = re.compile(r'ShutdownGame:')

# Data storage
game_stats = defaultdict(lambda: {"total_kills": 0, "players": [], "kills": defaultdict(int), "kills_by_means": defaultdict(int)})
current_game = None

# Read the log file
import urllib.request
with urllib.request.urlopen(log_url) as f:
    for line in f:
        line = line.decode('utf-8').strip()
        player_kill_match = player_kill_pattern.search(line)
        game_start_match = game_start_pattern.search(line)
        game_end_match = game_end_pattern.search(line)
        
        if game_start_match:
            if current_game:
                game_stats[current_game]["players"] = list(set(game_stats[current_game]["players"]))
            current_game = len(game_stats) + 1
        elif game_end_match:
            current_game = None
        elif player_kill_match and current_game is not None:
            killer = player_kill_match.group(1)
            victim = player_kill_match.group(2)
            means_of_death = player_kill_match.group(3)
            
            game_stats[current_game]["total_kills"] += 1
            if killer != "<world>":
                game_stats[current_game]["kills"][killer] += 1
            if killer != "<world>" and killer not in game_stats[current_game]["players"]:
                game_stats[current_game]["players"].append(killer)
            if victim not in game_stats[current_game]["players"]:
                game_stats[current_game]["players"].append(victim)
            
            if means_of_death.startswith("MOD_"):
                game_stats[current_game]["kills_by_means"][means_of_death] += 1

# Print statistics per game
for game, stats in game_stats.items():
    total_kills = stats["total_kills"]
    players = stats["players"]
    kills = stats["kills"]
    kills_by_means = stats["kills_by_means"]
    
    print(f'"{game}": {{')
    print(f'  "total_kills": {total_kills},')
    print(f'  "players": {players},')
    print('  "kills": {')
    for player, kill_count in kills.items():
        print(f'    "{player}": {kill_count},')
    print('  },')
    print('  "kills_by_means": {')
    for means, count in kills_by_means.items():
        print(f'    "{means}": {count},')
    print('  }')
    print('},')
