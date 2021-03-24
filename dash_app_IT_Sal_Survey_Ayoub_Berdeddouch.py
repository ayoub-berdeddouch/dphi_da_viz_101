import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import plotly.express as px

import numpy as np
import pandas as pd



df_survey = pd.read_csv('survey_18_20.csv')

# the style arguments for the sidebar.
SIDEBAR_STYLE = {
    'position': 'fixed',
    'top': 0,
    'left': 0,
    'bottom': 0,
    'width': '20%',
    'padding': '20px 10px',
    'background-color': '#f8f9fa'
}

# the style arguments for the main content page.
CONTENT_STYLE = {
    'margin-left': '25%',
    'margin-right': '5%',
    'padding': '20px 10p'
}

TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#191970'
}

CARD_TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#0074D9'
}

controls = dbc.FormGroup(
    [
        html.P('Dropdown', style={
            'textAlign': 'center'
        }),
        dcc.Dropdown(
            id='dropdown',
            options=[
            {
                'label': '2018',
                'value': 2018
            }, {
                'label': '2019',
                'value': 2019
            },
                {
                    'label': '2020',
                    'value': 2020
                }
            ],
            value=2018,  # default value
            multi=False,
        ),
        html.Br(),
        dbc.Button(
            id='submit_button',
            n_clicks=0,
            children='Submit',
            color='primary',
            block=True
        ),
    ]
)

sidebar = html.Div(
    [
        html.H2('Parameters', style=TEXT_STYLE),
        html.Hr(),
        controls
    ],
    style=SIDEBAR_STYLE,
)

content_first_row = dbc.Row([
    dbc.Col(
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.H4(id='card_title_1', children=['Card Title 1'], className='card-title',
                                style=CARD_TEXT_STYLE),
                        html.P(id='card_text_1', children=['Sample text.'], style=CARD_TEXT_STYLE),
                    ]
                )
            ]
        ),
        md=3
    ),
    dbc.Col(
        dbc.Card(
            [

                dbc.CardBody(
                    [
                        html.H4('IT Salary Survey Dataset', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Years : 2018-2019-2020 ', style=CARD_TEXT_STYLE, ),
                    ]
                ),
            ]

        ),
        md=3
    ),
    dbc.Col(
        dbc.Card(
            [	
                dbc.CardBody(
                    [
                        html.H4('Dphi BootCamp', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Data Analysis & Visualization 101', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]

        ),
        md=3,
        width="auto"
    ),
    dbc.Col(
        dbc.Card(
            [
                dbc.CardBody(
                    [
                        html.H4('Gender Ratio Through years 2018-2020', className='card-title', style=CARD_TEXT_STYLE),
                        html.P('Female%  growed from 13.7% to 15.5%, while Male%  dropped 86.3% to 84.5%', style=CARD_TEXT_STYLE),
                    ]
                ),
            ]
        ),
        md=3
    )
])

content_second_row = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(id='graph_1'), md=6
        ),
        dbc.Col(
            dcc.Graph(id='graph_2'), md=6
        ),
    ]
)

content_third_row = dbc.Row(
    [   
        dbc.Col(
            dcc.Graph(id='graph_3'), md=12
        ),
        
    ]
)

content_fourth_row = dbc.Row(
    [   
        dbc.Col(
            dcc.Graph(id='graph_4'), md=6
        ),
        dbc.Col(
            dcc.Graph(id='graph_5'), md=6
        ),
        
    ]
)

content_fifth_row = dbc.Row(
    [

        dbc.Col(
            dcc.Graph(id='graph_6'), md=6
        ),
        dbc.Col(
            dcc.Graph(id='graph_7'), md=6
        ),


    ]

)

content_sixth_row = dbc.Row(
    [

        dbc.Col(
            dcc.Graph(id='graph_8'), md=12
        ),    
    ]

)

content = html.Div(
    [
        html.H2('IT Salary Survey Analytics Dashboard', style=TEXT_STYLE),
        html.H3('by Ayoub Berdeddouch', style=TEXT_STYLE),
        html.Hr(),
        content_first_row,
        content_second_row,
        content_third_row,
        content_fourth_row,
        content_fifth_row,
        content_sixth_row,
    ],
    style=CONTENT_STYLE
)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([sidebar, content])


@app.callback(
    Output('graph_1', 'figure'),
    [Input('submit_button', 'n_clicks')],
    [State('dropdown', 'value'),
     
     ])
def update_graph_1(n_clicks, dropdown_value):
    print(n_clicks)
    print(dropdown_value)
    
    
    fig = px.bar(df_survey, x="Gender", y="Age", color="Salary_in_EUR",opacity=0.9, title='Gender by Age & Salary')

    fig.update_layout({
        'height': 600,
        
    })
    return fig


@app.callback(
    Output('graph_2', 'figure'),
    [Input('submit_button', 'n_clicks')],
    [State('dropdown', 'value'),
     
     ])
