from dotenv import load_dotenv
from db.manager import DatabaseManager
from ingestion.fetch import fetch_pitching_stats, fetch_roster
from ingestion.load import load_pitching_stats, load_roster
from transform.clean import clean_pitching_stats, clean_roster
from pipeline_logger import get_logger
import subprocess
import os

logger = get_logger(__name__)

def run_dbt(project_dir: str) -> None:
    result = subprocess.run(
        ['dbt', 'build', '--exclude', 'snap_roster'],
        cwd=project_dir,
        capture_output=True,
        text=True
    )
    logger.info(result.stdout)
    if result.returncode != 0:
        logger.error('dbt build failed:')
        logger.error(result.stderr)
        raise RuntimeError('dbt build failed - check output above')
    logger.info('dbt build completed successfully')

def main() -> None:
    logger.info('Pipeline started')

    load_dotenv()
    db_path = os.getenv('DB_PATH')
    dbt_project_dir = os.getenv('DBT_PROJECT_DIR')
    logger.info('Environment variables loaded')

    db = DatabaseManager(db_path)

    raw_roster = fetch_roster(119, 2025)
    roster_df = clean_roster(raw_roster)
    load_roster(roster_df, db)

    raw_pitching_stats = fetch_pitching_stats(119, 2025)
    pitching_stats_df = clean_pitching_stats(raw_pitching_stats)
    load_pitching_stats(pitching_stats_df, db)

    db.table_info()

    logger.info('Running dbt build...')
    run_dbt(dbt_project_dir)
    logger.info('Pipeline completed successfully')

main()