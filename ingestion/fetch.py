import requests

def fetch_roster(team_id: int, season: int) -> list:
    url = f'https://statsapi.mlb.com/api/v1/teams/{team_id}/roster?season={season}'
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()

def fetch_pitching_stats(team_id: int, season: int) -> list:
    url = f'https://statsapi.mlb.com/api/v1/stats?stats=season&group=pitching&teamId={team_id}&season={season}&gameType=R&playerPool=ALL'
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()