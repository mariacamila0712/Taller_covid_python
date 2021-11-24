# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 15:14:56 2021

@author: Maria Camila
"""

import pandas as pd

url = 'covid_22_noviembre.csv'
data = pd.read_csv(url)

# 1.Número de casos de Contagiados en el País.
contagios = data['ID de caso'].count()
print(f'El número de casos en el pais es: {contagios}')
print('-----------------------------------------------------------------')

# 2. Número de Municipios Afectados.
municipios_afectados = data['Nombre municipio'].unique().size
print(f'El número de municipios afectados es: {municipios_afectados}')
print('-----------------------------------------------------------------')

# 3.Liste los municipios afectados (sin repetirlos)
lista_mun_afectados = data['Nombre municipio'].unique()
print(f'Lista de municipios afectados es: {lista_mun_afectados}')
print('-----------------------------------------------------------------')

# 4.Número de personas que se encuentran en atención en casa
data['Ubicación del caso'].replace('Casa', 'casa', inplace=True)
data['Ubicación del caso'].replace('CASA', 'casa', inplace=True)
per_aten_casa = len(data[data['Ubicación del caso'] == 'casa'])
print(f'Numero de personas atencion en casa es: {per_aten_casa}')
print('-----------------------------------------------------------------')

# 5.Número de personas que se encuentran recuperados
pers_recuperadas = len(data[data['Recuperado'] == 'Recuperado'])
print(f'Numero de personas recuperadas es: {pers_recuperadas}')
print('-----------------------------------------------------------------')

# 6.Número de personas que ha fallecido
data['Recuperado'].replace('Fallecido', 'fallecido', inplace=True)
pers_fallecidas = len(data[data['Recuperado'] == 'fallecido'])
print(f'Numero de personas fallecidas es: {pers_fallecidas}')
print('-----------------------------------------------------------------')

# 7.Orden de Mayor a menor por tipo de caso (Importado, en estudio,Relacionado)
tipo_caso = data.groupby('Tipo de contagio').size().sort_values(ascending=False)
print(f'Orden de mayor a menor por tipo de caso: {tipo_caso} ')
print('-----------------------------------------------------------------')