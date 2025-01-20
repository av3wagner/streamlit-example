import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
#import pandas as pd
#import numpy as np
from dash import Dash, dcc, html, Input, Output, State, callback
from jupyter_dash import JupyterDash
import base64

app = JupyterDash(external_stylesheets=[dbc.themes.SLATE])
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

File1="ArtikelList.md"
File2="README05.md"
File3="+Resume04.md"
MdFile="AWresume.md"
Asni="TOC10+.md"

image_path = 'assets/WagnerFoto.jpg'
image = html.Img(src='assets/WagnerFoto.jpg', style={"height":"200", "width":"150", 'padding-left': 220,})


def b64_image(image_filename):
    with open(image_filename, 'rb') as f:
        image = f.read()
    return 'data:image/png;base64,' + base64.b64encode(image).decode('utf-8')

def demo_explanation(File):
    # Markdown files
    with open(File, "r", encoding="utf-8") as file:    
        demo_md = file.read()
    return html.Div(
        html.Div([dcc.Markdown(demo_md, className="markdown")]),
        style={"margin": "20px"},
    )

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "A simple sidebar layout with navigation links", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Page 1", href="/page-1", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
                dbc.NavLink("Page 3", href="/page-3", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.Div(
                [html.Div(id="demo-explanation",  children=[demo_explanation(File1)])         
                ],style={'width':'95.0%',"height": '710px','display':'inline-block',
                                 'overflow-y':'auto',
                                 'marginLeft':50, 'vertical-align':'middle'},
                  className="four columns instruction",
            ), 
    elif pathname == "/page-1":
        return html.P("This is the content of page 1. Yay!")
        return html.Div(
                [html.Div(id="demo-explanation",  children=[demo_explanation(File2)])         
                ],style={'width':'95.0%',"height": '710px','display':'inline-block',
                                 'overflow-y':'auto',
                                 'marginLeft':50, 'vertical-align':'middle'},
                  className="four columns instruction",
            ),
    elif pathname == "/page-2":
        return html.Div(
             [html.Div(id="demo-explanation", children=[demo_explanation(MdFile)])],
               style={'width':'95.0%',"height": '710px','display':'inline-block',
                      'overflow-y':'auto', 'color': 'yellow', "font-size": "1.4rem",
                      'marginLeft':50, 'vertical-align':'middle'},
               className="four columns instruction",         
        )
    
    elif pathname == "/page-3":
        return html.Div(
             [html.Div(id="demo-explanation", children=[demo_explanation(Asni)])],
               style={'width':'95.0%',"height": '710px','display':'inline-block',
                      'overflow-y':'auto', 'color': 'yellow', "font-size": "1.4rem",
                      'marginLeft':50, 'vertical-align':'middle'},
               className="four columns instruction",         
        )
       
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


def snapshot_page(value):
    if value == 'Об авторе (профиль)':
        img=1
        Text="Профессиональный профиль"
        MDfile=profil
    elif value == 'Об авторе (биография)':
        img=1
        Text="Краткая биография"
        MDfile=resume
    elif value == 'Об авторе (проекты)':
        img=1
        Text="Научно-технические проекты (1974-2023)"
        MDfile=proects
    elif value == 'Об авторе (публикации)':
        img=1
        Text="Публикации (70+)"
        #MDfile=papers
        MDfile=papers2023
    elif value == 'Об авторе (Контакты)':
        img=1
        Text="Контакты"
        MDfile=kontakt
    elif value == 'Система: инструкция':
        img=0
        Text='Инструкция по эксплуатации Аналитической Информационной Системы «АИС ВTИИ»'
        MDfile=System1      
    elif value == 'Система: описание':
        img=0
        Text="Аналитическая Информационная Система «АИС ВTИИ»"
        MDfile=System2   
    elif value == 'Система: история создания':
        img=0
        Text="История разработки Аналитической Информационной Системы в медицине, здравоохранении и смежных областях"
        MDfile=System3     
            
    if img==1:
        return html.Div([
            html.Div([
            html.Div(id='tabs-div', children=[image], className='tab-div'), 
            html.H1(children=Text, style={'color': 'white', 'textAlign': 'left', 'padding-left': 100}),
            html.H1(children="x", style={'color': "#111111", 'textAlign': 'left', 'padding-left': 100, "font-size": "2.4rem", "line-height": "0.7em"}),            
            html.Div([dcc.Markdown(children=MDfile)], style={'color': 'yellow', "font-size": "1.4rem", 'padding-left': 100, 'display': 'display-inblock'}),
            #html.Br()    
         ]),
        ])
    elif img==0:
        return html.Div([
            html.Div([
            html.H1(children=Text, style={'color': 'white', 'textAlign': 'left', 'padding-left': 100, "font-size": "2.4rem"}),    
            html.H1(children="x", style={'color': "#111111", 'textAlign': 'left', 'padding-left': 100, "font-size": "2.4rem", "line-height": "0.7em"}),            
            html.Div([dcc.Markdown(children=MDfile)], style={'color': 'yellow', "font-size": "1.4rem", 'padding-left': 100, 'display': 'display-inblock'}),
            html.Br()    
             ]),
            ])    


if __name__ == "__main__":
    app.run_server(debug=False, port=8054)
