import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('dataset/Customer Churn Model.txt')

columnas_español = ['Estado', 'longitud de la cuenta', 'Codigo de area', 'Telefono',
                    'Plan internacional', 'plan VMail', 'Minutos VMail', 'Llamadas Diurnas',
                    'Cargo del dia','Minutos por la tarde', 'Llamadas por la tarde',
                    'Cargo por la tarde', 'Minutos Nocturnos', 'Llamadas Nocturnas',
                    'Cargo Nocturno', 'Minutos Internacionales', 'Llamdas Internacionales',
                    'Cargo Internacional', 'costo de servio por llamdas', 'Churn']

data2 = pd.read_csv('dataset/Customer Churn Model.txt', header=0, names=columnas_español)


#Filtrado de personas con el plan internacional (type=df)
df_intl_plan = data[data["Int'l Plan"] == 'yes']
#Columna de personas con el plan internacional (type=series)
intl_plan = df_intl_plan["Int'l Plan"]
#Columna de minutos internacionael de personas que poseen el plan internacional (type=series)
intl_mins = df_intl_plan["Intl Mins"]

#filtrado por iloc(basado en posicion) y loc(basado en etiqueta)
sample_data = data.iloc[:20, 3:6]
sample_data1 = data.iloc[:20, [2,4,6]]

sample_data2 = data.loc[:20, ['State', 'Day Mins']]

#Estados unicos en el dataframe (states=51)
states = data['State'].drop_duplicates()
    

data['Total Mins'] = (data['Day Mins'] + data['Night Mins'] + data['Eve Mins'])
data['Total Calls'] = (data['Day Calls'] + data['Night Calls'] + data['Eve Calls'])
data['Total Charge'] = (data['Day Charge'] + data['Night Charge'] + data['Eve Charge'])

#Recorrera la lista de estados y sumara el total de llamadas por estado, almacenando los valores en una lista
state_list = []
for x in states:
    state = sum(data[data['State'] == x].iloc[:, 22])
    state_list.append(state)

states = states.tolist()
total_state_calls = pd.DataFrame(state_list, states)
print(total_state_calls)

plt.bar(states, state_list)
plt.xticks(rotation=60, horizontalalignment='left')
plt.show()