import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_html_components.Br import Br
from app import app
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_table
import pandas as pd
import numpy as np
from collections import defaultdict
import plotly.graph_objects as go
import plotly.express as px
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
from sklearn import metrics
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.metrics import precision_recall_curve, average_precision_score

colors = {
    'background': '#90A4AE',
    'text': '#F5F5F5'
}


layoutPage1 = html.Div([
    html.Header([
        dcc.Link(html.Button("Page d'accueil", className='pth_button'), href='/'),
        #dcc.Link(html.Button('Résultats de la classification', className='pth_button'), href="layoutPage2"),
        html.Br(),
        html.H1(
            children='Analyse des émotions dans un Texte',
            style={
                'backgroundColor': colors['background'],
                'textAlign': 'center',
                'color': colors['text']  
    }),
        html.H2(
             children='Analyse des données',
             style={
                 'backgroundColor': colors['background'],
                'textAlign': 'center',
                'color': colors['text'] 
             }),
        html.Br(),
        html.Br(),

    ]),
    html.Main(

    ),
    html.Tbody(style={'display':'block','backgroundColor': colors['background'],'textAlign': 'center','color':'white'},
    children=[
        html.Div(style={'backgroundColor': colors['background']}, children=[
            html.Article(children=[
                
                html.Br(),
                html.H3('Selection du jeu de données'),
                html.Br(),
                dcc.Dropdown(
                    id='DataSet_dropdown',
                    options=[
                        {'label': '1er jeu de données : Kaggle', 'value': 'Emotion_final.csv'},
                        {'label': '2em jeu de données: Data.word', 'value': 'text_emotion.csv'},
                    ],
                    optionHeight= 60,
                    value='Emotion_final.csv',
                    clearable=False,
                ),

                html.Br(),
                                
                html.H3('Selection des émotions'),
                html.Br(),
                dcc.RadioItems(
                   id='Emotion_radio'
                   ),
                html.Br(),
                html.H3('Histogramme des Emotions'),

                ## Fig 1 : Hist des Emotions
                dcc.Graph(
                    id='Hist_emotions'
                    ),
            ]),
        ]),
        html.Div(id='Block_right', children=[
            html.Section(id='Block_1',children=[
                html.Article(id='Block_1_Article_1', children=[

                    ## Fig 2 : Hist des mots
                    html.H3("Classement des mots du mot le plus frequent au moins présent"),
                    dcc.Graph(
                        id='Hist_mots',
                        ),
                    dcc.RangeSlider(
                        id='word_rank_slider',
                        min=0,
                        max=100,
                        step=1,
                        value=[2, 50],
                        marks={
                            0: {'label': 'Top(min)', 'style': {'color': '#90A4AE'}},
                            50: {'label': 'Top(50)'},
                            100: {'label': 'Top(Max)', 'style': {'color': '#90A4AE'}}
                        },
                        allowCross=False
                    ),
                ]),

                html.Article(id='Block_1_Article_2', children=[
                    html.H3('Repartition des Emotions '),
                    dcc.Graph(
                        # Fig 3 : Pie Chart
                        id='Pie_chart'
                        ),
                ]),
            ]),
            html.Section(id='Block_2',children=[
                html.Article(id='Block_2_Article_1', children=[
                    html.H3('Base de données'), 
                    # Tableau des données
                    html.Div(id='div_table_data',children=[
                        html.Div(id='page1_table'),
                    ]),
                ]),
            ]),        
        ]),
    ]),
])