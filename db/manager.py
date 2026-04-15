from sqlalchemy import create_engine, Engine, inspect
import pandas as pd

class DatabaseManager:

    def __init__(self, db_path: str) -> None:
        self.db_path = db_path
        self.url = self._build_url()
        self.engine = create_engine(self.url)
        print(f'Connected to {self.url}')
        self._table_info()

    def _table_info(self) -> None:
        inspector = inspect(self.engine)
        tables = inspector.get_table_names()
        for table in tables:
            count = pd.read_sql(f'SELECT COUNT(*) as cnt FROM {table}', con=self.engine)
            print(f'Table: {table}. Number of rows: {count['cnt'][0]}')

    def _build_url(self) -> str:
        return f'sqlite:///{self.db_path}'

    def full_load(self, table_name: str, df: pd.DataFrame) -> None:
        df.to_sql(name=table_name, con=self.engine, if_exists='replace', index=False)
        print(f'Full loaded {len(df)} rows to table {table_name}')

    def query(self, sql: str) -> pd.DataFrame:
        try:
            return pd.read_sql(sql=sql, con=self.engine)
        except Exception as e:
            print(f'Error: {e}')
            return pd.DataFrame()

    def append(self, table_name: str, df: pd.DataFrame, id_col: str) -> None:
        df_to_append = self._filter_new_rows(df, id_col, table_name)
        print(f'Deduplicated {len(df) - len(df_to_append)} rows by {id_col}')
        df_to_append.to_sql(name=table_name, con=self.engine, if_exists='append', index=False)
        print(f'Appended {len(df_to_append)} rows to table {table_name}')

    def _get_existing_ids(self, table_name: str, id_col: str) -> set:
        try:
            ids = pd.read_sql(f'SELECT {id_col} FROM {table_name}', con=self.engine)
            return set(ids[id_col].tolist())
        except Exception as e:
            print(f'Error: {e}')
            return set()
    
    def _filter_new_rows(self, df: pd.DataFrame, id_col: str, table_name: str) -> pd.DataFrame:
        return df[~df[id_col].isin(self._get_existing_ids(table_name, id_col))]
    
    def table_info(self) -> None:
        self._table_info()
