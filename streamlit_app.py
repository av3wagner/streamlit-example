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

#pdf_file = st.file_uploader("Choose your Resume", type=["pdf"])
pdf_file = "/app/streamlit-example/data/post1-compressed10G.pdf"

logo = Image.open('data/KI3.jpg')
#profile = Image.open('data/KI.jpg')
profile = Image.open('data/AWagner.JPG')

def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

if pdf_file is not None:
    #st.markdown(pdf_file)
    save_image_path = "/app/streamlit-example/data/post1-compressed10G.pdf"
    #save_image_path = pdf_file.name
    with open(save_image_path, "wb") as f:
        col1, col2 = st.columns( [0.1, 0.9])
        with col1:              
             st.markdown(""" <style> .font {
             font-size:20px ; font-family: 'Cooper Black'; color: #FF9633;} 
             </style> """, unsafe_allow_html=True)
             st.markdown('<p class="font"> </p>', unsafe_allow_html=True)
        with col2:  
            st.title("Dr. Alexander Wagner, Berlin")
            st.markdown("")
            #st.image(logo, width=130 )
            st.image(profile, width=400 )
             st.markdown(""" <style> .font {
             font-size:14px ; font-family: 'Cooper Black'; color: #FF9633;} 
             </style> """, unsafe_allow_html=True)
             st.markdown('<p class="font">Фото: Мюнхен, 2010</p>', unsafe_allow_html=True)
             st.markdown("")
             st.write("Дорогие одноклассники! Вашему вниманию предлагаются воспоминания выпускников сш. им В.И.Ленина 1968 года. Это первая редакция сборника, так называемы сигнальный вариан. Авторы продолжают работать дальше и расширять сборник. В скором времени он будет предложен вам для прочтения. Желаем вам приятного чтения!")    
             #show_pdf(save_image_path)
             show_pdf("post1-compressed10G.pdf")

# We create our Streamlit App
def main():
    logo = Image.open('KI3.jpg')
    profile = Image.open('KI.jpg')

    with st.sidebar:
        choose = option_menu("App Gallery", ["About", "Photo Editing", "Project Planning", "Python e-Course", "Contact"],
                             icons=['house', 'camera fill', 'kanban', 'book','person lines fill'],
                             menu_icon="app-indicator", default_index=0,
                             styles={
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }
        )
   
#if __name__ == '__main__':
#    main()

