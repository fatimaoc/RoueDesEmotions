import dash
import dash_core_components as dcc
import dash_html_components as html
from dash_html_components import Header
from dash_html_components.Br import Br
from dash_html_components.P import P
import plotly.express as px
import pandas as pd
from app import app
from app import server


colors = {
    'background': '#90A4AE',
    'text': '#F5F5F5'
}


layoutHome = html.Div(style={'display':'block','margin':'auto','backgroundColor':colors['background']}, children= [
    html.Header([
        dcc.Link(html.Button("Page d'accueil"), href='/'),
        dcc.Link(html.Button('Analyse des données'), href='layoutPage1'),
        #dcc.Link(html.Button('Classification', className='pth_button'), href='layoutPage2'),
        ]),
        
    

    html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='La Roue des Emotions',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.H2(
        children='Brief de fin de bloc',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.H6(
        children='Décembre 2020 Fatima MOUSSAOUI',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    
        
    ),

    html.Img(style={'display':'block','margin':'auto','height':'400px','border-radius':'50%'},id='image_roue', src=app.get_asset_url('roue.png')),

    html.Br(),
    html.Br(),
    html.Br(),


    html.H1(
        children='Contexte',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
   

    html.P(style={'margin':'auto','text-align': 'left','color':colors['text'],'margin-left':'50px'} , children=['''
    Construit d’après les travaux du psychologue américain Robert Plutchik,\
    la roue des émotions est un modèle des émotions humaines et peut facilement servir à définir\ 
    des personnages, ainsi que leur évolution dans une trame narrative. Est-il possible\
    d'identifier des émotions dans des phrases narratives issues de communications écrites ?''']),

    html.Br(),

    html.P(style={'margin':'auto','text-align': 'left','color':colors['text'],'margin-left':'50px'} , children=['''
    Depuis quelques années, les dispositifs de communication médiatisée par ordinateur (CMO) sont massivement\
    utilisés, aussi bien dans les activités professionnelles que personnelles. Ces dispositifs permettent à des\
    participants distants physiquement de communiquer. La plupart implique une communication écrite médiatisée \
    par ordinateur (CEMO) : forums de discussion, courrier électronique, messagerie instantanée. Les participants\
    ne s’entendent pas et ne se voient pas mais peuvent communiquer par l’envoi de messages écrits, qui combinent, \
    généralement, certaines caractéristiques des registres écrit et oral .\
    (Marcoccia, 2000a ; Marcoccia, Gauducheau, 2007 ; Riva, 2001).''']),

    html.H3(style={'text-align': 'left','color':colors['text'],'margin-left':'50px'} , children=["Livrables attendus "]),

    html.Br(),

    html.H6(style={'text-align': 'left','color':colors['text'],'margin-left':'50px'} , children=["1) Notebook résumant l'analyse machine learning des émotions"]),
    html.Br(),
    html.H6(style={'text-align': 'left','color':colors['text'],'margin-left':'50px'} , children=["2) Visualisation de l'analyse sur un Dashboard multi-pages avec deployment sur Heroku"]),
    html.Br(),
    html.H3(style={'text-align': 'left','color':colors['text'],'margin-left':'50px'} , children=["Consignes "]),
    html.Br(),
    html.H6(style={'margin-left':'50px','text-align': 'left','color':colors['text']} , children=["1)Réalisez les apprentissages et les évaluations des modèles avec le jeu de données de Kaggle"]),
    html.Br(),
    html.H6(style={'margin-left':'50px','text-align': 'left','color':colors['text']} , children=["2)Présentez vos résultats sous la forme d'un dashboard multi-pages Dash"]),
    html.H6(style={'margin-left':'70px','text-align': 'left','color':colors['text']} , children=["a)La première page du Dashboard sera dédiée à l'analyse et du traitement des données brutes"]),
    html.H6(style={'margin-left':'70px','text-align': 'left','color':colors['text']} , children=["b)La  deuxième page du Dashboard sera dédiée aux résultats issues des classifications avec au moins cinq classifiers présentés dans un tableau"]),
    html.Br(),
    html.H6(style={'margin-left':'50px','text-align': 'left','color':colors['text']} , children=["3)Héberger le dashboard sur le cloud de visualisation de données Héroku "]),
    html.Br(),
    

    
])])
