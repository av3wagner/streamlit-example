#Hurra, es läuft! 09.01.2023
import streamlit as st
#from streamlit_option_menu import option_menu
from  PIL import Image
import numpy as np
import pandas as pd
import base64
import sys
import inspect, os
#from streamlit_text_rating.st_text_rater import st_text_rater

path = os.getcwd()
#print(path)
#st.markdown(path)
#/app/streamlit-example

pdf_file=os.path.join(path, "", "data", "post1-compressed10G.pdf")
#path = "./data/"
#st.markdown(pdf_file)
#/app/streamlit-example/data/post1-compressed10G.pdf

 #st.sidebar.image('./data/KI3.jpg')
 st.sidebar.title("Navigation")
 #options = st.sidebar.radio("Go to",['Home','Global Situation', 'Situation by WHO Region', 'Situation in the United States'], key='1')
 st.sidebar.markdown("")
 st.sidebar.image('https://media.giphy.com/media/dVuyBgq2z5gVBkFtDc/giphy.gif')

def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

#pdf_file = st.file_uploader("Choose your Resume", type=["pdf"])
pdf_file = "/app/streamlit-example/data/post1-compressed10G.pdf"
if pdf_file is not None:
    #st.markdown(pdf_file)
    save_image_path = "/app/streamlit-example/data/post1-compressed10G.pdf"
    #save_image_path = pdf_file.name
    with open(save_image_path, "wb") as f:
        #st.markdown("Добрый день дорогие одноклассники!")
        #f.write(pdf_file.getbuffer())
    #show_pdf(save_image_path)
    show_pdf("post1-compressed10G.pdf")




