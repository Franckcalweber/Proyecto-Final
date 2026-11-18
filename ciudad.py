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

def distancia_a(self, otra):
        """Devuelve la distancia en kilómetros hasta otra Ciudad."""
        return calcular_distancia(
            self.latitud, self.longitud, otra.latitud, otra.longitud
        )

def __str__(self):
        """Devuelve una representación legible de la ciudad."""
        return f"{self.nombre}, {self.pais} ({self.latitud:.4f}, {self.longitud:.4f})"


