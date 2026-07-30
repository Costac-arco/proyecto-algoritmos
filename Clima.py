class Clima:
    """
    Encapsula los valores meteorologicos obtenidos al consultar el clima actual
    de una localidad. La API entrega estos datos dentro de un diccionario y esta
    clase los conserva ya convertidos en un objeto.

    Atributos:
        temperatura (float): Temperatura del aire en grados Celsius.
        humedad (int): Humedad relativa expresada en porcentaje.
        viento (float): Rapidez del viento en km/h.
        codigoTiempo (int): Codigo WMO que identifica el estado del cielo.
        estado (str): Texto descriptivo derivado del codigo WMO.
    """

    def __init__(self, temperatura, humedad, viento, codigoTiempo):
        """
        Arma un objeto Clima a partir de las magnitudes recibidas y calcula de
        inmediato la descripcion textual asociada al codigo del tiempo.

        Args:
            temperatura (float): Temperatura del aire en grados Celsius.
            humedad (int): Humedad relativa en porcentaje.
            viento (float): Rapidez del viento en km/h.
            codigoTiempo (int): Codigo WMO del estado del cielo.
        """
        self.temperatura = temperatura
        self.humedad = humedad
        self.viento = viento
        self.codigoTiempo = codigoTiempo
        self.estado = self.traducirCodigo(codigoTiempo)

    def traducirCodigo(self, codigo):
        """
        Convierte un codigo WMO de Open-Meteo en una frase entendible. Se apoya
        en un diccionario de referencia que es una constante del programa (no
        proviene de la API), y devuelve un valor por defecto si el codigo no esta.

        Args:
            codigo (int): Codigo WMO a interpretar.

        Returns:
            str: Descripcion correspondiente, o "Desconocido" si no figura.
        """
        codigos = {
            0: "Despejado",
            1: "Mayormente despejado",
            2: "Parcialmente nublado",
            3: "Nublado",
            45: "Niebla",
            48: "Niebla con escarcha",
            51: "Llovizna ligera",
            53: "Llovizna moderada",
            55: "Llovizna densa",
            56: "Llovizna helada ligera",
            57: "Llovizna helada densa",
            61: "Lluvia ligera",
            63: "Lluvia moderada",
            65: "Lluvia fuerte",
            66: "Lluvia helada ligera",
            67: "Lluvia helada fuerte",
            71: "Nieve ligera",
            73: "Nieve moderada",
            75: "Nieve fuerte",
            77: "Granos de nieve",
            80: "Chubascos ligeros",
            81: "Chubascos moderados",
            82: "Chubascos violentos",
            85: "Chubascos de nieve ligeros",
            86: "Chubascos de nieve fuertes",
            95: "Tormenta",
            96: "Tormenta con granizo ligero",
            99: "Tormenta con granizo fuerte"
        }
        return codigos.get(codigo, "Desconocido")