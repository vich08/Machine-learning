# -*- coding: utf-8 -*-
""""Society's Healthscape

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T5VbtjdHtYQS71MWfzw69w2ynpHsnyuU

Vicente Vergara


Primeramente se importan las librerías Pandas, Mathplotlib.pyplot, Numpy y Seaborn; estas corresponden a librerías de Python que utilizaremos para poder desarrollar el análisis EDA, para el cual se analizará la base de datos KaggleV2-May-2016.

# Importación librerías

**INFORMACIÓN DEL DATASET**

El objetivo es realizar un análisis de las variables vislumbrando la relación que tienen con los cargos de las primas por el seguro para los clientes; para esto se utilizá una base de dato llamada "KaggleV2-May-2016". Esta corresponte a un archivo .csv con 14 variables las que corresponden a PatientId, AppointmentID, Gender, ScheduledDay, AppointmentDay, Age, Neighbourhood, Scholarship, Hipertension, Diabetes, Alcoholism, Handcap, SMS_received, No-show, cada columna cuenta con 110527 datos, lo que nos otorga recuento final de 1547364 datos.
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

hosp = pd.read_csv("/content/KaggleV2-May-2016.csv")

"""# Análisis macro"""

hosp.shape

hosp.columns

hosp.corr

hosp = hosp.drop(["PatientId", "AppointmentDay"], axis=1)

hosp.head()

hosp.tail()

hosp.head()

hosp.info()

hosp.describe()

"""Con esta funcion nos damos cuenta que no faltan datos, por lo tanto no habria necesidad de inventar o omitir columnas"""

hosp.groupby(['Gender','Neighbourhood'])[['Neighbourhood']].count()

hosp.groupby(['Gender','Neighbourhood'])[['Gender']].count()

hosp.groupby(['Gender','Hipertension','Diabetes','Alcoholism','Handcap'])[['Gender']].describe()

"""# Funciones"""



"""Decidimos eliminar 2 columnas las cuales consideramos que no aportan informacion relevante para el análisis que queremos realizar"""

EnfermedadesxVecindario = hosp['Hipertension'] + hosp['Diabetes'] + hosp['Alcoholism'] + hosp['Handcap']

"""Creamos una nueva variable haciendo una fusion entre enfermedades y vencindario, para poder analizar de mejor manera la cantidad de enfermos.
Esta variable se basa en sumar las enfermedades por individuo para saber cuantos enfermedades hay por vencindario o por grupo etareo.
"""

EnfermedadesxVecindario

hosp["EnfermedadesxVecindario"] = EnfermedadesxVecindario

"""Incluimos la funcion creada a una columna dentro de nuestro dataset para poder trabajarla"""

hosp[['Neighbourhood', 'EnfermedadesxVecindario']].groupby('Neighbourhood').sum()

"""Revisamos que nuestra variable se comportara de manera correcta"""

Enfermedades_vs_FM = hosp[["Gender","EnfermedadesxVecindario"]].groupby("Gender").sum()

Hipertension_vs_FM = hosp[["Gender","Hipertension"]].groupby("Gender").sum()

Diabetes_vs_FM = hosp[["Gender","Diabetes"]].groupby("Gender").sum()

Alcohol_vs_FM = hosp[["Gender","Alcoholism"]].groupby("Gender").sum()

Handcap_vs_FM = hosp[["Gender","Handcap"]].groupby("Gender").sum()

"""Creamos nuevas variables para empezar con nuestro análisis en este caso hacer relaciones entre las enfermedades y el género."""

def grupo_etareo (x):
  if(x < 18):
    return "Joven"

  if (x >= 18 and x < 60):
      return "Adulto"
  if (x >= 60):
    return "tercera edad"

"""Se define una nueva funcion que nos ayude a filtrar por el grupo etareo de las personas, para realizar un mejor analisis.

# Relacion de enfermedades y personas
"""

hosp[['Hipertension','Diabetes','Alcoholism','Handcap']].sum().plot(kind="bar", legend=False  )
plt.show()

"""# Relación Enfermedades y género"""

Enfermedades_vs_FM.plot(kind="bar", legend=False)
plt.show()

"""Yendo a un contexto más generalizado, las mujeres tienen muchas más de estas enfermedades que los mismos hombres."""

Alcohol_vs_FM.plot(kind="bar", legend=False)
plt.show()
#alcoholismo se puede apreciar una mayor tasa de alcoholismo en el genero masculino que en el femenino

"""Podemos ver en la imagen que el alcoholismo domina en más de un 30% a los hombres que en las mujeres"""

