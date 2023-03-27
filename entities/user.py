import streamlit as st

class user:
    
    def __init__(_self, db_conn):
        """
        Constructor for the user class.
        Args:
            db_conn: The database connection.
        """
        _self.db_conn = db_conn
        
    def get_user(_self, username, password=''):
        """
        Gets a user from the database.
        Args:
            username: The username of the user.
            password (optional): The password of the user.
        Returns: The user object if found, None otherwise.
        """
        if _self.is_logged_in():
            return st.session_state['user']
        
        muser = None
        
        if password == '':
            return _self.db_conn.MATTLLM.User.find_one({'username': username})
        else:
            return _self.db_conn.MATTLLM.User.find_one({'username': username, 'password': password})     
        
    def user_exists(_self, username, password):
        user = _self.get_user(username, password)   
        
        if user is not None:
            _self.logged_in_user = user 
        
        return not user == None            
    
    def create_user(_self, username, password=''):
        """
        Creates a new user in the database.
        Args:
            username: The username of the user.
            password: The password of the user.
        """
        user = _self.get_user(username)
        
        if user is None:
            id = _self.db_conn.MATTLLM.User.insert_one({'username': username, 'password': password, 'active': True})
            new_user = _self.db_conn.MATTLLM.User.find_one({'_id': id.inserted_id})
        
        return new_user
        
    def is_logged_in(_self):
        """
        Determines if a user is logged by checking the session state.
        Returns: True if a user is logged in, False otherwise.
        """
        if 'user' in st.session_state:
            return st.session_state['user'] is not None
        else:
            return False
        
        