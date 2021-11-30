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

# 13.Liste de mayor a menor los 10 departamentos con mas casos recuperados
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

# 22. Diga cual es la tasa de mortalidad y recuperación que tiene toda Colombia
tasa_mortalidad = ((len(data[data['Recuperado'] == 'fallecido'])) * 100) / (len(data))
print(f'La tasa de mortalidad en toda Colombia es: {tasa_mortalidad}')
print('-----------------------------------------------------------------')
tasa_recuperacion = ((len(data[data['Recuperado'] == 'Recuperado'])) * 100) / (len(data))
print(f'La tasa de recuperación en toda Colombia es: {tasa_recuperacion}')
print('-----------------------------------------------------------------')

# 23.Liste la tasa de mortalidad y recuperación que tiene cada departamento
tasa_mortalidad_dep = (data[data['Recuperado'] == 'fallecido'].groupby('Nombre departamento').size() / len(data)) * 100
print(f'La lista por tasa de mortalidad en por departamento es: {tasa_mortalidad_dep}')
print('-----------------------------------------------------------------')

tasa_recuperacion_dep = (data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size() / len(data)) * 100
print(f'La lista por tasa de recuperación por departamento es: {tasa_recuperacion_dep}')
print('-----------------------------------------------------------------')

# 24. Liste la tasa de mortalidad y recuperación que tiene cada ciudad
tasa_mortalidad_mun = (data[data['Recuperado'] == 'fallecido'].groupby('Nombre municipio').size() / len(data)) * 100
print(f'La lista por tasa de mortalidad en por ciudad es: {tasa_mortalidad_mun}')
print('-----------------------------------------------------------------')

tasa_recuperacion_mun = (data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size() / len(data)) * 100
print(f'La lista por tasa de recuperación por municipio es: {tasa_recuperacion_mun}')
print('-----------------------------------------------------------------')

# 25. Liste por cada ciudad la cantidad de personas por atención
ciudad_atencion = data.groupby(['Nombre municipio', 'Recuperado']).size().sort_values()
print(f'Lista de ciudades por la cantidad de atención: {ciudad_atencion}')
print('-----------------------------------------------------------------')

# 26. Liste el promedio de edad por sexo por cada ciudad de contagiados
data['Nombre municipio'].replace('puerto colombia', 'PUERTO COLOMBIA', inplace=True)
prom_edad_sexo_ciudad = data.groupby(['Nombre municipio','Sexo']).Edad.mean()
print(f'Lista de promedios de edad por sexo por cada ciudad de contagiados: {prom_edad_sexo_ciudad}')
print('-----------------------------------------------------------------')

# 27. Grafique las curvas de contagio, muerte y recuperación de toda Colombia acumulados
curva_contagio = data[data['Recuperado'] == 'fallecido'].groupby('Fecha de diagnóstico').size().sort_values().plot()
print('La curva de contagio es: ')
plt.show(curva_contagio)
print('-----------------------------------------------------------------')

curva_fallecidos = data[data['Recuperado'] == 'fallecido'].groupby('Fecha de diagnóstico').size().sort_values().plot()
print('La curva de fallecidos es: ')
plt.show(curva_fallecidos)
print('-----------------------------------------------------------------')

curva_recuperados = data[data['Recuperado'] == 'Recuperado'].groupby('Fecha de diagnóstico').size().sort_values().plot()
print('La curva de recuperados es: ')
plt.show(curva_recuperados)
print('-----------------------------------------------------------------')

# 28. Grafique las curvas de contagio, muerte y recuperación de los 10 departamentos con mas casos de contagiados acumulados
contagios_10_dep = data.groupby('Nombre departamento').size().sort_values(ascending = False).head(10).plot()
print('La curva de contagio en los 10 departamentos con mas casos es: ')
plt.show(contagios_10_dep)
print('-----------------------------------------------------------------')

fallecidos_10_dep = data[data['Recuperado'] == 'fallecido'].groupby('Nombre departamento').size().sort_values(ascending = False).head(10).plot()
print('La curva de fallecidos en los 10 departamentos con mas casos es: ')
plt.show(fallecidos_10_dep)
print('-----------------------------------------------------------------')

recuperados_10_dep = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size().sort_values(ascending = False).head(10).plot()
print('La curva de recuperados en los 10 departamentos con mas casos es: ')
plt.show(recuperados_10_dep)
print('-----------------------------------------------------------------')

# 29. Grafique las curvas de contagio, muerte y recuperación de las 10 ciudades con mas casos de contagiados acumulados
contagiados_10_ciu = data.groupby('Ubicación del caso').size().sort_values(ascending = False).head(10).plot()
print('La curva de contagios en las 10 ciudades con mas casos es: ')
plt.show(contagiados_10_ciu)
print('-----------------------------------------------------------------')

fallecidos_10_ciu = data[data['Recuperado'] == 'fallecido'].groupby('Ubicación del caso').size().sort_values(ascending = False).head(10).plot()
print('La curva de fallecidos en las 10 ciudades con mas casos es: ')
plt.show(fallecidos_10_ciu)
print('-----------------------------------------------------------------')

recuperados_10_ciu = data[data['Recuperado'] == 'Recuperado'].groupby('Ubicación del caso').size().sort_values(ascending = False).head(10).plot()
print('La curva de recuperados en las 10 ciudades con mas casos es: ')
plt.show(recuperados_10_ciu)
print('-----------------------------------------------------------------')

# 30.  Liste de mayor a menor la cantidad de fallecidos por edad en toda Colombia.
fallecidos_edad = data[data['Recuperado'] == 'fallecido'].groupby('Edad').size().sort_values(ascending = False)
print(f'La cantidad de fallecidos por edad organizados de forma descendente es: {fallecidos_edad}')
print('-----------------------------------------------------------------')

# 31. Liste el porcentaje de personas por atención de toda Colombia
porcentaje_atencion = ((data.groupby('Ubicación del caso').size().sort_values(ascending = False)) / ((data.groupby('Ubicación del caso').size().sort_values(ascending = False)).sum())) * 100
print(f'La lista de porcentajes por atencion en toda Colombia es: {porcentaje_atencion} ')
print('-----------------------------------------------------------------')

# 32.  Haga un gráfico de barras por atención de toda Colombia
