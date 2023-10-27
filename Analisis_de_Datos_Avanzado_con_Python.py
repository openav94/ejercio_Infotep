import numpy as np
import pandas as pd

#Crear una lista de datos de ejemplo
data = [12, 15, 23, 25, 27, 15, 18, 20, 23, 25]

#Mostrar Lista
print(f"De la siguiente Lista se calculará: {data}")

#Calcular la media
mean = np.mean(data)
print("La Media es:", mean)

#Calcular la moda
mode = pd.Series(data).mode().values
print("La Moda es:", mode)

#Calcular la mediana
median = np.median(data)
print("La Mediana es:", median)

print("---------------------------------------------------------------")

#Calcular la desviación estándar
std_dev = np.std(data)
print(f"La Desviación Estandar es: {round(std_dev,2)}")

print("---------------------------------------------------------------")

#Calcular los cuartiles (Q1, Q2, Q3)
q1 = np.percentile(data, 25)
q2 = np.percentile(data, 50)
q3 = np.percentile(data, 75)
print(f"A continuación se muestran los Cuartiles calculados: \n"
      f"Q1 = {q1} \n"
      f"Q2 = {q2} \n"
      f"Q3 = {q3}")

print("---------------------------------------------------------------")
#Calcular el rango intercuartilico
iqr = q3 - q1
print(f"Rango Intercuartilico: {iqr}")

print("---------------------------------------------------------------")

#Crear un Dataframe con valores faltantes
data = pd.DataFrame({"A": [1, 2, np.nan, 4, 5], "B": [np.nan, 2, 3, 4, 5]})

#Impulsar los valores faltantes con la media
data.fillna(data.mean(), inplace=True)
print(data)

