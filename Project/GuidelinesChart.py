import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

df = pd.read_csv('/Users/DSetton/Documents/FedSentencing/Data/NYSouthernDistrictData.csv',na_values=[-999])

Guidlinescodedict = {0: "Within Range", 1: "Above Departure", 2:"Govt Sponsored", 
                     3:"Below Range"}

for key in Guidlinescodedict.keys():
    df["BOOKER2"].__setitem__(df["BOOKER2"]==key, Guidlinescodedict[key])


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
                ) for i in df.BOOKER2.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'linear', 'title': 'Sentence in Months'},
                yaxis={'title': 'Criminal history (0 = None, 1 = Some)'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 5},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server()