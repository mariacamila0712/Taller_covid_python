# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 15:14:56 2021

@author: Maria Camila
"""

import pandas as pd

url = 'covid_22_noviembre.csv'
data = pd.read_csv(url)

# Número de casos de Contagiados en el País.
print(data['ID de caso'].count())
