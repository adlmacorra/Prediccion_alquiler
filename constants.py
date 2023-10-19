# For random generation of numbers (sleep time)
from time import sleep
from numpy.random import default_rng
rng = default_rng()


# Encoded Labels Dict
label_to_encoded = {'Tipo': {'Apartamento': 0, 'Dúplex': 1, 'Piso': 2, 'Ático': 3, 'Chalet': 2},
                            
                            'Distrito': {'Arganzuela': 0,
                            'Barajas': 1,
                            'Carabanchel': 2,
                            'Centro': 3,
                            'Chamartín': 4,
                            'Chamberí': 5,
                            'Ciudad Lineal': 6,
                            'Fuencarral': 7,
                            'Hortaleza': 8,
                            'Latina': 9,
                            'Moncloa': 10,
                            'Moratalaz': 11,
                            'Puente de Vallecas': 12,
                            'Retiro': 13,
                            'Salamanca': 14,
                            'San Blas': 15,
                            'Tetuán': 16,
                            'Usera': 17,
                            'Vicálvaro': 18,
                            'Villa de Vallecas': 19,
                            'Villaverde': 20},

                            'Barrio': {'Abrantes': 0,
                            'Acacias': 1,
                            'Adelfas': 2,
                            'Alameda de Osuna': 3,
                            'Almagro': 4,
                            'Almenara': 5,
                            'Almendrales': 6,
                            'Aluche': 7,
                            'Ambroz': 8,
                            'Amposta': 9,
                            'Apóstol Santiago': 10,
                            'Arapiles': 11,
                            'Aravaca': 12,
                            'Arcos': 13,
                            'Argüelles': 14,
                            'Atalaya': 15,
                            'Atocha': 16,
                            'Bellas Vistas': 17,
                            'Bernabéu - Hispanoamérica': 18,
                            'Berruguete': 19,
                            'Buenavista': 20,
                            'Butarque': 21,
                            'Campamento': 22,
                            'Canillas': 23,
                            'Canillejas': 24,
                            'Casa de Campo': 25,
                            'Casco Histórico de Barajas': 26,
                            'Casco Histórico de Vallecas': 27,
                            'Casco histórico de Vicálvaro': 28,
                            'Castellana': 29,
                            'Castilla': 30,
                            'Castillejos': 31,
                            'Centro': 32,
                            'Chamartín': 33,
                            'Chamberí': 34,
                            'Chopera': 35,
                            'Ciudad Jardín': 36,
                            'Ciudad Universitaria': 37,
                            'Colina': 38,
                            'Comillas': 39,
                            'Concepción': 40,
                            'Corralejos - Campo de las Naciones': 41,
                            'Cortes - Huertas': 42,
                            'Costillares': 43,
                            'Cuatro Caminos': 44,
                            'Cuatro vientos': 45,
                            'Delicias': 46,
                            'El Cañaveral - Los Berrocales': 47,
                            'El Pardo': 48,
                            'El Viso': 49,
                            'Embajadores - Lavapiés': 50,
                            'Ensanche de Vallecas - Valdecarros': 51,
                            'Entrevías': 52,
                            'Estrella': 53,
                            'Fontarrón': 54,
                            'Fuente del Berro': 55,
                            'Fuentelarreina': 56,
                            'Gaztambide': 57,
                            'Goya': 58,
                            'Guindalera': 59,
                            'Hellín': 60,
                            'Horcajo': 61,
                            'Ibiza': 62,
                            'Imperial': 63,
                            'Jerónimos': 64,
                            'Justicia - Chueca': 65,
                            'La Florida - El Plantío': 66,
                            'La Paz': 67,
                            'Las Tablas': 68,
                            'Legazpi': 69,
                            'Lista': 70,
                            'Los Cármenes': 71,
                            'Los Rosales': 72,
                            'Los Ángeles': 73,
                            'Lucero': 74,
                            'Marroquina': 75,
                            'Media Legua': 76,
                            'Mirasierra': 77,
                            'Montecarmelo': 78,
                            'Moscardó': 79,
                            'Niño Jesús': 80,
                            'Nueva España': 81,
                            'Nuevos Ministerios - Ríos Rosas': 82,
                            'Numancia': 83,
                            'Opañel': 84,
                            'Orcasitas': 85,
                            'Orcasur': 86,
                            'Pacífico': 87,
                            'Palacio': 88,
                            'Palomas': 89,
                            'Palomeras bajas': 90,
                            'Palomeras sureste': 91,
                            'Palos de Moguer': 92,
                            'Pau de Carabanchel': 93,
                            'Peñagrande': 94,
                            'Pilar': 95,
                            'Pinar del Rey': 96,
                            'Piovera - Conde Orgaz': 97,
                            'Portazgo': 98,
                            'Pradolongo': 99,
                            'Prosperidad': 100,
                            'Pueblo Nuevo': 101,
                            'Puerta bonita': 102,
                            'Puerta del Ángel': 103,
                            'Quintana': 104,
                            'Recoletos': 105,
                            'Rejas': 106,
                            'Rosas - Musas': 107,
                            'Salvador': 108,
                            'San Andrés': 109,
                            'San Cristóbal': 110,
                            'San Diego': 111,
                            'San Fermín': 112,
                            'San Isidro': 113,
                            'San Juan Bautista': 114,
                            'San Pascual': 115,
                            'Sanchinarro': 116,
                            'Santa Eugenia': 117,
                            'Simancas': 118,
                            'Sol': 119,
                            'Tetuán': 120,
                            'Timón': 121,
                            'Trafalgar': 122,
                            'Tres Olivos - Valverde': 123,
                            'Universidad - Malasaña': 124,
                            'Valdeacederas': 125,
                            'Valdebebas - Valdefuentes': 126,
                            'Valdebernardo - Valderribas': 127,
                            'Valdemarín': 128,
                            'Valdezarza': 129,
                            'Vallehermoso': 130,
                            'Ventas': 131,
                            'Vicálvaro': 132,
                            'Vinateros': 133,
                            'Virgen del Cortijo - Manoteras': 134,
                            'Vista Alegre': 135,
                            'Zofio': 136,
                            'Águilas': 137}
}

