import json
import os
from Municipio import Municipio
from Localidad import Localidad

class GestorArchivos:
    """
    Componente responsable de tomar el archivo zonas_caracas.json y convertir su
    contenido en una estructura de objetos: una lista de municipios, cada uno con
    sus respectivas localidades.

    Atributos:
        rutaZonas (str): Ubicacion del archivo de zonas de Caracas.
    """

    def __init__(self):
        """
        Prepara el gestor fijando la ruta por defecto del archivo de zonas.
        """
        self.rutaZonas = "zonas_caracas.json"

    def construirMunicipio(self, clave, registros):
        """
        Genera un objeto Municipio ya poblado con sus localidades a partir de la
        clave del archivo y la lista de registros asociada. La clave "El_Hatillo"
        se ajusta a "El Hatillo" reemplazando el guion bajo por un espacio.

        Args:
            clave (str): Nombre del municipio tal como aparece en el archivo.
            registros (list): Lista de diccionarios con los datos de cada localidad.

        Returns:
            Municipio: Municipio con todas sus localidades agregadas.
        """
        municipio = Municipio(clave.replace("_", " "))
        for registro in registros:
            localidad = Localidad(registro["localidad"], registro["latitud"], registro["longitud"])
            municipio.agregarLocalidad(localidad)
        return municipio

    def leerZonas(self):
        """
        Abre y decodifica el archivo de zonas, y devuelve la lista de municipios
        construida a partir de el. Si el archivo no se encuentra en disco, retorna
        una lista vacia en lugar de fallar.

        Returns:
            list: Objetos Municipio cargados desde el archivo (vacia si no existe).
        """
        if not os.path.exists(self.rutaZonas):
            return []

        with open(self.rutaZonas, "r", encoding="utf-8") as archivo:
            contenido = json.load(archivo)

        municipios = []
        for clave in contenido:
            municipios.append(self.construirMunicipio(clave, contenido[clave]))
        return municipios