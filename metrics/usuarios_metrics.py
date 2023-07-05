import pandas as pd
from connection import connect_to_database, retrieve_data

# Leer los datos de usuarios desde MongoDB y convertirlos en un DataFrame
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

# Conexión a la base de datos y obtención de los datos de usuarios
database = connect_to_database()
usuarios_collection = database["usuarios"]
df_usuarios = retrieve_data(usuarios_collection)

# Obtener la cantidad total de usuarios
cantidad_usuarios = len(df_usuarios)
print("Cantidad total de usuarios:", cantidad_usuarios)
print()
# Encontrar el usuario con la mayor cantidad de pedidos en su historial
usuario_mas_pedidos = df_usuarios.loc[df_usuarios["historial_pedidos"].apply(lambda x: len(x) if isinstance(x, list) else 0).idxmax()]
print("Usuario con más pedidos en su historial:")
print(usuario_mas_pedidos)
print()
# Contar la cantidad de usuarios que tienen preferencia por las hamburguesas
usuarios_hamburguesas = df_usuarios[df_usuarios["preferencias_comida"].apply(lambda x: "Hamburguesas" in x if isinstance(x, list) else False)]
cantidad_usuarios_hamburguesas = len(usuarios_hamburguesas)
print("Cantidad de usuarios con preferencia por las hamburguesas:", cantidad_usuarios_hamburguesas)
print()
# Obtener la lista de usuarios que no tienen historial de pedidos
usuarios_sin_pedidos = df_usuarios[df_usuarios["historial_pedidos"].apply(lambda x: len(x) if isinstance(x, list) else 0) == 0]
lista_usuarios_sin_pedidos = usuarios_sin_pedidos["nombre"].tolist()
print("Usuarios sin historial de pedidos:")
print(lista_usuarios_sin_pedidos)
print()