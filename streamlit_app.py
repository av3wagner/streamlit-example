import streamlit as st
from streamlit_option_menu import option_menu
from  PIL import Image
import numpy as np
import pandas as pd
import base64
import sys
import inspect, os
from streamlit_text_rating.st_text_rater import st_text_rater

path = os.getcwd()
print(path)
path = "./data/"
print(path)

with st.sidebar:
    choose = option_menu("Main Menu", ["About", "Projects", "Blog","Apps", "Contact"],
                         icons=['house', 'bar-chart-line','file-slides','app-indicator','person lines fill'],
                         menu_icon="list", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#24A608"},
    }
    )

def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)


pdf_file = st.file_uploader("Choose your Resume", type=["pdf"])
#pdf_file = st.file_uploader("Choose your Resume", type=["docx"])
#print(pdf_file.name)
if pdf_file is not None:
    #save_image_path = './assets/'+pdf_file.name
    save_image_path = 'pdf_file.name
    with open(save_image_path, "wb") as f:
        f.write(pdf_file.getbuffer())
    show_pdf(save_image_path)




