import os
import streamlit as st
from pymongo import MongoClient
import pandas as pd
from bson import ObjectId

class helper:
    
    def __init__(_self):
        """
        Constructor for the helper class.
        Contains helper fuctions for this streamlit application.
        """
        _self.gpt_api_key = st.secrets['chatgpt']['api_key']
        _self.db_conn = _self.mongo_connection()
        
        
    @st.experimental_singleton(suppress_st_warning=True)
    def mongo_connection(_self):
        """
        Creates a connection to the LLM mongo database.
        Returns: A connection to the LLM mongo database.
        """
        user = st.secrets['mongodb']['username']
        pwd = st.secrets['mongodb']['password']
        cluster = st.secrets['mongodb']['cluster']  
        server = st.secrets['mongodb']['server']
        
        connect = 'mongodb+srv://' + user + ':' 
        connect += pwd + '@' + cluster 
        connect += server 
        connect += '?retryWrites=true&w=majority'

        _self.mongo_db = MongoClient(connect)

        return _self.mongo_db
    
    def session_variable_exists(variable):
        """
        Checks if a session variable exists.
        Returns: True if the session variable exists, and contains a value.
        """
        exists = variable in st.session_state
        if not exists:
            return False
        else:
            return st.session_state[variable] is not None
        
