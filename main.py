
"""
Proyecto Final CS1400 - Información del Viajero
Idiomas: Español y Português

Integrantes: Franck Calderon y Marcos Araujo
Fecha: 

Programa para consultar información de ciudades
y planificar viajes usando APIs públicas.
"""

from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from api import (
    obtener_coordenadas,
    obtener_clima,
    obtener_datos_pais
)


# Traducciones de todos los mensajes principales.
MENSAJES = {
    "es": {
        "bienvenida": "¡Bienvenido a Información del Viajero!",
        "menu": (
            "1. Calcular distancia / Planear viaje\n"
            "2. Información de ciudad\n"
            "3. Salir"
        ),
        "opcion": "Elige una opción: ",
        "invalida": "Opción inválida. Intenta otra vez.",
        "vacio": "El campo no puede estar vacío.",
        "origen": "Ciudad de origen: ",
        "destino": "Ciudad de destino: ",
        "ciudad": "Nombre de la ciudad: ",
        "unidad": "Unidad (km/millas): ",
        "unidad_error": "Escribe km o millas.",
        "transporte": "Transporte (avion/carro/pie): ",
        "transporte_error": "Elige avion, carro o pie.",
        "resumen": "--- Resumen ---",
        "consultando": "Consultando datos...",
        "no_encontrada": "Ciudad no encontrada o error de conexión.",
        "confirmar": "¿Es la ciudad correcta? (s/n): ",
        "coordenadas": "--- Coordenadas ---",
        "info": "--- Información de la ciudad ---",
        "temperatura": "Temperatura actual",
        "hora": "Hora local",
        "capital": "Capital",
        "moneda": "Moneda",
        "pais": "País",
        "nota": "La distancia y el tiempo se calcularán después.",
        "despedida": "¡Gracias por usar el programa!",
        "no_disponible": "No disponible",
        "unidad_larga_km": "kilómetros",
        "unidad_larga_millas": "millas",
        "transporte_label": "Transporte",
        "origen_label": "Origen",
        "destino_label": "Destino",
        "unidad_label": "Unidad",
        "reintentar": "Prueba con otra ciudad."
    },

    "pt": {
        "bienvenida": "Bem-vindo ao Informações do Viajante!",
        "menu": (
            "1. Calcular distância / Planejar viagem\n"
            "2. Informações da cidade\n"
            "3. Sair"
        ),
        "opcion": "Escolha uma opção: ",
        "invalida": "Opção inválida. Tente novamente.",
        "vacio": "O campo não pode ficar vazio.",
        "origen": "Cidade de origem: ",
        "destino": "Cidade de destino: ",
        "ciudad": "Nome da cidade: ",
        "unidad": "Unidade (km/milhas): ",
        "unidad_error": "Digite km ou milhas.",
        "transporte": "Transporte (aviao/carro/pe): ",
        "transporte_error": "Escolha aviao, carro ou pe.",
        "resumen": "--- Resumo ---",
        "consultando": "Consultando dados...",
        "no_encontrada": "Cidade não encontrada ou erro de conexão.",
        "confirmar": "Esta é a cidade correta? (s/n): ",
        "coordenadas": "--- Coordenadas ---",
        "info": "--- Informações da cidade ---",
        "temperatura": "Temperatura atual",
        "hora": "Hora local",
        "capital": "Capital",
        "moneda": "Moeda",
        "pais": "País",
        "nota": "A distância e o tempo serão calculados depois.",
        "despedida": "Obrigado por usar o programa!",
        "no_disponible": "Indisponível",
        "unidad_larga_km": "quilômetros",
        "unidad_larga_millas": "milhas",
        "transporte_label": "Transporte",
        "origen_label": "Origem",
        "destino_label": "Destino",
        "unidad_label": "Unidade",
        "reintentar": "Tente outra cidade."
    }
}


def seleccionar_idioma():
    """Permite seleccionar español o portugués."""
    while True:
        print("\n=== Idioma / Língua ===")
        print("1. Español")
        print("2. Português")

        opcion = input("Seleccione / Escolha: ").strip()

        if opcion == "1":
            return "es"
        elif opcion == "2":
            return "pt"
        else:
            print("Opción inválida / Opção inválida.")


def pedir_texto(mensaje, textos):
    """Pide texto y evita entradas vacías."""
    while True:
        valor = input(mensaje).strip()

        if valor:
            return valor

        print(textos["vacio"])


def pedir_unidad(textos):
    """Valida la unidad de distancia."""
    while True:
        unidad = input(textos["unidad"]).strip().lower()

        if unidad == "km":
            return "km"

        elif unidad in ("millas", "milhas"):
            return "millas"

        print(textos["unidad_error"])


def pedir_transporte(textos):
    """Permite elegir un medio de transporte."""
    while True:
        transporte = input(textos["transporte"]).strip().lower()

        if transporte in (
            "avion", "avião", "carro",
            "pie", "pe", "a pe", "a pé"
        ):
            return transporte

        print(textos["transporte_error"])


