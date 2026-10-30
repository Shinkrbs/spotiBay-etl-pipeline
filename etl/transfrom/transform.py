import pandas as pd

class Transform:
    """
    Transforms extracted data into intended use
    """
    def __init__(self):
        self.user_keys = ["display_name", "email", "country", "account_id"]

    def user_profile(self, user) -> pd.DataFrame:
        """
        Extract important data from current user and transfrom it into a dataframe
        """
        filtered_user = {key: user[key] for key in self.user_keys if key in user}
        return pd.DataFrame([filtered_user])
       
        