encoded_to_label = {'Tipo': {0: 'Apartamento', 1: 'Dúplex', 2: 'Piso', 3: 'Ático'},
                            
                            'Distrito': {0: 'Arganzuela',
                            1: 'Barajas',
                            2: 'Carabanchel',
                            3: 'Centro',
                            4: 'Chamartín',
                            5: 'Chamberí',
                            6: 'Ciudad Lineal',
                            7: 'Fuencarral',
                            8: 'Hortaleza',
                            9: 'Latina',
                            10: 'Moncloa',
                            11: 'Moratalaz',
                            12: 'Puente de Vallecas',
                            13: 'Retiro',
                            14: 'Salamanca',
                            15: 'San Blas',
                            16: 'Tetuán',
                            17: 'Usera',
                            18: 'Vicálvaro',
                            19: 'Villa de Vallecas',
                            20: 'Villaverde'},
                            
                            'Barrio': {0: 'Abrantes',
                            1: 'Acacias',
                            2: 'Adelfas',
                            3: 'Alameda de Osuna',
                            4: 'Almagro',
                            5: 'Almenara',
                            6: 'Almendrales',
                            7: 'Aluche',
                            8: 'Ambroz',
                            9: 'Amposta',
                            10: 'Apóstol Santiago',
                            11: 'Arapiles',
                            12: 'Aravaca',
                            13: 'Arcos',
                            14: 'Argüelles',
                            15: 'Atalaya',
                            16: 'Atocha',
                            17: 'Bellas Vistas',
                            18: 'Bernabéu - Hispanoamérica',
                            19: 'Berruguete',
                            20: 'Buenavista',
                            21: 'Butarque',
                            22: 'Campamento',
                            23: 'Canillas',
                            24: 'Canillejas',
                            25: 'Casa de Campo',
                            26: 'Casco Histórico de Barajas',
                            27: 'Casco Histórico de Vallecas',
                            28: 'Casco histórico de Vicálvaro',
                            29: 'Castellana',
                            30: 'Castilla',
                            31: 'Castillejos',
                            32: 'Centro',
                            33: 'Chamartín',
                            34: 'Chamberí',
                            35: 'Chopera',
                            36: 'Ciudad Jardín',
                            37: 'Ciudad Universitaria',
                            38: 'Colina',
                            39: 'Comillas',
                            40: 'Concepción',
                            41: 'Corralejos - Campo de las Naciones',
                            42: 'Cortes - Huertas',
                            43: 'Costillares',
                            44: 'Cuatro Caminos',
                            45: 'Cuatro vientos',
                            46: 'Delicias',
                            47: 'El Cañaveral - Los Berrocales',
                            48: 'El Pardo',
                            49: 'El Viso',
                            50: 'Embajadores - Lavapiés',
                            51: 'Ensanche de Vallecas - Valdecarros',
                            52: 'Entrevías',
                            53: 'Estrella',
                            54: 'Fontarrón',
                            55: 'Fuente del Berro',
                            56: 'Fuentelarreina',
                            57: 'Gaztambide',
                            58: 'Goya',
                            59: 'Guindalera',
                            60: 'Hellín',
                            61: 'Horcajo',
                            62: 'Ibiza',
                            63: 'Imperial',
                            64: 'Jerónimos',
                            65: 'Justicia - Chueca',
                            66: 'La Florida - El Plantío',
                            67: 'La Paz',
                            68: 'Las Tablas',
                            69: 'Legazpi',
                            70: 'Lista',
                            71: 'Los Cármenes',
                            72: 'Los Rosales',
                            73: 'Los Ángeles',
                            74: 'Lucero',
                            75: 'Marroquina',
                            76: 'Media Legua',
                            77: 'Mirasierra',
                            78: 'Montecarmelo',
                            79: 'Moscardó',
                            80: 'Niño Jesús',
                            81: 'Nueva España',
                            82: 'Nuevos Ministerios - Ríos Rosas',
                            83: 'Numancia',
                            84: 'Opañel',
                            85: 'Orcasitas',
                            86: 'Orcasur',
                            87: 'Pacífico',
                            88: 'Palacio',
                            89: 'Palomas',
                            90: 'Palomeras bajas',
                            91: 'Palomeras sureste',
                            92: 'Palos de Moguer',
                            93: 'Pau de Carabanchel',
                            94: 'Peñagrande',
                            95: 'Pilar',
                            96: 'Pinar del Rey',
                            97: 'Piovera - Conde Orgaz',
                            98: 'Portazgo',
                            99: 'Pradolongo',
                            100: 'Prosperidad',
                            101: 'Pueblo Nuevo',
                            102: 'Puerta bonita',
                            103: 'Puerta del Ángel',
                            104: 'Quintana',
                            105: 'Recoletos',
                            106: 'Rejas',
                            107: 'Rosas - Musas',
                            108: 'Salvador',
                            109: 'San Andrés',
                            110: 'San Cristóbal',
                            111: 'San Diego',
                            112: 'San Fermín',
                            113: 'San Isidro',
                            114: 'San Juan Bautista',
                            115: 'San Pascual',
                            116: 'Sanchinarro',
                            117: 'Santa Eugenia',
                            118: 'Simancas',
                            119: 'Sol',
                            120: 'Tetuán',
                            121: 'Timón',
                            122: 'Trafalgar',
                            123: 'Tres Olivos - Valverde',
                            124: 'Universidad - Malasaña',
                            125: 'Valdeacederas',
                            126: 'Valdebebas - Valdefuentes',
                            127: 'Valdebernardo - Valderribas',
                            128: 'Valdemarín',
                            129: 'Valdezarza',
                            130: 'Vallehermoso',
                            131: 'Ventas',
                            132: 'Vicálvaro',
                            133: 'Vinateros',
                            134: 'Virgen del Cortijo - Manoteras',
                            135: 'Vista Alegre',
                            136: 'Zofio',
                            137: 'Águilas'}
}

