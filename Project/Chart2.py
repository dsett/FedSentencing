import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

df = pd.read_csv('/Users/DSetton/Documents/FedSentencing/Data/NYSouthernDistrictData.csv')

app.layout = html.Div([
    
    dcc.Graph(
        id='ageeducatuon-vs-offense',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['BOOKER2'] == i]['SentenceMonths'],
                    y=df[df['BOOKER2'] == i]['CRIMHIST'],
                    text=df[df['BOOKER2'] == i]['BOOKER2'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.BOOKER3.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'Sentence'},
                yaxis={'title': 'Relation to Sentence Guidelines'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server()