Diabetes_vs_FM.plot(kind="bar", legend=False)
plt.show()
#este es el de las diabetes
#se puede apreciar una mayor cantidad de diabetes en el genero femenino que en el masculino

"""Aqui podemos ver la diferencia que hay entre hombres y mujeres cuando hablamos de alcoholismo

Podemos visualizar que la Diabetes es más propensa encontrarla en mujeres, que en hombres al menos en estas muestras, ya que con estsos datos, podemos decir que las mujeres tienen un poco más del 60% esta enfermedad.
"""

Hipertension_vs_FM.plot(kind="bar", legend=False)
plt.show()

"""Podemos visualizar que la Hipertension es más propensa encontrarla en mujeres, que en hombres al menos en estas muestras, ya que con estsos datos, podemos decir que las mujeres tienen un poco más del 60% esta enfermedad."""

Handcap_vs_FM.plot(kind="bar", legend=False)
plt.show()

"""Con este grafico se puede apreciar que hay más mujeres sufriendo discapacidad que hombres.

# Relacion entre las enfermedades y el vecindario
"""

hosp[['Neighbourhood', 'EnfermedadesxVecindario']].groupby('Neighbourhood').sum().sort_values(by='EnfermedadesxVecindario',ascending=False)[0:10]

"""Aqui podemos ver los 10 vecindarios con más enfermedades"""

hosp

hosp_oficial

"""# Relación enfermedad y edad"""

hosp["Grupo etareo"] = hosp.Age.map(grupo_etareo)

hosp[['Grupo etareo','EnfermedadesxVecindario']].groupby('Grupo etareo').sum()

"""Con esta tabla podemos saber que la concentración de enfermedades estan en los grupos Adultos y de Tercera edad"""

EnfermdedadesxGrupoEtareo = hosp[['Grupo etareo','EnfermedadesxVecindario']].groupby('Grupo etareo').sum()

ax = EnfermdedadesxGrupoEtareo.plot(kind="bar", legend=False)

for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 5), textcoords='offset points')

plt.show()

conteo_zonas = hosp['Grupo etareo'].value_counts()

plt.pie(conteo_zonas, labels=conteo_zonas.index, autopct='%1.1f%%')
plt.title('Distribución de Personas por grupo etario')

plt.show()

"""Bueno aqui se puede apreciar la cantidad de personas que se encuentran en total y se puede observar que la mayoria son adultos de entre 18 a 60 años

Tabla para una mejor visualización de este problema

# Relacion citas y meses del año
"""

hosp['ScheduledDay'] = pd.to_datetime(hosp['ScheduledDay'])
# citas_por_mes = hosp.groupby(pd.Grouper(key='ScheduledDay', freq='M')).count()

hosp['ScheduledDay'] = pd.to_datetime(hosp['ScheduledDay'])
citas_por_mes = hosp.groupby(pd.Grouper(key='ScheduledDay', freq='M')).size()
suma_por_mes = citas_por_mes.sum()

"""Se intenta filtrar el formato de fechas para llevarlas a mes, para lograr una mejor visualización de las citas que tenia contemplada este hospital."""

citas_por_mes

data = {'Mes': citas_por_mes.index, 'Cantidad de Citas': citas_por_mes.values}
df = pd.DataFrame(data)

# Mostrar el DataFrame como una tabla
print(df)

