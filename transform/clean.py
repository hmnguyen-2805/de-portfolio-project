import pandas as pd

def clean_roster(data: list) -> pd.DataFrame:
    roster = data['roster']

    players = []

    for player in roster:
        player_id = player['person']['id']
        name = player['person']['fullName']
        position = player['position']['name']

        players.append({
            'player_id': int(player_id),
            'name': str(name),
            'position': str(position)
        })
    
    return pd.DataFrame(players)

def clean_pitching_stats(data: list) -> pd.DataFrame:
    stats = data['stats']
    splits = stats[0]['splits']

    players_stats = []
    
    for split in splits:
        player_id = split['player']['id']
        name = split['player']['fullName']
        era = split['stat']['era']
        strikeouts = split['stat']['strikeOuts']
        innings_pitched = split['stat']['inningsPitched']

        players_stats.append({
            'player_id': int(player_id),
            'name': str(name),
            'era': float(era),
            'strikeouts': int(strikeouts),
            'innings_pitched': float(innings_pitched)
        })

    return pd.DataFrame(players_stats)