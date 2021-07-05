# -*- coding: utf-8 -*-
"""
Created on Tue May 18 14:20:14 2021

@author: scpgo
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go # or 
import plotly.express as px

from pygraphtec import lee_fichero_sesion

df = lee_fichero_sesion("201112-165432.csv", path_sesiones='dataLogger')

app = dash.Dash()

#fig_names = ['fig1', 'fig2']
fig_names = df.columns #asigno fig_names a las columnas del Dataframe

cols_dropdown = html.Div([ #Div del filtro de variables
    dcc.Dropdown(
        id='cols_dropdown',
        options=[{'label': x, 'value': x} for x in fig_names], #creo el filtro de variables
        value=None, #ninguna opcion inicial preseleccionada    
        multi=True #permite selección de varias opciones
    )])
    
fig_plot = html.Div(id='fig_plot') #Div de la gráfica

app.layout = html.Div([cols_dropdown, fig_plot]) #permite construir la estructura el filtro
                                                 #de variables y la gráfica

@app.callback( #permite devolver la gráfica como Dash Core Component dcc.Graph (línea 44)
dash.dependencies.Output('fig_plot', 'children'),
[dash.dependencies.Input('cols_dropdown', 'value')])
def name_to_figure(value):
    if value is None:
        figure = {}
    else:
        figure = px.line(df[value]) #se crea figura que representa todas las variables
                                   #fig_names corresponde a la variable global (línea 25)
    return dcc.Graph(figure=figure)

app.run_server(debug=True, use_reloader=False) #arranca la aplicacion