# Barrios y Distritos de Madrid, España
Distritos_Barrios_MAD = {'Chamartín': (['Bernabéu - Hispanoamérica', 'Prosperidad', 'Castilla', 'El Viso',
        'Nueva España', 'Ciudad Jardín']),
 'Latina': (['Los Cármenes', 'Puerta del Ángel', 'Lucero', 'Aluche', 'Campamento',
        'Águilas', 'Cuatro vientos']),
 'Arganzuela': (['Legazpi', 'Palos de Moguer', 'Chopera', 'Acacias', 'Delicias',
        'Imperial', 'Atocha']),
 'Centro': (['Sol', 'Embajadores - Lavapiés', 'Justicia - Chueca', 'Universidad - Malasaña', 'Palacio', 'Cortes - Huertas']),
 'Salamanca': (['Recoletos', 'Goya', 'Castellana', 'Lista', 'Fuente del Berro',
        'Guindalera']),
 'Fuencarral': (['Tres Olivos - Valverde', 'La Paz', 'Mirasierra', 'Peñagrande', 'Pilar',
        'El Pardo', 'Fuentelarreina' , 'Las Tablas', 'Montecarmelo']),
 'Ciudad Lineal': (['Pueblo Nuevo', 'Costillares', 'Concepción', 'Ventas',
        'San Juan Bautista', 'Quintana', 'San Pascual', 'Colina', 'Atalaya']),
 'Moncloa': (['Argüelles', 'Ciudad Universitaria', 'Valdezarza', 'Casa de Campo',
        'Aravaca', 'Valdemarín', 'La Florida - El Plantío']),
 'Chamberí': (['Almagro', 'Nuevos Ministerios - Ríos Rosas', 'Trafalgar', 'Arapiles', 'Gaztambide',
        'Vallehermoso']),
 'San Blas': (['Arcos', 'Simancas', 'Salvador', 'Rejas', 'Rosas - Musas', 'Canillejas',
        'Hellín', 'Amposta']),
 'Retiro': (['Pacífico', 'Ibiza', 'Jerónimos', 'Niño Jesús', 'Adelfas',
        'Estrella']),
 'Villaverde': (['Los Ángeles', 'San Andrés', 'Los Rosales', 'Butarque',
        'San Cristóbal']),
 'Barajas': (['Timón', 'Casco Histórico de Barajas', 'Alameda de Osuna',
        'Corralejos - Campo de las Naciones']),
 'Hortaleza': (['Canillas', 'Piovera - Conde Orgaz', 'Valdebebas - Valdefuentes', 'Pinar del Rey',
        'Apóstol Santiago', 'Palomas', 'Sanchinarro', 'Virgen del Cortijo - Manoteras']),
 'Puente de Vallecas': (['Numancia', 'San Diego', 'Palomeras sureste', 'Palomeras bajas',
        'Portazgo', 'Entrevías']),
 'Usera': (['San Fermín', 'Moscardó', 'Zofio', 'Almendrales', 'Orcasur',
        'Orcasitas', 'Pradolongo']),
 'Carabanchel': (['Comillas', 'Opañel', 'Puerta bonita', 'San Isidro',
        'Vista Alegre', 'Abrantes', 'Buenavista', 'Pau de Carabanchel']),
 'Moratalaz': (['Marroquina', 'Fontarrón', 'Vinateros', 'Media Legua',
        'Horcajo']),
 'Tetuán': (['Berruguete', 'Almenara', 'Castillejos', 'Cuatro Caminos',
        'Bellas Vistas', 'Valdeacederas']),
 'Villa de Vallecas': (['Casco Histórico de Vallecas', 'Santa Eugenia', 'Ensanche de Vallecas - Valdecarros']),
 'Vicálvaro': (['Casco histórico de Vicálvaro', 'Ambroz' , 'El Cañaveral - Los Berrocales', 'Valdebernardo - Valderribas'])}

