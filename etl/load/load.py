import os
from supabase import create_client, Client

class Load:
    def __init__(self):
        self.url: str = os.environ.get("SUPABASE_URL")
        self.key: str = os.environ.get("SUPABASE_SERVICE_KEY")
        self.supabase: Client = create_client(self.url, self.key)
    
    def insert_to_table(self, table_name: str, t_data: list[dict]):
        """
        Load transformed data to supabase database 
        """
        if not t_data:
            print("Data is Empty")
            return
        try:
            response =  (
                self.supabase.table(table_name)
                .upsert(t_data)
                .execute()
            )
            print(f"Loaded {len(response.data)} record(s) into {table_name}")
        except Exception as e:
            print(f"Failed to insert data to {table_name}: {e}")
            raise
