
from app import app
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_table
import pandas as pd
import numpy as np
from collections import defaultdict
import pickle
import plotly.graph_objects as go
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
from sklearn import metrics
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.metrics import precision_recall_curve, average_precision_score



df = pd.read_csv("./Data/Emotion_final.csv")
emot = df.Emotion.unique()
corpus = df.Text
targets = df.Emotion
targets = np.array([1 if x == emot[0] else 2 if x==emot[1] else 3 if x==emot[2] else 4 if x==emot[3] else 5 if x==emot[4] else 6 for x in targets])

def subsample(x, init, end, step=400):
    return np.hstack((x[init:end], x[end:end:step]))

all_options = {
    'Emotion_final.csv': ['all', 'sadness', 'anger', 'love', 'surprise', 
                          'fear', 'happy'],
    'text_emotion.csv': [u' all ', ' empty ', ' sadness ', ' enthusiasm ', ' neutral ', ' worry ', ' surprise ', ' love ', ' fun ', ' hate ', ' happy ', ' boredom ', ' relief ', ' anger ']
}




@app.callback(
    Output('Emotion_radio', 'options'),
    Input('DataSet_dropdown', 'value'))
def set_emotions_options(selected_dataset):
    return [{'label': i, 'value': i} for i in all_options[selected_dataset]]

@app.callback(
    Output('Emotion_radio', 'value'),
    Input('Emotion_radio', 'options'))
def set_emotions_value(available_options):
    return available_options[0]['value']


@app.callback(
    Output('Hist_emotions','figure'), 
    Input('DataSet_dropdown', 'value'))
def display_hist_emotions_page1(dataset):
    df = pd.read_csv('./Data/'+dataset)
    if dataset == 'text_emotion.csv':
        df.columns = ["Tweet_id", "Emotion", "Author", "Text"]
        df = df.drop(columns='Tweet_id')
        df = df.drop(columns='Author')
        df.loc[df.Emotion =='happiness', 'Emotion'] = 'happy'
    
    fig_Hist_Emot = go.Figure(
        data=[go.Histogram(x=df.Emotion, 
                           name='words count', 
                           ), 
        go.Histogram(x=df.Emotion, 
                     cumulative_enabled=True, 
                     name='cumulative <br>words count', 
                     )],
        layout ={
            'xaxis_title_text': 'Emotions',
            'paper_bgcolor':'#B0BEC5',
            'plot_bgcolor':'#546E7A',
            'font_color':'white',
            'legend' : {
                'yanchor':"top",
                'y':1.2,
                'xanchor':"left",
                'x':0.01
                }
            })
    return fig_Hist_Emot



@app.callback(
    Output('Hist_mots','figure'), 
    Input('Emotion_radio', 'value'),
    Input('word_rank_slider', 'value'),
    Input('DataSet_dropdown', 'value'))
def display_hist_mots_page1(Emotion_value, slid_value, dataset):
    df_temp = pd.read_csv('./Data/'+dataset)
    if dataset == 'text_emotion.csv':
        df_temp.columns = ["Tweet_id", "Emotion", "Author", "Text"]
        df_temp = df_temp.drop(columns='Tweet_id')
        df_temp = df_temp.drop(columns='Author')
        df_temp.loc[df_temp.Emotion =='happiness', 'Emotion'] = 'happy'

    if Emotion_value == 'all':
        df = df_temp
    else:
        df=df_temp.loc[df_temp.Emotion==Emotion_value]

    del df_temp

    vect = CountVectorizer(stop_words='english')
    X = vect.fit_transform(df.Text)
    words = vect.get_feature_names()
    
    wsum = np.array(X.sum(0))[0]
    ix = wsum.argsort()[::-1]
    wrank = wsum[ix] 
    labels = [words[i] for i in ix]

    trace = go.Bar(x = subsample(labels, slid_value[0], slid_value[1]), 
                   y = subsample(wrank, slid_value[0], slid_value[1]),
                   marker = dict(color = 'rgba(255, 174, 255, 0.5)',
                   line = dict(color ='rgb(0,0,0)',width =1.5)),
    )
    layout = go.Layout(
                    xaxis_title_text = 'Word rank',
                    yaxis_title_text = 'word frequency',
                    paper_bgcolor = '#B0BEC5',
                    plot_bgcolor = '#546E7A',
                    font_color='white')
    figure = go.Figure(data = trace, layout = layout)
    return figure
   

@app.callback(
    Output('Pie_chart','figure'), 
    Input('DataSet_dropdown', 'value'))
def display_Pie_Chart_page1(dataset):
    df = pd.read_csv('./Data/'+dataset)
    if dataset == 'text_emotion.csv':
        df.columns = ["Tweet_id", "Emotion", "Author", "Text"]
        df = df.drop(columns='Tweet_id')
        df = df.drop(columns='Author')
        df.loc[df.Emotion =='happiness', 'Emotion'] = 'happy'
    
    fig_Pie_chart = go.Figure(data=[go.Pie(labels=df.Emotion.unique(),
                                values=df.groupby('Emotion').Text.nunique(), 
                                textinfo='label+percent',
                                )],
                    layout ={
                    #'title':'Répartition des Émotions',
                    'paper_bgcolor':'#B0BEC5',
                    'plot_bgcolor':'#546E7A',
                    'font_color':'white',
                    'legend' : {
                        'orientation' : "h",
                        'yanchor':"top",
                        'y':1,
                        'xanchor':"left",
                        'x':-0.4
                        }
                })   
             
    return fig_Pie_chart

@app.callback(
    Output('page1_table','children'), 
    Input('Emotion_radio', 'value'),
    Input('DataSet_dropdown', 'value'))
def display_table_page1(Emotion_value, dataset):
    df_temp = pd.read_csv('./Data/'+dataset)
    if dataset == 'text_emotion.csv':
        df_temp.columns = ["Tweet_id", "Emotion", "Author", "Text"]
        df_temp = df_temp.drop(columns='Tweet_id')
        df_temp = df_temp.drop(columns='Author')
        df_temp.loc[df_temp.Emotion =='happiness', 'Emotion'] = 'happy'
        df_temp = df_temp.reindex(columns=['Text','Emotion'])

    if Emotion_value == 'all':
        df = df_temp
    else:
        df=df_temp.loc[df_temp.Emotion==Emotion_value]
        
    del df_temp

    table = dash_table.DataTable(
        id='app-1-table',
        export_format='csv',
        export_headers='display',
        columns=[{'id': c, 'name': c} for c in df.columns],
        data= df.to_dict('records'),
        style_as_list_view=True,
        fixed_rows={'headers': True},
        style_table={
            'overflowX': 'auto',
            'overflowY': 'auto',
            'maxHeight':'400px',
            'minWidth':'70vw',
            'maxWidth':'1600px'
            },

        style_cell_conditional=[
            {'if': {'column_id': 'Text'},'width': '58vw'},
            {
            'height': 'auto',
            'minWidth': '50px', 'width': '70px', 'maxWidth': '300px',
            'whiteSpace': 'normal','textAlign':'center',
            'backgroundColor': '#7986CB',
            'color': 'white'
            }],
        
        style_data_conditional=[{
            'if': {'row_index': 'odd'},
            'backgroundColor': '#B0BEC5',
            'color': 'white'
            }],
        style_header={
            'backgroundColor': '#01579B',
            'fontWeight': 'bold',
            'color':'white'},
        
        tooltip_data=[{
            column: {'value': str(value), 'type': 'markdown'} for column, value in row.items()
            } for row in df.to_dict('rows')],
        tooltip_duration=None
        ),  

    return table



             


