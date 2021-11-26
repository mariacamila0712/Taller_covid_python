# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 15:14:56 2021

@author: Maria Camila
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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
tipo_caso = data.groupby(
    'Tipo de contagio').size().sort_values(ascending=False)
print(f'Orden de mayor a menor por tipo de caso: {tipo_caso} ')
print('-----------------------------------------------------------------')

# 8.Número de departamentos afectados
data['Nombre departamento'].replace('Caldas', 'CALDAS', inplace=True)
data['Nombre departamento'].replace('caldas', 'CALDAS', inplace=True)
data['Nombre departamento'].replace('Tolima', 'TOLIMA', inplace=True)
num_dep_afectados = data['Nombre departamento'].unique().size
print(f'El número de departamentos afectados es: {num_dep_afectados}')
print('-----------------------------------------------------------------')

# 9.Liste los departamentos afectados(sin repetirlos)
lista_dep_afectados = data['Nombre departamento'].unique()
print(f'Lista de departamentos afectados es: {lista_dep_afectados}')
print('-----------------------------------------------------------------')

# 10.Ordene de mayor a menor por tipo de atención
tipo_atencion = data.groupby(
    'Ubicación del caso').size().sort_values(ascending=False)
print(f'Orden de mayor a menor por tipo de atención es: {tipo_atencion}')
print('-----------------------------------------------------------------')

# 11.Liste de mayor a menor los 10 departamentos con mas casos de contagiados
dep_mas_contagiados = data.groupby(
    'Nombre departamento').size().sort_values(ascending=False).head(10)
print(
    f'Los 10 departamentos con mas casos de contagiados son: {dep_mas_contagiados}')
print('-----------------------------------------------------------------')

# 12.Liste de mayor a menor los 10 departamentos con mas casos de fallecidos
dep_mas_fallecidos = data[data['Recuperado'] == 'fallecido'].groupby(
    'Nombre departamento').size().sort_values(ascending=False).head(10)
print(
    f'Los 10 departamentos con mas casos de fallecidos son: {dep_mas_fallecidos}')
print('-----------------------------------------------------------------')

# 13.Liste de mayor a menor los 10 departamentos con mas casos de
dep_mas_recuperados = data[data['Recuperado'] == 'Recuperado'].groupby(
    'Nombre departamento').size().sort_values(ascending=False).head(10)
print(
    f'Los 10 departamentos con mas casos de recuperados son: {dep_mas_recuperados}')
print('-----------------------------------------------------------------')

# 14.Liste de mayor a menor los 10 municipios con mas casos de contagiados
mun_mas_contagiados = data.groupby(
    'Nombre municipio').size().sort_values(ascending=False).head(10)
print(
    f'Los 10 municipios con mas casos de contagiados son: {mun_mas_contagiados}')
print('-----------------------------------------------------------------')

# 15. Liste de mayor a menor los 10 municipios con mas casos de fallecidos
mun_mas_fallecidos = data[data['Recuperado'] == 'fallecido'].groupby(
    'Nombre municipio').size().sort_values(ascending=False).head(10)
print(
    f'Los 10 municipios con mas casos de fallecidos son: {mun_mas_fallecidos}')
print('-----------------------------------------------------------------')

# 16.Liste de mayor a menor los 10 municipios con mas casos de recuperados
mun_mas_recuperados = data[data['Recuperado'] == 'Recuperado'].groupby(
    'Nombre municipio').size().sort_values(ascending=False).head(10)
print(
    f'Los 10 municipios con mas casos de recuperados son: {mun_mas_recuperados}')
print('-----------------------------------------------------------------')

# 17.Liste agrupado por departamento y en orden de Mayor a menor las ciudades con mas casos de contagiados
dep_ciudades_mas_contagiados = data.groupby(['Nombre departamento', 'Nombre municipio']
                                            ).size().sort_values(ascending=False)
print(
    f'Departamentos agrupados por ciudades con mas casos: {dep_ciudades_mas_contagiados}')
print('-----------------------------------------------------------------')

# 18.Número de Mujeres y hombres contagiados por ciudad por departamento
hom_muj_conta_depar = data.groupby(['Nombre departamento', 'Nombre municipio',
                                    'Sexo']).size().sort_values(ascending=False)
print(
    f'El número de mujeres y hombres contagiados por ciudades y departamentos es: {hom_muj_conta_depar}')
print('-----------------------------------------------------------------')

# 19. Liste el promedio de edad de contagiados por hombre y mujeres por ciudad por departamento
prom_edad_hom_muj = data.groupby(['Nombre departamento','Nombre municipio', 'Sexo']).Edad.mean()
print(f'EL promedio de edad de contagiados por hombre y mujeres por ciudad por departamentos es : {prom_edad_hom_muj}')
print('-----------------------------------------------------------------')

# 20.Liste de mayor a menor el número de contagiados por país de procedencia
conta_pais_procedencia = data.groupby('Nombre del país').size().sort_values(ascending=False)
print(f'Lista de mayor a menor contagiados por pais de procedencia: {conta_pais_procedencia}')
print('-----------------------------------------------------------------')

# 21. Liste de mayor a menor las fechas donde se presentaron mas contagios
fecha_mas_contagiados = data.groupby('Fecha de diagnóstico').size().sort_values(ascending=False)
print(f'Fecha de mayor a menor donde se presentaron mas contagiados : {fecha_mas_contagiados}')
print('-----------------------------------------------------------------')
