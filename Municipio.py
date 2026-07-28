class Municipio:
    """
    Representa a un municipio del Area Metropolitana de Caracas (Chacao, Baruta,
    El Hatillo, Sucre o Libertador) y mantiene el conjunto de localidades que le
    pertenecen.

    Atributos:
        nombre (str): Identificador del municipio.
        localidades (list): Coleccion de objetos Localidad asociados.
    """

    def __init__(self, nombre):
        """
        Construye un municipio que arranca sin ninguna localidad asociada.

        Args:
            nombre (str): Identificador del municipio.
        """
        self.nombre = nombre
        self.localidades = []

    def agregarLocalidad(self, localidad):
        """
        Incorpora una nueva localidad al conjunto del municipio.

        Args:
            localidad (Localidad): Objeto Localidad que se desea sumar.
        """
        self.localidades.append(localidad)

    def contarLocalidades(self):
        """
        Informa el total de localidades asociadas al municipio.

        Returns:
            int: Numero de localidades registradas.
        """
        total = 0
        for localidad in self.localidades:
            total = total + 1
        return total

    def contarConCoordenadas(self):
        """
        Determina cuantas localidades poseen latitud y longitud registradas.

        Returns:
            int: Numero de localidades geolocalizadas.
        """
        conUbicacion = self.localidadesConCoordenadas()
        return len(conUbicacion)

    def contarSinCoordenadas(self):
        """
        Determina cuantas localidades carecen de coordenadas registradas.

        Returns:
            int: Numero de localidades sin geolocalizacion.
        """
        faltantes = 0
        for localidad in self.localidades:
            if not localidad.tieneCoordenadas():
                faltantes = faltantes + 1
        return faltantes

    def porcentajeConCoordenadas(self):
        """
        Expresa, en porcentaje, que proporcion de las localidades del municipio
        cuenta con coordenadas geograficas.

        Returns:
            float: Valor entre 0.0 y 100.0. Es 0.0 cuando no hay localidades.
        """
        cantidad = len(self.localidades)
        if cantidad == 0:
            return 0.0
        proporcion = self.contarConCoordenadas() / cantidad
        return proporcion * 100

    def localidadesConCoordenadas(self):
        """
        Reune las localidades aptas para ser consultadas en la API, es decir,
        aquellas que tienen coordenadas validas.

        Returns:
            list: Objetos Localidad que poseen latitud y longitud.
        """
        return [localidad for localidad in self.localidades if localidad.tieneCoordenadas()]

    def buscarPorNombre(self, texto):
        """
        Filtra las localidades cuyo nombre incluya el texto recibido, ignorando
        la diferencia entre mayusculas y minusculas.

        Args:
            texto (str): Fragmento del nombre que se quiere localizar.

        Returns:
            list: Objetos Localidad cuyo nombre contiene el fragmento buscado.
        """
        patron = texto.lower()
        encontradas = []
        for localidad in self.localidades:
            nombreEnMinuscula = localidad.nombre.lower()
            if patron in nombreEnMinuscula:
                encontradas.append(localidad)
        return encontradas