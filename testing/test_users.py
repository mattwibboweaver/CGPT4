# Create tests for the user class.
import unittest
import streamlit as st
import entities.user as usr

class Test_Users(unittest.TestCase):
    
    def test_no_user_session(self):
        user = usr.user(None)
        st.session_state['user'] = None
        assert user.is_logged_in() == False
        
        
    def test_user_session_exists(self):
        user = usr.user(None)
        st.session_state['user'] = 'data'
        assert user.is_logged_in() == True  
        

