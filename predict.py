import pickle
from constants import label_to_encoded, rng, sleep, Registros_por_Distrito, diccionario_idealista_m2
import numpy as np
import pandas as pd

# Cargar modelo desde el archivo pickle
with open("XGB_modelo_entrenado.pkl", 'rb') as file:
    modelo_cargado = pickle.load(file)
xgb_regressor = modelo_cargado["XGB_regressor"]

label_encoders = label_to_encoded # Diccionario en fichero constants.py del label encoding que se hizo durante el modelado

def encode_solicitud(solicitud, label_encoders): # Encode las columnas categoricas de la solicitud input para uso en nuestro modelo RFR
    """
    Encode las columnas categoricas del input dict solicitud usando el dict de label_encoders en fichero constants.py
    
    Parametros:
    - solicitud: dict
        El input diccionary con los campos a ser encoded.
    - label_encoders: dict de objetos LabelEncoder
        Diccionario que contiene objetos LabelEncoder para cada campo categorico a ser encoded.

    Returns:
    - encoded_solicitud: dict
        La version encoded del input solicitud.
    """
    
    encoded_solicitud = solicitud.copy()

    # Loop atraves de las keys en la solicitud que requieren de encoding
    for key in ['Tipo', 'Distrito', 'Barrio']:
        if key in encoded_solicitud:
            encoded_solicitud[key] = label_encoders[key][encoded_solicitud[key]]
    
    encoded_solicitud_list = []
    encoded_solicitud_list.append(encoded_solicitud)
    return encoded_solicitud_list

def estimacion(encoded_solicitud_list, area, distrito): # Usar la encoded solicitud para hacer la estimacion de precio mensual
    """
    Utiliza la encoded_solicitud para hacer la prediccion usando modelo xgb_regressor
    
    Parametros:
    - encoded_solicitud: dict
        El input diccionary con los campos categoricos encoded.

    Returns:
    - predicted_price: int
        La version encoded del input solicitud.
    """

    # Predecir el precio de renta para el nuevo_listing
    data = pd.DataFrame(encoded_solicitud_list)
    data['Furnished'] = data['Furnished'].astype('category')
    predicted_price = xgb_regressor.predict(data)
    predicted_price = int(np.around(predicted_price, -2)[0])

    # Validar y hacer ajustes al predicted_price
    predicted_price = int(modified_price(predicted_price, area, distrito))

    #Un pequeño delay en el calculo
    time_to_sleep = rng.uniform(1, 3)
    sleep(time_to_sleep)

    return predicted_price

def query(tipo, distrito, barrio, hab, banos, area, furnished):
    """
    Utiliza los inputs del usuario web para generar una solicitud encodificada
    
    Parametros:
    - tipo: texto
        El input de tipo de vivienda
    - distrito: texto
        El input de distrito de Madrid donde esta ubicada la vivienda
    - barrio: texto
        El input de barrio de Madrid donde esta ubicada la vivienda
    - hab: numero
        El input de numero de habitaciones de la vivienda
    - banos: numero
        El input de numero de banos de la vivienda
    - area: numero
        El input de area (en m2) de la vivienda
    - furnished: numero 
        1 = Amueblado y 0 = Sin Amueblar
        
    Returns:
    - encoded_solicitud: dict
        La version encoded del input solicitud.
    """

    # Se llena el diccionario solicitud con los inputs del usuario en la web.
    solicitud = {
        "Tipo" : tipo,
        "Distrito" : distrito,
        "Barrio" : barrio,
        "Habitaciones" : hab,
        "Banos" : banos,
        "Area" : area,
        "Furnished" : furnished
    }
    # Proceder con encoding la solicitud
    encoded_solicitud = encode_solicitud(solicitud, label_encoders)

    return encoded_solicitud   

def fiability(distrito):
    """
    Revisar el numero de registros de viviendas en el distrito solicitado en el query para dar una metrica
    de fiabilidad del modelo.
    
    Parametros:
    - distrito: texto
        El input de distrito de Madrid donde esta ubicada la vivienda

    Returns:
    - fiabilidad: texto
        La metrica de fiabilidad (Alta/Media/Baja)
    """
    # Revisar numero de registros en el distrito del query
    number = Registros_por_Distrito[distrito]

    if number >= 1000:
        return "Fiabilidad Alta"
    elif 300 < number < 1000:
        return "Fiabilidad Media"
    elif number < 300:
        return "Fiabilidad Baja"

def modified_price(predicted_price, area, distrito):

    """
    
    Ponderación de la predicción del modelo según la precisión contra la tabla de estimaciones por m2 de idealista
    
    Parametros:
    - predicted_price: int
        La predicción de precio del XGB
    - area: texto
        Area en metros cuadrados de la vivienda
    - distrito: texto
        El input de distrito de Madrid donde esta ubicada la vivienda

    Returns:
    - modified_price: float
        Precio tras ponderar según fiabilidad contra la tabla de estimaciones de idealista
        
    """
    

    #funcion de fiabilidad para tres clases, alta media baja, con la tabla de idealista por barrio

    precision_diana = (.84, .76, .74)
    if fiability(distrito) ==  "Fiabilidad Alta":
        alpha = precision_diana[0]
    elif fiability(distrito) ==  "Fiabilidad Media":
        alpha = precision_diana[1]
    else: alpha = precision_diana[2]

    modified_price = ((((alpha)*(predicted_price / area) + (1-alpha) * diccionario_idealista_m2[distrito])) * area )

    return modified_price
