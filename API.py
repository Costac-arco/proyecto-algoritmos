import requests
from Clima import Clima

class API:
    """
    Cliente que se comunica con el servicio Open-Meteo para traer el clima actual
    de una coordenada. Ante cualquier fallo de red no interrumpe el programa: la
    consulta simplemente devuelve None.

    Atributos:
        urlBase (str): Direccion del endpoint de pronostico de Open-Meteo.
        conectado (bool): Resultado de la ultima verificacion de conexion.
    """

    def __init__(self):
        """
        Configura el cliente con la direccion del servicio y marca la conexion
        como aun no verificada.
        """
        self.urlBase = "https://api.open-meteo.com/v1/forecast"
        self.conectado = False

    def conectar(self):
        """
        Comprueba si el servicio Open-Meteo esta accesible. Cualquier respuesta
        del servidor se interpreta como que hay red; un error de conexion deja
        conectado en False.

        Returns:
            bool: True si se pudo contactar el servicio.
        """
        try:
            respuesta = requests.get(self.urlBase, timeout=5)
            self.conectado = respuesta.status_code in (200, 400)
        except:
            self.conectado = False
        return self.conectado

    def hayConexion(self):
        """
        Informa el estado de conexion registrado en la ultima verificacion.

        Returns:
            bool: True si el cliente estaba conectado.
        """
        return self.conectado

    def construirClima(self, actual):
        """
        Toma la seccion "current" devuelta por la API y arma con ella un objeto
        Clima, dejando atras la estructura de diccionario original.

        Args:
            actual (dict): Bloque "current" de la respuesta de Open-Meteo.

        Returns:
            Clima: Objeto con temperatura, humedad, viento y codigo del tiempo.
        """
        temperatura = actual["temperature_2m"]
        humedad = actual["relative_humidity_2m"]
        viento = actual["wind_speed_10m"]
        codigo = actual["weather_code"]
        return Clima(temperatura, humedad, viento, codigo)

    def consultarClimaActual(self, latitud, longitud):
        """
        Consulta el clima actual de una coordenada y lo devuelve como objeto
        Clima. Construye la URL con los parametros de la peticion y transforma la
        respuesta; si algo falla, devuelve None.

        Args:
            latitud (float): Latitud de la localidad.
            longitud (float): Longitud de la localidad.

        Returns:
            Clima: Datos del clima, o None si la consulta no fue exitosa.
        """
        variables = "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code"
        url = self.urlBase + "?latitude=" + str(latitud) + "&longitude=" + str(longitud) + "&current=" + variables
        try:
            respuesta = requests.get(url, timeout=5)
            if respuesta.status_code != 200:
                return None
            datos = respuesta.json()
            return self.construirClima(datos["current"])
        except:
            return None