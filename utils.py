
"""
utils.py
Funciones para calcular distancias y tiempos de viaje.
"""

from geopy.distance import geodesic


def calcular_distancia(lat1, lon1, lat2, lon2):
    """Calcula la distancia entre dos ciudades en kilómetros."""
    origen_coordenadas = (lat1, lon1)
    destino_coordenadas = (lat2, lon2)

    distancia = geodesic(
        origen_coordenadas,
        destino_coordenadas
    )

    return distancia.kilometers


def convertir_a_millas(distancia_km):
    """Convierte una distancia de kilómetros a millas."""
    return distancia_km / 1.609344


def calcular_tiempo_vuelo(distancia_km):
    """Estima el vuelo a una velocidad de 850 km/h."""
    tiempo_vuelo = distancia_km / 850

    minutos_totales = round(tiempo_vuelo * 60)
    horas = minutos_totales // 60
    minutos = minutos_totales % 60

    return horas, minutos

from geopy.distance import geodesic


def calcular_distancia(origem_cordenadas, destino_cordenadas):
    """
    Calcula la distancia entre dos ciudades en kilómetros y millas,
    además del tiempo estimado de vuelo a 850 km/h.
    """

    # Calcular distancia geográfica
    distancia = geodesic(origem_cordenadas, destino_cordenadas)

    distancia_km = distancia.kilometers
    distancia_mlh = distancia.miles

    # Calcular tiempo estimado de vuelo
    tempo_voo = distancia_km / 850

    horas_de_voo = int(tempo_voo)
    minutos_de_voo = round((tempo_voo - horas_de_voo) * 60)

    if minutos_de_voo == 60:
        horas_de_voo += 1
        minutos_de_voo = 0

    # Mostrar resultados
    print(f"Distancia da viagem: {distancia_km:.2f} km")
    print(f"Distancia da viagem: {distancia_mlh:.2f} milhas")
    print(
        f"Tempo estimado de voo: "
        f"{horas_de_voo} horas e {minutos_de_voo} minutos"
    )

    # Devolver resultados para utilizarlos en otras funciones
    return distancia_km, distancia_mlh, horas_de_voo, minutos_de_voo
