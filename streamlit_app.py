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
            st.markdown(""" <style> .font {font-size:16px ; font-family: 'Cooper Black'; color: #FF9633;} </style> """, unsafe_allow_html=True)
            st.markdown('<p class="font">Фото: Мюнхен, MSD SHARP & DOHME GMBH, 2010</p>', unsafe_allow_html=True)
            st.markdown("")
            #st.write("Дорогие одноклассники! Вашему вниманию предлагаются воспоминания выпускников сш. им В.И.Ленина 1968 года. Это первая редакция сборника, так называемы сигнальный вариан. Авторы продолжают работать дальше и расширять сборник. В скором времени он будет предложен вам для прочтения. Желаем вам приятного чтения!")    
            #show_pdf(save_image_path)
            st.markdown("Дорогие одноклассники! ")
            st.markdown("**1.** Вашему вниманию предлагаются воспоминания выпускников сш. им В.И.Ленина 1968 года. ")
            st.markdown("**2.** Это первая редакция сборника, так называемы сигнальный вариант. Авторы продолжают работать дальше и расширяют сборник.")
            st.markdown("**3.** В скором времени он будет предложен вам для ознакомления. Желаем вам приятного чтения!")
            #st.markdown("Желаем вам приятного чтения!")
            #st.markdown("If you have any questions regarding this project or require any further information, feel free to [contact me](https://www.navidma.com/contact).")
            #We will write the GitHub link here.
            #st.subheader('GitHub Link:')
            #st.markdown('* [GitHub Repo](https://github.com/navido89/covid19-dashboard-dataviz)')
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
    # Main Page.
    if options == "Home":
        row1_spacer1, row1_1, row1_spacer2 = st.beta_columns((.1, 3.2, .1))

        with row1_1:
            st.markdown("![COVID-19 Picture](https://d2jx2rerrg6sh3.cloudfront.net/image-handler/ts/20200420091641/ri/674/picture/2020/4/%40shutterstock_1647268288.jpg)")
            st.markdown("Welcome to my COVID-19 data visualization web app. The purpose of this project is to have a look at the current state of COVID-19 using visualizations from different geographical perspectives. The plots have been created by using data visualization tools such as Plotly and Folium. The project is broken down into three parts.")
            st.markdown("**1. Global COVID-19 Situation**: We will display a folium map that shows the total cases, total deaths, total cases per 100,000, and total deaths per 100,000. In addition to that, we will display various time series plots to understand better how the disease spreads over time across the globe.")
            st.markdown("**2. COVID-19 Situation by World Health Organization Region (WHO)**: In the following section, we look at the disease from the World Health Organization's regional perspective. We will compare the different regions based on their total cases, total deaths, total cases per 100 million and total deaths per 100 million deaths.")
            st.markdown("**3. COVID-19 Situation in the United States**: Last but not least, we pay our attention to the United States and explore the current situation in the US based on the cases, deaths (with and without per capita), vaccine status, and the status of the different variants spreading across the states. ")
            st.markdown("The data is pulled from various resources, as you can see below in the Data Source section, and it will be updated daily by the various organizations listed below.")
            st.markdown("If you have any questions regarding this project or require any further information, feel free to [contact me](https://www.navidma.com/contact).")
            #We will write the GitHub link here.
            st.subheader('GitHub Link:')
            st.markdown('* [GitHub Repo](https://github.com/navido89/covid19-dashboard-dataviz)')
            
            #We will list the libraries here.
            st.subheader('Technologies:')
            st.markdown("Streamlit, Plotly, Folium, Pandas, GeoPandas, NumPy, Branca, Jinja2, Date.")
    
            #We will list the data source.
            st.subheader('Data Source:')
            
            # Covid data source.
            st.markdown('**COVID-19 - Data:**')
            st.markdown('* [Global Cases](https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv) by Johns Hopkins CCSE.')
            st.markdown('* [Global Deaths](https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv) by Johns Hopkins CCSE.')
            st.markdown('* [US Cases](https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv) by Johns Hopkins CCSE.')
            st.markdown('* [US Deaths](https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv) by Johns Hopkins CCSE.')
            st.markdown("* [Global Data](https://covid19.who.int/WHO-COVID-19-global-data.csv) by World Health Organization")
            st.markdown("* [US Vaccine Data](https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/us_state_vaccinations.csv) by Our World in Data.")
            st.markdown("* [US COVID-19 Cases Variants Data](https://www.cdc.gov/coronavirus/2019-ncov/downloads/transmission/03252021WebUpdateMAP.csv) by Centers for Disease Control and Prevention (CDC).")

            # Population Data:
            st.markdown('**Population - Data:**')
            st.markdown('* [2020 Population by country](https://www.kaggle.com/tanuprabhu/population-by-country-2020?select=population_by_country_2020.csv) from Kaggle.')
            st.markdown('* [Population by WHO region](https://apps.who.int/gho/athena/data/xmart.csv?target=GHO/WHS9_86,WHS9_88,WHS9_89,WHS9_92,WHS9_96,WHS9_97,WHS9_90&profile=crosstable&filter=COUNTRY:-;REGION:*&x-sideaxis=REGION&x-topaxis=GHO;YEAR) by World Health Organization.')
        
            # Geography Date
            st.markdown('**GeoJSON - Data:**')
            st.markdown('* [World geoJSON file](https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json)')
            st.markdown('* [US geoJSON file](https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/us-states.json)')

    # Global Situation Page
    #if options == "Global Situation":
    
    
#if __name__ == '__main__':
#    main()

