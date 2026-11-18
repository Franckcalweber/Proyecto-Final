"""
"""
 
"""Consultas a APIs públicas para Información del Viajero."""

import requests

GEOCODING = "https://geocoding-api.open-meteo.com/v1/search"
CLIMA = "https://api.open-meteo.com/v1/forecast"
PAISES = "https://restcountries.com/v3.1/alpha/"
HORA = "https://timeapi.io/api/v1/time/current/zone"

def obtener_coordenadas(ciudad, idioma="es"):
    """Obtiene nombre, país, coordenadas y zona horaria."""
    parametros = {
        "name": ciudad.strip(),
        "count": 1,
        "language": idioma,
        "format": "json"
    }

    try:
        respuesta = requests.get(
            GEOCODING, params=parametros, timeout=10
        )
        respuesta.raise_for_status()
        datos = respuesta.json()

        resultados = datos.get("results", [])

        if not resultados:
            return None

        lugar = resultados[0]

        return {
            "nombre": lugar.get("name", ciudad),
            "pais": lugar.get("country", ""),
            "codigo_pais": lugar.get("country_code", ""),
            "lat": lugar["latitude"],
            "lon": lugar["longitude"],
            "zona_horaria": lugar.get("timezone", "")  
        }

    except requests.exceptions.Timeout:
        print("Tiempo agotado / Tempo esgotado.")
        return None

    except requests.exceptions.RequestException:
        print("Error de conexión / Erro de conexão.")
        return None

    except (ValueError, KeyError, TypeError):
        print("Respuesta inválida / Resposta inválida.")
        return None


def obtener_clima(lat, lon, zona_horaria="auto"):
    """Consulta la temperatura actual en grados Celsius."""
    parametros = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m",
        "timezone": zona_horaria or "auto"
    }

    try:
        respuesta = requests.get(
            CLIMA, params=parametros, timeout=10
        )
        respuesta.raise_for_status()

        datos = respuesta.json()
        return datos["current"]["temperature_2m"]

    except (requests.exceptions.RequestException,
            ValueError, KeyError, TypeError):
        return None


def obtener_datos_pais(codigo):
    """Obtiene capital y moneda utilizando REST Countries."""
    if not codigo:
        return None

    try:
        respuesta = requests.get(
            PAISES + codigo,
            params={"fields": "capital,currencies"},
            timeout=10
        )
        respuesta.raise_for_status()

        datos = respuesta.json()

        capitales = datos.get("capital") or []
        monedas = datos.get("currencies") or {}
        moneda = next(iter(monedas.values()), {})

        return {
            "capital": capitales[0] if capitales else None,
            "moneda": moneda.get("name"),
            "simbolo": moneda.get("symbol", "")
        }

    except (requests.exceptions.RequestException,
            ValueError, KeyError, TypeError, AttributeError):
        return None


def obtener_hora(zona_horaria):
    parametros = {"timeZone":zona_horaria}
    try:
         respuesta = requests.get(HORA,params=parametros, timeout=10)
         datos = respuesta.json()
         return datos["time"][:5]
    except requests.exceptions.RequestException as erro:
        print(f"eror al consultar la hora:{erro}")
        return None
#print(obtener_hora("America/Sao_Paulo"))
    

    

