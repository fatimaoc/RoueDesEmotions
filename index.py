import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


from app import app
from app import server
from layoutHome import layoutHome
from layoutPage1 import layoutPage1
#from layoutPage2 import layoutPage2
import callbacks

app.layout = html.Div(id='app', children=[
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/' :
        return layoutHome
    elif pathname == '/layoutPage1':
        return layoutPage1
    #elif pathname == layoutPage2:
        #return layoutPage2
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)