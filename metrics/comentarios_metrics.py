import pandas as pd
from tabulate import tabulate
from connection import connect_to_database, retrieve_data

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
pedidos_collection = database["comentarios"]
df_pedidos = retrieve_data(pedidos_collection)

# Contar la cantidad de comentarios por sucursal
comentarios_por_sucursal = df_pedidos.groupby("sucursal_id").size().reset_index(name="Cantidad de comentarios")
print("Cantidad de comentarios por sucursal:")
print(tabulate(comentarios_por_sucursal, headers="keys", tablefmt="psql"))
print()

# Comentarios más recientes
comentarios_recientes = df_pedidos.sort_values("fecha", ascending=False).head(3)
print("Comentarios más recientes:")
print(tabulate(comentarios_recientes, headers="keys", tablefmt="psql"))
print()

# Comentarios más largos
df_pedidos["longitud_comentario"] = df_pedidos["comentario"].apply(lambda x: len(x))
comentarios_largos = df_pedidos.sort_values("longitud_comentario", ascending=False).head(3)
print("Comentarios más largos:")
print(tabulate(comentarios_largos, headers="keys", tablefmt="psql"))