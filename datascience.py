import pandas as pd
#import matplotlib as plt
#import seaborn as sns
import numpy as np

ruta_completa = "//Users/kevinalejandrocardenas/Desktop/Lista-de-clientes-con-nombre-y-direccion.xlsx"
df_clientes = pd.read_excel(ruta_completa)

print(df_clientes)#Muestra un resumen de la tabla 
print(df_clientes["ID"])#Murstra una columna indicada
print(df_clientes[["ID", "Dirección"]])#Muestra las columnas indicadas
print(df_clientes.head (10))#Muestra los  10 primeros
print(df_clientes[ "ventas totales"].) #calculará varias estadísticas resumidas para la columna, como el recuento de valores no nulos, la media, la desviación estándar, el valor mínimo, el percentil 25, la mediana (percentil 50), el percentil 75 y el valor máximo.

data = pd.concat([df_clientes["ID"], df_clientes["ventas totales"]], axis=1)#cocatenar columnas en una nueva tabala
print(data.head (10))