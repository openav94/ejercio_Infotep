#IMPORTAR LIBRERIAS
import os
import pandas as pd
import matplotlib.pyplot as plt

# CARGA DE DATOS
titanic = pd.read_csv("TITANIC.csv")

while True:
    print(f"Menú de Operaciones:\n"
          f"1. Mostrar las primeras filas del conjunto de datos \n"
          f"2. Obtener información básica sobre el conjunto de datos \n"
          f"3. Estadísticas descriptivas para las columnas numéricas \n"
          f"4. Número de pasajeros en cada clase \n"
          f"5. Promedio de edad de los pasajeros \n"
          f"6. Tasa de supervivencia por género \n"
          f"7. Numero de pasajeros por Sex \n"
          f"8. Salir\n")

    opcion = input("Seleccione una opción (1-8): ")

    if opcion == '1':
        print(titanic.head())
    elif opcion == '2':
        print(titanic.info())
    elif opcion == '3':
        print(titanic.describe())
    elif opcion == '4':
        passenger_class_counts = titanic['Pclass'].value_counts()
        print(passenger_class_counts)

        # Gráfico de barras para el número de pasajeros en cada clase
        passenger_class_counts.plot(kind='bar')
        plt.title("Número de pasajeros por clase")
        plt.xlabel("Clase")
        plt.ylabel("Número de Pasajeros")
        plt.show()
    elif opcion == '5':
        average_age = titanic['Age'].mean()
        print(f"Promedio de edad: {round(average_age,2)} \n")
    elif opcion == '6':
        survival_gender = titanic.groupby('Sex')['Survived'].mean()
        print(survival_gender)
        # Gráfico de barras para la tasa de supervivencia por género
        survival_gender.plot(kind="bar")
        plt.title("Tasa de Supervivencia por Género")
        plt.xlabel("Género")
        plt.ylabel("Tasa de Supervivencia")
        plt.show()
    elif opcion == '7':
        passenger_sex_counts = titanic['Sex'].value_counts()
        print(passenger_sex_counts)

        # Gráfico de barras para el número de pasajeros por edad
        passenger_sex_counts.plot(kind='pie')
        plt.title("Número de pasajeros por Genero")
        plt.ylabel(" ")
        plt.show()

    elif opcion == '8':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente de nuevo.\n")