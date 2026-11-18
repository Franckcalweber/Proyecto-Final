
"""
Proyecto Final CS1400 - Información del Viajero
Paso 7: Programación Orientada a Objetos (POO)

Idiomas: Español y Portugués
"""

from ciudad import Ciudad
from utils import calcular_distancia
from api import obtener_coordenadas, obtener_clima, obtener_datos_pais
from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


def seleccionar_idioma():
    """Permite elegir el idioma del programa."""
    while True:
        print("\n=== IDIOMA / LÍNGUA ===")
        print("1. Español")
        print("2. Português")

        opcion = input("Seleccione / Escolha: ").strip()

        if opcion == "1":
            return "es"
        elif opcion == "2":
            return "pt"
        else:
            print("Opción inválida / Opção inválida.")


def pedir_texto(mensaje):
    """Valida que el usuario no deje campos vacíos."""
    while True:
        texto = input(mensaje).strip()

        if texto:
            return texto

        print("No puede estar vacío / Não pode ficar vazio.")


def buscar_ciudad(idioma, mensaje):
    """Consulta la API y convierte los datos en un objeto Ciudad."""
    while True:
        nombre = pedir_texto(mensaje)

        datos = obtener_coordenadas(nombre, idioma)

        if datos is None:
            print("Ciudad no encontrada / Cidade não encontrada.")
            continue

        ciudad = Ciudad(
            datos["nombre"],
            datos["pais"],
            datos["lat"],
            datos["lon"]
        )

        print(f"\n{ciudad}")

        confirmar = input(
            "¿Es correcta? / Está correta? (s/n): "
        ).strip().lower()

        if confirmar in ("s", "si", "sí", "sim"):
            return ciudad, datos

        print("Intenta nuevamente / Tente novamente.")


def pedir_unidad(idioma):
    """Permite seleccionar kilómetros o millas."""
    while True:
        if idioma == "es":
            unidad = input(
                "Unidad de distancia (km/millas): "
            ).strip().lower()
        else:
            unidad = input(
                "Unidade de distância (km/milhas): "
            ).strip().lower()

        if unidad == "km":
            return "km"

        if unidad in ("millas", "milhas"):
            return "millas"

        print("Unidad inválida / Unidade inválida.")


def pedir_transporte(idioma):
    """Solicita y valida el medio de transporte."""
    while True:
        if idioma == "es":
            print("\n1. Avión")
            print("2. Carro")
            print("3. A pie")
        else:
            print("\n1. Avião")
            print("2. Carro")
            print("3. A pé")

        opcion = input(
            "Transporte (1/2/3): "
        ).strip()

        if opcion in ("1", "2", "3"):
            return opcion

        print("Opción inválida / Opção inválida.")


def mostrar_informacion(ciudad, datos, idioma):
    """Muestra clima, hora local, capital y moneda."""
    print("\n================================")

    if idioma == "es":
        print("INFORMACIÓN DE LA CIUDAD")
    else:
        print("INFORMAÇÕES DA CIDADE")

    print("================================")
    print(ciudad)

    temperatura = obtener_clima(
        ciudad.latitud,
        ciudad.longitud,
        datos.get("zona_horaria", "auto")
    )

    if temperatura is not None:
        print(f"Temperatura: {temperatura} °C")
    else:
        print("Temperatura: No disponible / Indisponível")

    zona = datos.get("zona_horaria")

    try:
        hora = datetime.now(
            ZoneInfo(zona)
        ).strftime("%H:%M")
        print(f"Hora local: {hora}")
    except (ZoneInfoNotFoundError, ValueError, TypeError):
        print("Hora local: No disponible / Indisponível")

    pais = obtener_datos_pais(datos.get("codigo_pais", ""))

    if pais:
        print(
            f"Capital: {pais.get('capital') or 'No disponible'}"
        )
        print(
            f"Moneda / Moeda: "
            f"{pais.get('moneda') or 'No disponible'} "
            f"{pais.get('simbolo', '')}"
        )
    else:
        print("Datos del país no disponibles.")


