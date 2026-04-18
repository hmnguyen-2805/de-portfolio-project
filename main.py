from dotenv import load_dotenv
from db.manager import DatabaseManager
from ingestion.fetch import fetch_pitching_stats, fetch_roster
from ingestion.load import load_pitching_stats, load_roster
from transform.clean import clean_pitching_stats, clean_roster
import subprocess
import os

def run_dbt(project_dir: str) -> None:
    result = subprocess.run(
        ['dbt', 'build', '--exclude', 'snap_roster'],
        cwd=project_dir,
        capture_output=True,
        text=True
    )
    print(result.stdout)
    if result.returncode != 0:
        print('dbt build failed:')
        print(result.stderr)
        raise RuntimeError('dbt build failed - check output above')
    print('dbt build completed successfully')

def main() -> None:
    load_dotenv()
    db_path = os.getenv('DB_PATH')
    dbt_project_dir = os.getenv('DBT_PROJECT_DIR')
    db = DatabaseManager(db_path)

    raw_roster = fetch_roster(119, 2025)
    roster_df = clean_roster(raw_roster)
    load_roster(roster_df, db)

    raw_pitching_stats = fetch_pitching_stats(119, 2025)
    pitching_stats_df = clean_pitching_stats(raw_pitching_stats)
    load_pitching_stats(pitching_stats_df, db)

    db.table_info()

    run_dbt(dbt_project_dir)

main()