def update_graph_2(n_clicks, dropdown_value):
    print(n_clicks)
    print(dropdown_value)

    fig = px.density_contour(df_survey, x='Years of experience', y='Salary_in_EUR', color="Gender", title='XP Years by Salary & Gender')
    
    fig.update_layout({
        'height': 600
    })
    return fig


@app.callback(
    Output('graph_3', 'figure'),
    [Input('submit_button', 'n_clicks')],
    [State('dropdown', 'value'),
     
     ])
def update_graph_3(n_clicks, dropdown_value):
    print(n_clicks)
    print(dropdown_value)
    

    fig = px.bar(df_survey, x="Position", y="Seniority level", color="Age" ,barmode="group", title='Position by Seniority & Age')
    
    fig.update_layout({
        'height': 600
    })
    return fig


@app.callback(
    Output('graph_4', 'figure'),
    [Input('submit_button', 'n_clicks')],
    [State('dropdown', 'value'),
     
     ])
def update_graph_4(n_clicks, dropdown_value):
    print(n_clicks)
    print(dropdown_value)
    

    #---------------------------------
    grouped = df_survey.groupby('Year')
    # pass the Year = dropdown_value
    dfgp = grouped.get_group(dropdown_value)

    #---------------------------------
    gender_count  = dfgp['Gender'].value_counts()
    gender_count_un = dfgp['Gender'].dropna().unique()
    print('Gender count\n')
    print(gender_count)
    print('Gender count unique\n')
    print(gender_count_un)
    genders =[]
    for i in range(0,len(gender_count)):
    	genders.append(gender_count[i])

    print(genders)

    df_gender = pd.DataFrame(genders,columns=["Gender_Ratio"], index= gender_count_un)

    fig = px.pie(df_gender, values='Gender_Ratio', names=df_gender.index, title='Gender Ratio for year {}'.format(dropdown_value))
    fig.update_layout({
        'height': 450
    })
    return fig


@app.callback(
    Output('graph_5', 'figure'),
    [Input('submit_button', 'n_clicks')],
    [State('dropdown', 'value'),

     ])
def update_graph_5(n_clicks, dropdown_value):
    print(n_clicks)
    print(dropdown_value)

    fig = px.scatter(df_survey, x='Position', y='Salary_in_EUR', color='Gender', title='Position by Salary & Gender')
    fig.update_layout({
        'height': 600,
        'width': 600

    })
    return fig


@app.callback(
    Output('graph_6', 'figure'),
    [Input('submit_button', 'n_clicks')],
    [State('dropdown', 'value'),
     
     ])
def update_graph_6(n_clicks, dropdown_value):
    print(n_clicks)
    print(dropdown_value)
    
    fig = px.bar(df_survey, x='Seniority level', y='Age',color="Year", orientation='h', title='Seniority by Age through the Years')
    return fig

@app.callback(
    Output('graph_7', 'figure'),
    [Input('submit_button', 'n_clicks')],
    [State('dropdown', 'value'),
     
     ])
def update_graph_7(n_clicks, dropdown_value):
    print(n_clicks)
    print(dropdown_value)
    
    
    fig = px.scatter(df_survey, x='Years of experience', y='Salary_in_EUR', color='Age', title='XP Years by Salary & Age')
    
    return fig

@app.callback(
    Output('graph_8', 'figure'),
    [Input('submit_button', 'n_clicks')],
    [State('dropdown', 'value'),
     
     ])
def update_graph_8(n_clicks, dropdown_value):
    print(n_clicks)
    print(dropdown_value)
    

    container = "The year chosen by the user is/are: {}".format(dropdown_value)
    print(container)


    dff = df_survey.copy()
    dff = dff[dff['Year'] == dropdown_value ]
    print(dff[:3])

    groupe = dff.groupby(['Years of experience','Year'], as_index=False)
    dfgp = groupe['Salary_in_EUR'].agg(np.median)
    dff1 = pd.DataFrame(dfgp)
    print(dff1[:3])
	

    fig = px.line(dff1, x='Years of experience', y='Salary_in_EUR', color='Year', title='XP Years by Salary by Year')
    
    return fig

@app.callback(
    Output('card_title_1', 'children'),
    [Input('submit_button', 'n_clicks')],
    [State('dropdown', 'value'),
     
     ])
def update_card_title_1(n_clicks, dropdown_value):
    print(n_clicks)
    print(dropdown_value)
    
    return 'Selected Year'


@app.callback(
    Output('card_text_1', 'children'),
    [Input('submit_button', 'n_clicks')],
    [State('dropdown', 'value'),
     
     ])
def update_card_text_1(n_clicks, dropdown_value):
    print(n_clicks)
    print(dropdown_value)
    
    return dropdown_value


if __name__ == '__main__':
    app.run_server(port='8085')