def buscar_ciudad(textos, idioma, pregunta):
    """Busca una ciudad y permite corregir el nombre."""
    while True:
        nombre = pedir_texto(pregunta, textos)

        lugar = obtener_coordenadas(nombre, idioma)

        if lugar is None:
            print(textos["no_encontrada"])
            continue

        print(f'{lugar["nombre"]}, {lugar["pais"]}')

        while True:
            confirmar = input(textos["confirmar"]).strip().lower()

            if confirmar in ("s", "sim", "si", "sí"):
                return lugar

            elif confirmar in ("n", "nao", "não", "no"):
                print(textos["reintentar"])
                break

            else:
                print(textos["invalida"])


def hora_local(zona):
    """Obtiene la hora local según la zona horaria."""
    try:
        return datetime.now(
            ZoneInfo(zona)
        ).strftime("%H:%M")

    except (ZoneInfoNotFoundError, ValueError,
            TypeError, KeyError):
        return None


def mostrar_coordenadas(lugar):
    """Imprime las coordenadas de una ciudad."""
    print(
        f'{lugar["nombre"]}, {lugar["pais"]} '
        f'-> lat {lugar["lat"]:.4f}, '
        f'lon {lugar["lon"]:.4f}'
    )


def mostrar_informacion(lugar, textos):
    """Muestra clima, hora, capital y moneda."""
    print("\n" + textos["info"])

    mostrar_coordenadas(lugar)

    temperatura = obtener_clima(
        lugar["lat"],
        lugar["lon"],
        lugar["zona_horaria"]
    )

    hora = hora_local(lugar["zona_horaria"])

    pais = obtener_datos_pais(lugar["codigo_pais"])

    sin_datos = textos.get(
        "no_disponible",
        textos.get("no_disponible", "Indisponível")
    )

    if temperatura is not None:
        print(f'{textos["temperatura"]}: {temperatura} °C')
    else:
        print(f'{textos["temperatura"]}: {sin_datos}')

    print(f'{textos["hora"]}: {hora or sin_datos}')

    if pais:
        print(
            f'{textos["capital"]}: '
            f'{pais.get("capital") or sin_datos}'
        )

        if pais.get("moneda"):
            print(
                f'{textos["moneda"]}: '
                f'{pais["moneda"]} '
                f'({pais.get("simbolo", "")})'
            )
        else:
            print(f'{textos["moneda"]}: {sin_datos}')

    else:
        print(f'{textos["capital"]}: {sin_datos}')
        print(f'{textos["moneda"]}: {sin_datos}')


def planear_viaje(textos, idioma):
    """Solicita los datos del viaje y consulta coordenadas."""
    origen = pedir_texto(textos["origen"], textos)
    destino = pedir_texto(textos["destino"], textos)

    unidad = pedir_unidad(textos)
    transporte = pedir_transporte(textos)

    # Resumen antes de consultar las APIs.
    print("\n" + textos["resumen"])
    print(f'{textos["origen_label"]}: {origen}')
    print(f'{textos["destino_label"]}: {destino}')

    if unidad == "km":
        nombre_unidad = textos["unidad_larga_km"]
    else:
        nombre_unidad = textos["unidad_larga_millas"]

    print(f'{textos["unidad_label"]}: {nombre_unidad}')
    print(f'{textos["transporte_label"]}: {transporte}')

    print("\n" + textos["consultando"])

    # Consulta de origen y destino.
    lugar_origen = obtener_coordenadas(origen, idioma)
    lugar_destino = obtener_coordenadas(destino, idioma)

    if lugar_origen is None:
        print(textos["no_encontrada"])
        lugar_origen = buscar_ciudad(
            textos, idioma, textos["origen"]
        )

    if lugar_destino is None:
        print(textos["no_encontrada"])
        lugar_destino = buscar_ciudad(
            textos, idioma, textos["destino"]
        )

    print("\n" + textos["coordenadas"])

    print(textos["origen_label"] + ": ", end="")
    mostrar_coordenadas(lugar_origen)

    print(textos["destino_label"] + ": ", end="")
    mostrar_coordenadas(lugar_destino)

    print(textos["nota"])


def main():
    """Ejecuta el programa hasta que el usuario elija salir."""
    idioma = seleccionar_idioma()
    textos = MENSAJES[idioma]

    print("\n" + textos["bienvenida"])

    while True:
        print("\n" + textos["menu"])

        opcion = input(textos["opcion"]).strip()

        if opcion == "1":
            planear_viaje(textos, idioma)

        elif opcion == "2":
            lugar = buscar_ciudad(
                textos, idioma, textos["ciudad"]
            )
            mostrar_informacion(lugar, textos)

        elif opcion == "3":
            print(textos["despedida"])
            break

        else:
            print(textos["invalida"])


if __name__ == "__main__":
    main()
