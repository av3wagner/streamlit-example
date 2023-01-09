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
 #st.sidebar.title("Navigation")
 #options = st.sidebar.radio("Go to",['Home','Global Situation', 'Situation by WHO Region', 'Situation in the United States'], key='1')
 #st.sidebar.markdown("")
 #st.sidebar.image('https://media.giphy.com/media/dVuyBgq2z5gVBkFtDc/giphy.gif')

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
        st.sidebar.title("Navigation")
        st.sidebar.markdown("")
        st.sidebar.image('https://media.giphy.com/media/dVuyBgq2z5gVBkFtDc/giphy.gif')
        #f.write(pdf_file.getbuffer())
    #show_pdf(save_image_path)
    show_pdf("post1-compressed10G.pdf")

# We create our Streamlit App
def main():
    st.set_page_config(layout="wide")
    st.title("Dr. Alexander Wagner, Berlin")
    #st.markdown('A Web App by [Navid Mashinchi](http://www.navidma.com)') 
    st.markdown("[![Follow](https://img.shields.io/github/followers/navido89?style=social)](https://github.com/navido89)&nbsp[![Follow](https://img.shields.io/twitter/follow/NMashinchi?style=social)](https://twitter.com/NMashinchi)") 

    # First Row
    row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.beta_columns((.1, 2, .2, 1, .1))

    # Create the sidebar.
    st.sidebar.image('./images/streamlit-logo.png')
    st.sidebar.title("Navigation")
    options = st.sidebar.radio("Go to",['Home','Global Situation', 'Situation by WHO Region', 'Situation in the United States'], key='1')
    st.sidebar.markdown("")
    st.sidebar.image('https://media.giphy.com/media/dVuyBgq2z5gVBkFtDc/giphy.gif')
    
    # Date for side bar
    date_current = get_pst_time()
    
    # Global cases and deaths for side bar
    global_cases_side_bar = round(get_global_cases())
    global_deaths_side_bar = round(get_global_deaths())   
    st.sidebar.info("Date: **{}**".format(date_current))
    st.sidebar.info("Global Cases: **{}**".format(global_cases_side_bar))
    st.sidebar.info("Global Deaths: **{}**".format(global_deaths_side_bar))

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
    if options == "Global Situation":
        # We create the third row.
        row3_spacer1, row3_1, row3_spacer2 = st.beta_columns((.1, 3.2, .1))  
        with row3_1:
            # We get the date 
            date_current = get_pst_time()
            st.title('1. Global Situation:')
            global_cases = round(get_global_cases())
            global_deaths = round(get_global_deaths())
            st.markdown("As of **{}**, there have been **{}** positive COVID-19 cases and **{}** deaths globally. Below is a Folium Choropleth that shows the total cases, total deaths, total cases per capita (100,000), and total deaths per capita (100,000). **Please click on the layer control to select the different maps**. In addition to that, you can hover over each country to see more information.".format(date_current,global_cases,global_deaths))
            folium_plot1 = plot1()
            folium_static(folium_plot1)
            
            # Adding Top 5 Cases plot
            top5_country_cases = plot9()
            st.plotly_chart(top5_country_cases)

            # Adding Top 5 Deaths plot
            top5_country_deaths = plot10()
            st.plotly_chart(top5_country_deaths)

            # Adding Time Series Bar Plot.
            tsa_plot1 = plot4()
            st.plotly_chart(tsa_plot1)
            tsa_plot2 = plot5()
            st.plotly_chart(tsa_plot2)

            # Adding time series bubble maps with animation.
            bubble_plot1 = plot2()
            st.plotly_chart(bubble_plot1)
            bubble_plot2 = plot3()
            st.plotly_chart(bubble_plot2)
    
    # WHO Region Page
    if options == "Situation by WHO Region":
        # We create the third row.
        row3_spacer1, row3_1, row3_spacer2 = st.beta_columns((.1, 3.2, .1))  
        with row3_1:
            # Adding bar plots for WHO regions.
            st.title('2. Situation by WHO Regions:')
            st.markdown("The World Health Organization (WHO) divides its regions into 6 separate regions. The division is for the purposes of reporting, analysis, and administration. Below is a picture that shows the 6 different regions.")
            st.markdown("![WHO Regions](https://www.researchgate.net/profile/Anna-Lena-Lopez/publication/277779794/figure/fig3/AS:339883563470854@1458045964167/World-Health-Organization-regions.png)")
            who_plot1 = plot4a()
            st.plotly_chart(who_plot1)
           
    # US Situation Page
    if options == "Situation in the United States":
        row4_spacer1, row4_1, row4_spacer2 = st.beta_columns((.1, 3.2, .1))  
        with row4_1:
            st.title('3. Situation in the United States:')
            st.markdown("![USA Covid Picture](https://989bull.com/wp-content/uploads/2020/06/expert-warns-us-could-see-up-to-400000-covid-19-deaths-by-spring-2021.jpg)")
            st.markdown("Here the focus is on the United States and its current state regarding COVID-19, its Vaccine situation, and the different variants of the disease. To better understand the vaccine variables, please read below.")
            st.markdown("* **people_fully_vaccinated**: total number of people who received all doses prescribed by the vaccination protocol. If a person receives the first dose of a 2-dose vaccine, this metric stays the same. If they receive the second dose, the metric goes up by 1.")
            st.markdown("* **people_fully_vaccinated_per_hundred**: people_fully_vaccinated per 100 people in the total population of the state. ")
            st.markdown("* **total_distributed**: cumulative counts of COVID-19 vaccine doses recorded as shipped in CDC's Vaccine Tracking System. ")
            st.markdown('**Please click on the layer control to select the different maps**. In addition to that, you can hover over each state to see more information.')
            folium_plot8 = plot8()
            folium_static(folium_plot8)

            # add the Vertical Bar Plots
            US_vacc = plot11()
            st.plotly_chart(US_vacc)

            # Add Variant Table
            st.subheader("US COVID-19 Cases Caused by Variants")
            st.markdown("*According to the CDC, the data will no longer be updated. **Last update April 09, 2021**. Current data showing the prevalence of variants in the United States is available in the [COVID-19 Data Tracker.](https://covid.cdc.gov/covid-data-tracker/#variant-proportions)*")
            st.markdown("* B.1.1.7 = UK Variant")
            st.markdown("* B.1.351 = South Africa Variant")
            st.markdown("* P.1 = Brazil Variant")

            st.table(vairant_summary())

            # Add State Comparison of different Variants plot.
            st.subheader("Comparison COVID-19 Cases (Caused by Variants) by States")
            US_variant_comp = plot12()
            st.plotly_chart(US_variant_comp)
   
if __name__ == '__main__':
    main()


