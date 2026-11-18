"""Representación orientada a la informacion de una ciudad."""

from utils import calcular_distancia


class Ciudad:
    """Agrupa los datos geográficos de una ciudad y sus operaciones."""

    def __init__(self, nombre, pais, latitud, longitud):
        """Inicializa la ciudad con nombre, país y coordenadas."""
        self.nombre = nombre
        self.pais = pais
        self.latitud = float(latitud)
        self.longitud = float(longitud)


