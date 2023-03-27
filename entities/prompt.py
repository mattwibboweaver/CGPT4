import streamlit as st
import pandas as pd
from bson import ObjectId

class Prompt:
    def __init__(_self, db_conn):
        """
        Constructor for the Prompt class.
        Args:
            db_conn: The database connection.
        """
        _self.db_conn = db_conn

      
    def get_prompts(_self):
        """
        Gets the prompt documents from the LLM mongo database.
        Args:
            _self: The class instance.
        Returns: A dataframe containing the prompt documents.
        """
        db = _self.db_conn.MATTLLM 
        items = db.Prompt.find()
        items = list(items)        
        df_prompts = pd.DataFrame(items)
        
        df_prompts._id = df_prompts._id.astype(str)
        df_prompts['owner'] = df_prompts['owner'].astype(str)
        df_prompts['owner_name'] = df_prompts['owner']
        
        for index, row in df_prompts.iterrows():
            obj_id = ObjectId(row['owner'])
            user = _self.db_conn.MATTLLM.User.find_one({'_id': obj_id})
            df_prompts.at[index, 'owner_name'] = user['fullname']
        
        st.session_state['prompts'] = df_prompts
        return df_prompts    