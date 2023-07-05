# Proyecto de Big Data Bembos

[![Build Status](https://img.shields.io/travis/tu-usuario/proyecto-bigdata-bembos.svg)](https://travis-ci.org/tu-usuario/proyecto-bigdata-bembos)
[![Python Version](https://img.shields.io/badge/python-3.11%20%7C%203.8%20%7C%203.9-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/tu-usuario/proyecto-bigdata-bembos/blob/main/LICENSE)

---

Este proyecto de Big Data tiene como objetivo realizar análisis exploratorio y visualización de datos para el caso de estudio de la empresa Bembos. Utilizaremos MongoDB, Python y Pandas para extraer y procesar los datos, calcular métricas relevantes y generar visualizaciones imformativas

## Tabla de contenidos
- [Estructura de carpetas](#estructura-de-carpetas)
- [Instrucciones de uso](#instrucciones-de-uso)
- [Requisitos del sistena](#requisitos)
- [Instalacion](#instalación)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)
- [Contacto](#contacto)

## Estructura de carpetas

```cmd
- bembos-bigdata-project/
    - data_processing/
        - __init__.py
        - data_processing.py
    - database_operations/
        - __init__.py
        - database_operations.py
    - analysis/
        - __init__.py
        - analysis.py
    - notebooks/
        - exploratory_analysis.ipynb
        - data_visualization.ipynb

```
- **data_processing:** Contiene el archivo `data_processing.py`, donde se implementa la lógica para procesar los datos de Bembos

- **database_operations:** Contiene el archivo `database_operations.py`, donde se establece la conexión con MongoDb y se definen las operaciones de recuperación de datos

- **analysis:** Contiene el archivo `analysis.py`, donde se calculan las métricas relacionadas con las ventas de Bembos

- **notebooks:** Contiene los notebooks de Jypiter para realizar el análisis exploratorio y la visualización de datos

## Instrucciones de uso

1. Clona este repositorio en tu máquina local
2. Asegúrate de tener MongoDB instalado y en ejecución
3. Instala las dependencias necesarias especificadas en el archivo 'requirements.txt'
4. Ejecuta el notebook `exploratory_analysis.ipynb` para realizar el análisis exploratorio de los datos y calcular las métricas relevantes
5. Ejecuta el notebook `data_visualization.ipynb` para generar visualizaciones a partir de los datos analizados
6. Explora y modifica los notebooks según tus necesidades

## Requisitos

- Python 3.x
- MongoDB
- Pandas
- Matplotlib
- Jypyter Notebook

## Instalación

1. Clona este repositorio en tu máquina local utilizando el sgte comando:
```
git clone https://github.com/70993543/Bembos-bigdata-project.git
```

2. Navega hasta el directorio del proyecto

```
cd proyecto-bigdata-bembos
```

3. Crea un entorno virtual

```cmd
py -m venv env
```

4. instala las dependencias necesarias utlizando `pip`

```
píp install -r requirements.txt
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas colaborar en el proyecto, sigue los sgtes pasos:
1. Realiza un fork del repositorio
2. Crea una rama con una descripción clara de la función que desees implementar
3. Envia un pull request describiendo tus cambios y explicando tu propósito

## Licencia

Este proyecto se encuentra bajo Licencia MIT. Puedes consultar el archivo 'LICENCE' para obtener más información

## Contacto

Si tienes alguna preguna o consulta relacionada con este proyecto, no dudes en ponerte en contacto con nuestro equipo:

Equipo de Desarrollo:

- Nombre: Bryan
  - Correo electrónico: [![Email](https://img.shields.io/badge/Email-tu--correo%40ejemplo.com-blue)](mailto:tu-correo@ejemplo.com)
  - GitHub: [![GitHub followers](https://img.shields.io/github/followers/tu-usuario?style=social)](https://github.com/tu-usuario)
  - LinkedIn: [![LinkedIn](https://img.shields.io/badge/LinkedIn-Perfil-blue)](https://www.linkedin.com/in/tu-usuario)

- Nombre: Alexander
  - Correo electrónico: [![Email](https://img.shields.io/badge/Email-correo%40ejemplo.com-blue)](mailto:correo@ejemplo.com)
  - GitHub: [![GitHub followers](https://img.shields.io/github/followers/miembro2?style=social)](https://github.com/miembro2)
  - LinkedIn: [![LinkedIn](https://img.shields.io/badge/LinkedIn-Perfil-blue)](https://www.linkedin.com/in/miembro2)

- Nombre: Victor
  - Correo electrónico: [![Email](https://img.shields.io/badge/Email-correo%40ejemplo.com-blue)](mailto:correo@ejemplo.com)
  - GitHub: [![GitHub followers](https://img.shields.io/github/followers/miembro3?style=social)](https://github.com/miembro3)
  - LinkedIn: [![LinkedIn](https://img.shields.io/badge/LinkedIn-Perfil-blue)](https://www.linkedin.com/in/miembro3)

- Nombre: Axel
  - Correo electrónico: [![Email](https://img.shields.io/badge/Email-correo%40ejemplo.com-blue)](mailto:correo@ejemplo.com)
  - GitHub: [![GitHub followers](https://img.shields.io/github/followers/miembro3?style=social)](https://github.com/miembro3)
  - LinkedIn: [![LinkedIn](https://img.shields.io/badge/LinkedIn-Perfil-blue)](https://www.linkedin.com/in/miembro3)