"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re


def ingest_data():

    #
    # Inserte su código aquí
    #
    
    file_path = 'clusters_report.txt'

    with open(file_path, 'r') as file:
        lines = file.readlines()


    clusters = []
    cantidad_palabras = []
    porcentaje_palabras = []
    palabras_clave = []

    
    for line in lines:
       
        match = re.match(r'\s*(\d+)\s+(\d+)\s+([\d,\.]+\s?%)\s+(.+)', line)
        if match:
            clusters.append(int(match.group(1)))
            cantidad_palabras.append(int(match.group(2)))
            porcentaje_palabras.append(match.group(3))
            palabras_clave.append(match.group(4).split(','))

    
    data = {
        'Cluster': clusters,
        'Cantidad de palabras clave': cantidad_palabras,
        'Porcentaje de palabras clave': porcentaje_palabras,
        'Principales palabras clave': palabras_clave
    }

    df = pd.DataFrame(data)

    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(' ', '_')

    df["porcentaje_de_palabras_clave"] = df["porcentaje_de_palabras_clave"].str.replace('%', '')
    df["porcentaje_de_palabras_clave"] = df["porcentaje_de_palabras_clave"].str.replace(',', '.')
    df["porcentaje_de_palabras_clave"] = df["porcentaje_de_palabras_clave"].astype(float)

    keywords_list = []

    # Read the text from the file and extract the relevant parts
    with open(file_path, 'r') as file:
        text = file.read()
        # Extracting the relevant parts based on patterns
        pattern = r'\d+\s+\d+\s+\d+,\d+\s%\s+([\w\s,()-]+)\n'
        matches = re.findall(pattern, text)
        # Splitting the matches into lists
        keywords_list = [match.strip() for match in matches]
    #print(keywords_list)
    # Printing the lists
    # for idx, keywords in enumerate(keywords_list, start=1):
    #     print(f"{keywords}\n")  

    df["principales_palabras_clave"] = keywords_list

    return df

