from db.manager import DatabaseManager
import pandas as pd

def load_roster(df: pd.DataFrame, db: DatabaseManager) -> None:
    db.full_load('roster', df)

def load_pitching_stats(df: pd.DataFrame, db: DatabaseManager) -> None:
    db.append('pitching_stats', df, 'player_id')