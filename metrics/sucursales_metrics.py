import pandas as pd
from connection import connect_to_database, retrieve_data

# Leer los datos de sucursales desde MongoDB y convertirlos en un DataFrame
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

# Conexión a la base de datos y obtención de los datos de sucursales
database = connect_to_database()
sucursales_collection = database["sucursales"]
df_sucursales = retrieve_data(sucursales_collection)

# Obtener la cantidad total de sucursales
cantidad_sucursales = len(df_sucursales)
print("Cantidad total de sucursales:", cantidad_sucursales)
print()
# Calcular la capacidad promedio de las sucursales
capacidad_promedio = df_sucursales["capacidad"].mean()
print("Capacidad promedio de las sucursales:", capacidad_promedio)
print()
# Encontrar la sucursal con la mayor capacidad
sucursal_mayor_capacidad = df_sucursales.loc[df_sucursales["capacidad"].idxmax()]
print("Sucursal con mayor capacidad:")
print(sucursal_mayor_capacidad)
print()
# Contar la cantidad de sucursales que ofrecen el servicio de Delivery
sucursales_con_delivery = df_sucursales[df_sucursales["servicios_ofrecidos"].apply(lambda x: "Delivery" in x)]
cantidad_sucursales_con_delivery = len(sucursales_con_delivery)
print("Cantidad de sucursales que ofrecen Delivery:", cantidad_sucursales_con_delivery)
print()
# Obtener la lista de sucursales con horario de atención antes de las 9:00 AM
sucursales_antes_9am = df_sucursales[df_sucursales["horario"].apply(lambda x: int(x.split(":")[0]) < 9)]
lista_sucursales_antes_9am = sucursales_antes_9am["nombre"].tolist()
print("Sucursales con horario antes de las 9:00 AM:")
print(lista_sucursales_antes_9am)
print()