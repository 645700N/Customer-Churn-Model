import pandas as pd
import numpy as np

data = pd.read_csv('dataset/Customer Churn Model.txt')

columnas_español = ['Estado', 'longitud de la cuenta', 'Codigo de area', 'Telefono',
                    'Plan internacional', 'plan VMail', 'Minutos VMail', 'Llamadas Diurnas',
                    'Cargo del dia','Minutos por la tarde', 'Llamadas por la tarde',
                    'Cargo por la tarde', 'Minutos Nocturnos', 'Llamadas Nocturnas',
                    'Cargo Nocturno', 'Minutos Internacionales', 'Llamdas Internacionales',
                    'Cargo Internacional', 'costo de servio por llamdas', 'Churn']

data2 = pd.read_csv('dataset/Customer Churn Model.txt', header=0, names=columnas_español)

print(data2.head())