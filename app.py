from dash import Dash, html, dcc, Output, Input, State, callback
from datetime import datetime as dt
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
# import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=['assests/styles.css'])
server = app.server

app.layout= html.Div([
    html.Div([
        html.H1("Welcome to Dash Stock Forecasting app", className="start"),

        html.Div([
            #stock code input
            html.Label('Input stock code'),
            html.Br(),
            dcc.Input(placeholder='Stock Name', id='stock-name', type='text'),
            html.Button('Submit', id='submit-button', n_clicks=0),
        ], className="stock-code"),

        html.Div([
            #date range picker input
            html.Label('Select a date range'),
            html.Br(),
            dcc.DatePickerRange(
                id='my-date-picker-range',
                initial_visible_month=dt.now(),
                start_date_placeholder_text='Start Date',
                end_date_placeholder_text='End Date',
                calendar_orientation='horizontal',
                clearable=True,
            ),
        ], className="date-range"),

        html.Div([
            #stock price button
            #indicators button
            #Number of days of forecast input
            #forecast button
            html.Button('Stock Price', id='stock-price-button'),
            html.Button('Indicators', id='indicators-button'),
            dcc.Input(type='number', id='forecast-period'),
            html.Button('Forecast', id='forecast-period-button'),
        ]),
    ], className="nav"
    ),

    html.Div([
        html.Div([
            #logo
            #company name
        ], className="header", id="header"),
        html.Div([
            #description
        ], className="description-ticker", id="description-ticker"),
        html.Div([
            #stock price plot
        ], id="graphs-content"),
        html.Div([
            #indicator plot
        ], id="main-content"),
        html.Div([
            #forecast plot        
        ], id="forecast-content")
    ], className="content"
    )

], className="container")

@app.callback(
    Output('header', 'children'),
    Output('description-ticker', 'children'),
    Input('submit-button', 'n_clicks'),
    State('stock-name', 'value')
)
def update_header(n_clicks, stock_name):
    if n_clicks > 0:
        stock = yf.Ticker(stock_name)
        info = stock.info
        df = pd.DataFrame().from_dict(info, orient="index").T
        domain = df['website'].values[0]
        logo_url = f"https://logo.clearbit.com/{domain}"
        return [
            html.Img(src=logo_url, className="logo"),
            html.H3(info['shortName'])
        ]


@app.callback(
    Output('graphs-content', 'children'),
    Input('stock-price-button', 'n_clicks'),
    State('stock-name', 'value'),
    State('my-date-picker-range', 'start_date'),
    State('my-date-picker-range', 'end_date')


)
def func():
    return

if __name__ == "__main__":
    app.run(debug=True)




