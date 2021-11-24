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

print('-----------------------------------------------------------------')

# 2. Número de Municipios Afectados.
print(data['Nombre municipio'].unique().size)
print('-----------------------------------------------------------------')

# 3.Liste los municipios afectados (sin repetirlos)
print(data['Nombre municipio'].unique())
print('-----------------------------------------------------------------')

# 4.Número de personas que se encuentran en atención en casa
data['Ubicación del caso'].replace('Casa', 'casa', inplace=True)
data['Ubicación del caso'].replace('CASA', 'casa', inplace=True)

print(len(data[data['Ubicación del caso'] == 'casa']))
print('-----------------------------------------------------------------')

# 5.Número de personas que se encuentran recuperados
print(len(data[data['Recuperado'] == 'Recuperado']))
print('-----------------------------------------------------------------')

# 6.Número de personas que ha fallecido
data['Recuperado'].replace('Fallecido', 'fallecido', inplace=True)
print(len(data[data['Recuperado'] == 'fallecido']))
print('-----------------------------------------------------------------')
