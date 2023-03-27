import streamlit as st
import helper as helper
import entities.prompt
import entities.user as usr
import entities.history

# Helper class gets a mongo_db connection and a ChatGPT API Key.
hlp = helper.helper()
user = usr.user(hlp.db_conn)
error = False
login_details = st.empty()
logged_in_details = st.empty()

col_blk1, col_login, col_blk2 = st.columns([1, 2, 1 ])
login = None
logout= None

if not user.is_logged_in():
    with col_login:
        with login_details.container():
            st.header('Login')
            st.subheader('User Details') 
            username = st.text_input('Username', '')
            password = st.text_input('Password', '')    
            new_user = st.checkbox('Create a new user')
            login = st.button('Login')
        
        if login:
            if username.strip() == '':
                st.error('Username cannot be empty')
                error = True
            if password.strip() == '':
                st.error('Password cannot be empty')
                error = True
                
            if not error:
                if not new_user:
                    current_user = user.get_user(username, password)
                    if current_user is not None:
                        st.success('Login Successful')
                        st.session_state.user = current_user
                    else:
                        st.error('Login Failed')
                else:
                    current_user = user.get_user(username)
                    if current_user is not None:
                        st.error('A user called ' + current_user['username'] + ' already exists. Please choose a different username.')
                    else:
                        new_user = user.create_user(username, password)
                        st.success(new_user['username'] + ' created successfully')
                        st.session_state.user = new_user
if user.is_logged_in():
    login_details.empty()
    with logged_in_details.container():
        st.write('You are logged in as ' + st.session_state['user']['username'])
        logout = st.button('Logout')
    
    if logout:
        st.session_state['user'] = None
        logged_in_details.empty()
        
        with login_details.container():
            st.header('Login')
            st.subheader('User Details') 
            username = st.text_input('Username', '')
            password = st.text_input('Password', '')    
            new_user = st.checkbox('Create a new user')
            login = st.button('Login')