plt.figure(figsize=(10, 6))
sns.lineplot(x=citas_por_mes.index, y=citas_por_mes.values, marker="o", color="b", label="Citas por Mes")
plt.title("Citas por Mes")
plt.xlabel("Mes")
plt.ylabel("Cantidad de Citas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

"""# Relacion citas y asistencia"""

def Asistencia1 (x):
  if(x == "No"):
    return 0

  if (x == "Yes"):
    return 1

"""Se crea una nueva variable para poder pasar a de valor str a int, y poder saber si las personas asistieron a las citas"""

hosp["Asistencia"] = hosp["No-show"].map(Asistencia1)

hosp

hosp[["No-show","Asistencia"]].groupby("No-show").count()

hosp

asist_por_mes = hosp[['ScheduledDay','Asistencia']].groupby(pd.Grouper(key='ScheduledDay', freq='M')).sum()

asist_por_mes

plt.figure(figsize=(10, 6))
sns.lineplot(x=citas_por_mes.index, y=citas_por_mes.values, marker="o", color="b", label="Citas por Mes")
sns.lineplot(x=asist_por_mes.index, y=asist_por_mes["Asistencia"], marker="o", color="r", label="Asistencia por Mes")
plt.title("Citas y Asistencia por Mes")
plt.xlabel("Mes")
plt.ylabel("Cantidad")
plt.xticks(rotation=45)
plt.tight_layout()
plt.legend()
plt.show()

"""# Relacion grupo etario y asistencia"""

hosp[['Grupo etareo','Asistencia','No-show']].groupby(['Grupo etareo','No-show']).count()

conteo_zonas = hosp[['Grupo etareo','No-show']].groupby(['Grupo etareo','No-show']).value_counts()

plt.pie(conteo_zonas, labels=conteo_zonas.index, autopct='%1.1f%%')
plt.title("Distribución de asistencia x Grupo etareo")

plt.show()

hosp[['Grupo etareo','Scholarship']].groupby('Grupo etareo').sum()

conteo_zonas = hosp['Scholarship'].value_counts()

plt.pie(conteo_zonas, labels=conteo_zonas.index, autopct='%1.1f%%')
plt.title('Cantidad de personas con beca de salud')

plt.show()

"""El 0 representa la cantidad de personas que tienen no la beca mientras que el 1 representa la cantidad que tienen."""

conteo_zonas = hosp[['Grupo etareo','Scholarship']].groupby('Grupo etareo').value_counts()

plt.pie(conteo_zonas, labels=conteo_zonas.index, autopct='%1.1f%%')
plt.title('Distribución de Personas con beca y sin beca por grupo etario')

plt.show()

"""En este grafico muestra lacantidad de personas con scholarship donde

*   0 significa que no tiene beca
*   1 significa que tiene beca

Con esto se puede deducir que hay mayor cantidad de gente sin scholarship

# Relación sms y citas
"""

hosp[['SMS_received','ScheduledDay']].groupby('SMS_received').count()

hosp[['SMS_received','ScheduledDay']].groupby('SMS_received').count().plot(kind="bar", legend=False  )

"""Se realiza comparacion de cantidad de citas y personas que recibieron un mensaje de recordatorio

# Relación sms y asistencia
"""

hosp[['SMS_received','Asistencia']].groupby('SMS_received').sum()

hosp[['SMS_received','Asistencia']].groupby('SMS_received').sum().plot(kind="bar", legend=False  )

"""Se realiza comparacion de personas que recibieron un recordatorio y asistieron a la cita, se ve que la mayoria de personas no recibió y asistió a la cita.

# Relacion entre asistencia a las citas y becas
"""

hosp[['Scholarship','Asistencia']].groupby('Scholarship').sum()

hosp[['Scholarship','Asistencia']].groupby('Scholarship').sum().plot(kind="bar", legend=False  )

"""Se muestra en el grafico la cantidad de personas que tienen una beca y como diferenciación:

*   0 no tiene beca
*   1 tiene beca

#CONCLUSIÓN

Inicialmente, trabajamos bajo la hipótesis de un análisis multivariado de 5 variables, ya que la información dentro del data set, nos permitiía trabajar mezclando gran cantidad de estas para hacer nuestro análisis.  Estas variables corresponden a: la edad o grupo etario, la cantidad de citas, asistencias, las enfermedades, y el genero

Para ello, se realizaron gráficos de los cuales se obtuvieron 4 conclusiones importantes. En primer lugar,al analizar la variable objetivo, se encontró que hubo un aumento en la cantidad de citas en junio del 2016 y luego tuvo una gran caída, pero esto no se veía reflejado en las asistencias, ya que las personas no tuvieron una gran asistencia en comparacion a la gran cantidad de citas(79,7% del total de personas no asitieron a su cita), teniendo en cuenta este dato, se decidio investigar sobre los mensajes que emitia el hospital a los pacientes, y logrando encontrar que la efectvidad de recepción de mensajes era bastante baja, ya que solo reciibian los mensajes un 30% de las personas, y es más independiente de que lo recibieran, más del 50% de las personas que recibieron los mensajes no iban a las citas medicas. En segundo lugar,luego de analizar las personas que tenian becas, se llego a que menos del 10% del universo que se consideró tenian becas y de ellos tan solo el 13% iba a las citas medicas, Por otro lado con el análisis realizado se encontró que el vecindario con mayor cantidad de enfermos era SANTA MARTHA, se observó que la mayoría de las personas que contenian una enfermedad eran principalmente mujeres. Por último, se analizó La cantidad de personas que tenian becas y se encontró que el grupo etario con menor catidad de becas era la tercera edad con un 2.6% con respecto al 11.5% de los adultos y el 11.2% de los jovenes.
"""

