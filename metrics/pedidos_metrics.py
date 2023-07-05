import pandas as pd
from connection import connect_to_database, retrieve_data
from tabulate import tabulate
# Leer los datos de pedidos desde MongoDB y convertirlos en un DataFrame
def retrieve_data(collection):
    try:
        # Realizar consulta para recuperar los datos de la colección especificada
        data = collection.find()
        
        # Convertir los datos en un DataFrame de Pandas
        df = pd.DataFrame(list(data))
        
        return df
    except Exception as e:
        print("Error al recuperar datos:", str(e))
        return None

# Conexión a la base de datos y obtención de los datos de pedidos
database = connect_to_database()
pedidos_collection = database["pedidos"]
df_pedidos = retrieve_data(pedidos_collection)

# Convertir la columna "total" a tipo numérico
df_pedidos["total"] = pd.to_numeric(df_pedidos["total"])

# Calcular métricas de pedidos
promedio_monto = df_pedidos["total"].mean()
cantidad_total_pedidos = df_pedidos.shape[0]
maximo_monto = df_pedidos["total"].max()
minimo_monto = df_pedidos["total"].min()
suma_monto = df_pedidos["total"].sum()

# Imprimir métricas de pedidos
metricas_pedidos = [
["Promedio de monto de los pedidos:", promedio_monto],
["Cantidad total de pedidos realizados:", cantidad_total_pedidos],
["Monto máximo de los pedidos:", maximo_monto],
["Monto mínimo de los pedidos:", minimo_monto],
["Suma de los montos de los pedidos:", suma_monto]
]
print("metricas_pedidos: ")
print(tabulate(metricas_pedidos,headers="keys", tablefmt="psql"))
