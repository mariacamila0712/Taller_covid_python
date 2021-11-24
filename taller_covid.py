# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 15:14:56 2021

@author: Maria Camila
"""

import pandas as pd

url = 'covid_22_noviembre.csv'
data = pd.read_csv(url)

# 1.Número de casos de Contagiados en el País.
print(data['ID de caso'].count())

# 2. Número de Municipios Afectados.
data['Nombre municipio'].unique().size

# 3.Liste los municipios afectados (sin repetirlos)
print(data['Nombre municipio'].unique())

# 4.Número de personas que se encuentran en atención en casa
data['Ubicación del caso'].replace('Casa', 'casa', inplace=True)
data['Ubicación del caso'].replace('CASA', 'casa', inplace=True)

len(data[data['Ubicación del caso'] == 'casa'])
