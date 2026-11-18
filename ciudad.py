
from utils import calcular_distancia


class Ciudad:
    """Representa una ciudad con su ubicación geográfica."""

    def __init__(self, nombre, pais, latitud, longitud):
        """Inicializa los atributos de la ciudad."""
        self.nombre = nombre
        self.pais = pais
        self.latitud = float(latitud)
        self.longitud = float(longitud)

    def distancia_a(self, otra):
        """Calcula y devuelve la distancia en kilómetros."""
        origen = (self.latitud, self.longitud)
        destino = (otra.latitud, otra.longitud)

        distancia_km, _, _, _ = calcular_distancia(
            origen, destino
        )

        return distancia_km

    def __str__(self):
        """Devuelve una representación legible de la ciudad."""
        return (
            f"{self.nombre}, {self.pais} "
            f"({self.latitud:.4f}, {self.longitud:.4f})"
        )



