import pandas as pd
from connection import connect_to_database, retrieve_data

# Leer los datos de productos desde MongoDB y convertirlos en un DataFrame
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

# Conexión a la base de datos y obtención de los datos de productos
database = connect_to_database()
productos_collection = database["productos"]
df_productos = retrieve_data(productos_collection)

# Calcular el precio promedio de los productos
precio_promedio = df_productos["precio"].mean()
print("Precio promedio de los productos:", precio_promedio)
print()

# Contar la cantidad de productos por categoría
productos_por_categoria = df_productos["categoria"].value_counts()
print("Cantidad de productos por categoría:")
print(productos_por_categoria)
print()

# Obtener el producto más caro
producto_mas_caro = df_productos.loc[df_productos["precio"].idxmax()]
print("Producto más caro:")
print(producto_mas_caro)
print()