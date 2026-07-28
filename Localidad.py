class Localidad:
    """
    Modela una localidad perteneciente a un municipio de Caracas, guardando su
    nombre y su posicion geografica. Dado que no toda localidad tiene ubicacion
    documentada, la latitud y la longitud admiten el valor None.

    Atributos:
        nombre (str): Denominacion de la localidad.
        latitud (float): Coordenada de latitud, o None si se desconoce.
        longitud (float): Coordenada de longitud, o None si se desconoce.
    """

    def __init__(self, nombre, latitud, longitud):
        """
        Crea una localidad con su nombre y sus coordenadas. Las coordenadas
        pueden llegar como None cuando la ubicacion no esta registrada.

        Args:
            nombre (str): Denominacion de la localidad.
            latitud (float): Coordenada de latitud (admite None).
            longitud (float): Coordenada de longitud (admite None).
        """
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud

    def tieneCoordenadas(self):
        """
        Verifica si la localidad cuenta con una ubicacion geografica completa,
        es decir, con ambas coordenadas definidas.

        Returns:
            bool: True cuando ni la latitud ni la longitud son None.
        """
        if self.latitud is None:
            return False
        if self.longitud is None:
            return False
        return True

    def mostrar(self):
        """
        Entrega una representacion breve de la localidad para listarla en
        pantalla.

        Returns:
            str: El nombre de la localidad.
        """
        texto = self.nombre
        return texto