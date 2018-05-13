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
                    x=df[df['AGE'] == i]['MinTimeServed'],
                    y=df[df['AGE'] == i]['nDependents'],
                    text=df[df['MinTimeServed'] == i]['MinTimeServed'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.AGE.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'Minimum Time Served in Months'},
                yaxis={'title': '# Dependents = y-axis, Age = colors'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server()