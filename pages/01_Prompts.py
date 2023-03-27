import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid
import entities.prompt as pmt
import entities.user as usr
from bson import ObjectId
import helper as helper

def display_prompt_grid(df):
    """
    Display details of prompts from the mongodb database.
    Returns: The currently selected row of the grid.
    """

    builder = GridOptionsBuilder.from_dataframe(df)
    builder.configure_column('owner', hide=True)
    builder.configure_column('_id', hide=True)    
    builder.configure_column(field="name", header_name="Name", width=200)
    builder.configure_column(field="desc", header_name="Description", width=200)   
    builder.configure_column(field="version", header_name="Version", width=90)    
    builder.configure_column(field="max_tokens", header_name="Tokens", width=90)  
    builder.configure_column(field="temperature", header_name="Temperature", width=130)  
    builder.configure_column(field="presence_penalty", header_name="Presence", width=110)
    builder.configure_column(field="frequency_penalty", header_name="Frequency", width=110) 
    builder.configure_column(field="promt_text", header_name="Prompt", width=220)
    builder.configure_column(field="created_on", header_name="Created On", width=130)     
    builder.configure_column(field="owner_name", header_name="Owner", width=130)                  
    builder.configure_selection('single', pre_selected_rows=[0]) 
    go = builder.build()

    return AgGrid(df, gridOptions=go) 

current_user = None
prompt_details = st.empty()
hlp = helper.helper()
user = usr.user(hlp.db_conn)
prompts = pmt.Prompt(hlp.db_conn)
df_prompts = prompts.get_prompts()

if user.is_logged_in():    
        st.subheader('Prompt Details') 
        prompt_row = display_prompt_grid(df_prompts) 
else:
    st.write('You are not logged in. Please login to view the prompts.')

    
