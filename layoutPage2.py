import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
import pandas as pd
import numpy as np
from collections import defaultdict
import pickle
import plotly.express as px
import plotly.graph_objects as go
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn import metrics



data = pd.read_csv("./Data/Emotion_final.csv")
emot = data.Emotion.unique()
corpus = data.Text
targets = data.Emotion
targets = np.array([1 if x == emot[0] else 2 if x==emot[1] else 3 if x==emot[2] else 4 if x==emot[3] else 5 if x==emot[4] else 6 for x in targets])