# Número de registros por distrito, para impplementar función de fiabilidad
Registros_por_Distrito = {
    'Arganzuela' : 1026,
    'Barajas' : 22,
    'Carabanchel' : 1187,
    'Centro' : 1050,
    'Chamartín' : 479,
    'Chamberí' : 632,
    'Ciudad Lineal' : 137,
    'Fuencarral' : 127,
    'Hortaleza' : 220,
    'Latina' : 62,
    'Moncloa' : 212,
    'Moratalaz' : 16,
    'Puente de Vallecas' : 63,
    'Retiro' : 315,
    'Salamanca' : 1185,
    'San Blas' : 76,
    'Tetuán' : 493,
    'Usera' : 57,
    'Vicálvaro' : 38,
    'Villa de Vallecas' : 40,
    'Villaverde' : 87,
}

# División de distritos en grupos de precio para poder suavizar outliers dentro de cada grupo

Distritos1 = ['Barajas', 'Carabanchel', 'Fuencarral' , 'Hortaleza', 'Latina', 'Moratalaz', 'Puente de Vallecas' , 'San Blas' , 'Usera' , 'Vicálvaro', 'Villa de Vallecas', 'Villaverde' ]
Distritos2 = ['Arganzuela' , 'Chamartín' , 'Ciudad Lineal' , 'Moncloa' , 'Retiro' , 'Tetuán' ]
Distritos3 = ['Centro' , 'Chamberí', 'Salamanca' ]

# Estimación de precio/m2 y barrio de idealista, para ponderar contra prediccion del modelo
diccionario_idealista_m2 = {
    'Arganzuela': 17.2,
    'Barajas': 13.6,
    'Carabanchel': 13.7,
    'Centro': 20.6,
    'Chamartín': 18.1,
    'Chamberí': 20.6,
    'Ciudad Lineal': 15.4,
    'Fuencarral': 14.1,
    'Hortaleza': 14.5,
    'Latina': 13.8,
    'Moncloa': 17.1,
    'Moratalaz': 12.7,
    'Puente de Vallecas': 13.9,
    'Retiro': 18.0,
    'Salamanca': 21.8,
    'San Blas': 13.3,
    'Tetuán': 17.5,
    'Usera': 13.8,
    'Vicálvaro': 12.3,
    'Villa de Vallecas': 12.7,
    'Villaverde': 12.7
}

# Vector de precisiones por clases segñun cantidad de registros, para usar en ajuste ponderado
precision_diana = (.84,.76,.74)


