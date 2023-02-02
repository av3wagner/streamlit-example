#Hurra, es läuft! 09.01.2023
#Hurra, es läuft! 09.01.2023
import streamlit as st
#from streamlit_option_menu import option_menu
from  PIL import Image
import numpy as np
import pandas as pd
import base64
import sys
import inspect, os

import streamlit.components.v1 as components
#import plotly.express as px
#from streamlit_timeline import timeline
#import plotly.graph_objects as go
#import seaborn as sns
#import plotly.figure_factory as ff

options = "Home"
path = os.getcwd()
#st.markdown(path)
#/app/streamlit-example

profile  = Image.open('data/AWagner.JPG')
profile2 = Image.open('AWprofil.jpg')
AWbrigade = Image.open('AWbrigade.jpg')
logo = Image.open('data/KI3.jpg')
be1 = Image.open('AutoitGuiBericht.jpg')
be2 = Image.open('AutoitGui2.jpg')
be3 = Image.open('AutoitGui4.jpg')
be4 = Image.open('AutoitGui5.jpg')

def show_pdf(file_path):
    col1, col2 = st.columns( [1, 9])
    with col1:              
        #st.title("Dr. Alexander Wagner, Berlin")
        st.markdown("")
        st.image(logo, width=100 )
        st.markdown("")
   
    with col2:  
        st.title('Visualisierung des Berichts in PDF-Form')
        #st.subheader('A simple app that shows different image processing algorithms. You can choose the options'
        #     + ' from the left. I have implemented only a few to show how it works on Streamlit. ' + 
        #     'You are free to add stuff to this app.')
        st.markdown("")
        with open(file_path,"rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="1000" height="1000" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

def read_markdown_file0(markdown_file):
    intro_markdown = Path(markdown_file).read_text()
    st.markdown(intro_markdown, unsafe_allow_html=True)

def read_markdown_file(markdown_file):
    with open(markdown_file, 'r') as fp:
        w = fp.read()
    return w    

def main():
    st.set_page_config(layout="wide")
    selected_box = st.sidebar.selectbox(
    'Bitte wählen Sie eine Funktion', ('Über uns', 'Einführung', 'Bericht Visualisierung', 'Hoch- Runterladen der Dateien', 'Beispiel 18 Modellen'))
    
    if selected_box == 'Über uns':
        welcome() 
    if selected_box == 'Bericht Visualisierung':
        show_pdf("KSFE2023.pdf")
    if selected_box == 'Einführung':
        Einführung()
    if selected_box == 'Hoch- Runterladen der Dateien':
        laden()
    if selected_box == 'Beispiel 18 Modellen':
        BeModellen()               

def welcome():
    col1, col2, col3 = st.columns( [1, 8, 1])
      
    with col1:              
        st.markdown("")
        #st.image(logo, width=100 )
        #st.markdown("")
    with col2:  
        st.title("Prof. Dr. Dirk Schieborn, Dipl. Math., Professor für Mathematik, Data Science und Statistik an der ESB Business School der Hochschule Reutlingen")
        st.header("Leiter Steinbeis Transferzentrum Data Analytics und Predictive Modelling")
        st.markdown("")
        
        st.title("Dr. Alexander Wagner, Berlin")
        st.markdown("")
        st.markdown("")
        st.image(profile, width=400 )
        st.markdown(""" <style> .font {font-size:16px ; font-family: 'Cooper Black'; color: #FF9633;} </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">MSD SHARP & DOHME GMBH: Alexander Wagner. Мюнхен, 2010</p>', unsafe_allow_html=True)
        st.markdown("")
        
        st.image(AWbrigade, width=400 )
        new_title = '<p style="font-family:sans-serif; color:Black; font-size: 14px;">Baustelle: Alexander Wagner 4. von links. Almaty, April 1973</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        st.markdown("")
                
        intro_markdown = read_markdown_file("DrWagner.md")
        st.markdown(intro_markdown, unsafe_allow_html=True)
        
    with col3:              
        st.markdown(""" <style> .font {
        font-size:10px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font"> </p>', unsafe_allow_html=True)

    
def Einführung():    
    st.title('System GUI für Administrator und Anwender')
    st.write('''
    System GUI ist ein Zentrall-Kern des Web- und Cloudbasiertes Multiple-Kernel Eco-System für die automatisierte Erstellung des Analytischen-Berichten.

    Mit Hilfe von Steuerelementen des System GUI werwalten der Administratorr und die Anwender das ganze Prozess von Entwicklung und Visualisierung des 
    analytischen Berichtes bis zu Start des Streamlit WEB-Apps auf Cloud-Plattform.

    Alles passiert auf GUI-Fenster, der Administratot bzw. die Anwender können schell und unproblematisch das System bedinnen und benutzen.
    

    Das System-Gui und die Komponenten wurde mit Hilfe von AutoIt entwickelt und hat andere Software-Kerne in ein System integriert.
    Dazu gehören: SAS, Python, Microsoft Office, etc.

    ''')
    
    col1,col2 = st.columns((4,1))
    with col1:  
        st.header("Berichts-Visialisirubg als Word-Dokument auf System-GUI")
        st.markdown("")
        st.image(be1, width=800 )
        st.markdown("")
        
        st.header("Visialisirubg der Streamlit App in GitHub auf System-GUI")
        st.markdown("")
        st.image(be2, width=800 )
        st.markdown("")  
        
        st.header("Start WEB-App auf Cloud-Plattform und Visualisierung auf System-GUI")
        st.markdown("")
        st.image(be3, width=800 )
        st.markdown("")    
        
        st.header("Schematische Darstellung des Anwendungsbetriebs in Web-Plattformen")
        st.markdown("")
        st.image(be4, width=800 )
        st.markdown("")  
        
#def file_selector(folder_path='.'):
def file_selector(folder_path=path):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)

def laden():    
    st.title('Hoch- bzw. Runterladen der Dateien')
    st.write('''
    Die Personen mit gültigen Zugrifsrechten dürfen des System-Dateien jederzeit Hoch- bzw. Runterladen.

    Danach könnten die Anwender bei Bedarf das Bericht lokal auf anwender-PC in MS Word Form korriegieren, konwertieren (in: PDF, HTML) und auf GitHub zurückspeichern.
   
    ''')
    
    col1,col2 = st.columns((4,1))
    with col1:  
        st.header("Runterladen des Word-Dokuments auf lokal-PC")
        st.markdown("")          
        filename = file_selector(folder_path=path)
        st.write("path: ", path)
        st.write('You selected `%s`' % filename)
                
        outfilename=str(path + "\Selected.docx")
        st.write(outfilename)                        
             
        data = open(filename, "rb").read()
        encoded = base64.b64encode(data)
        decoded = base64.b64decode(encoded)
        st.download_button('Download Here', decoded, outfilename) 
        
        st.header("Hochladen des Word-Dokuments vom lokal-PC auf GitHub")
        st.markdown("")  
        
def BeModellen():        
    st.header("Beispiel: 18 Maschinen Lernen Modellen")
    HtmlFile = open("A++Nostalgi08.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, width=1800, height=2000, scrolling=True)

        
if __name__ == "__main__":
    main()