def planear_viaje(idioma):
    """Crea objetos Ciudad y calcula distancia y tiempo de viaje."""
    print("\n================================")

    if idioma == "es":
        print("PLANIFICAR VIAJE")
        origen_texto = "Ciudad de origen: "
        destino_texto = "Ciudad de destino: "
    else:
        print("PLANEJAR VIAGEM")
        origen_texto = "Cidade de origem: "
        destino_texto = "Cidade de destino: "

    print("================================")

    nombre_origen = pedir_texto(origen_texto)
    nombre_destino = pedir_texto(destino_texto)

    unidad = pedir_unidad(idioma)
    transporte = pedir_transporte(idioma)

    # Mostrar resumen antes de consultar la API.
    print("\n========== RESUMEN / RESUMO ==========")
    print(f"Origen / Origem: {nombre_origen}")
    print(f"Destino: {nombre_destino}")
    print(f"Unidad / Unidade: {unidad}")
    print(f"Transporte: {transporte}")
    print("======================================")

    # Buscar coordenadas y crear objetos Ciudad.
    datos_origen = obtener_coordenadas(nombre_origen, idioma)
    datos_destino = obtener_coordenadas(nombre_destino, idioma)

    if datos_origen is None:
        print("\nOrigen no encontrado / Origem não encontrada.")
        origen, datos_origen = buscar_ciudad(idioma, origen_texto)
    else:
        origen = Ciudad(
            datos_origen["nombre"],
            datos_origen["pais"],
            datos_origen["lat"],
            datos_origen["lon"]
        )

    if datos_destino is None:
        print("\nDestino no encontrado / Destino não encontrado.")
        destino, datos_destino = buscar_ciudad(idioma, destino_texto)
    else:
        destino = Ciudad(
            datos_destino["nombre"],
            datos_destino["pais"],
            datos_destino["lat"],
            datos_destino["lon"]
        )

    print("\n========== CIUDADES / CIDADES ==========")
    print(f"Origen / Origem: {origen}")
    print(f"Destino: {destino}")

    # Requisito principal del Paso 7:
    # calcular distancia usando un método del objeto.
    distancia_km = origen.distancia_a(destino)

    # El utils.py de tu compañero devuelve cuatro valores.
    # Reutilizamos esa función para obtener millas y tiempo.
    coordenadas_origen = (origen.latitud, origen.longitud)
    coordenadas_destino = (destino.latitud, destino.longitud)

    _, distancia_millas, horas, minutos = calcular_distancia(
        coordenadas_origen,
        coordenadas_destino
    )

    print("\n========== RESULTADOS ==========")

    if unidad == "km":
        print(f"Distancia: {distancia_km:.2f} km")
    else:
        print(f"Distancia: {distancia_millas:.2f} millas")

    if transporte == "1":
        if idioma == "es":
            print(f"Tiempo estimado de vuelo: {horas} h {minutos} min")
        else:
            print(f"Tempo estimado de voo: {horas} h {minutos} min")
    else:
        if idioma == "es":
            print(
                "Tiempo de viaje por carretera o a pie "
                "no disponible en esta versión."
            )
        else:
            print(
                "Tempo de viagem de carro ou a pé "
                "indisponível nesta versão."
            )

    print("================================")


def main():
    """Menú principal del programa."""
    idioma = seleccionar_idioma()

    while True:
        print("\n================================")

        if idioma == "es":
            print("INFORMACIÓN DEL VIAJERO")
            print("1. Planificar viaje")
            print("2. Información de una ciudad")
            print("3. Salir")
        else:
            print("INFORMAÇÕES DO VIAJANTE")
            print("1. Planejar viagem")
            print("2. Informações de uma cidade")
            print("3. Sair")

        print("================================")

        opcion = input("Opción / Opção: ").strip()

        if opcion == "1":
            planear_viaje(idioma)

        elif opcion == "2":
            if idioma == "es":
                mensaje = "Nombre de la ciudad: "
            else:
                mensaje = "Nome da cidade: "

            ciudad, datos = buscar_ciudad(idioma, mensaje)
            mostrar_informacion(ciudad, datos, idioma)

        elif opcion == "3":
            if idioma == "es":
                print("¡Gracias por usar el programa!")
            else:
                print("Obrigado por usar o programa!")
            break

        else:
            print("Opción inválida / Opção inválida.")


if __name__ == "__main__":
    main()

