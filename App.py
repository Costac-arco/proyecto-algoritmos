from GestorArchivos import GestorArchivos
from API import API

class App:
    """
    Coordina la aplicacion MeteoCaracas: prepara los datos a partir del archivo
    de zonas, presenta el menu y atiende las consultas de clima en tiempo real,
    ya sea navegando por municipio o buscando la localidad por su nombre.

    Atributos:
        gestorArchivos (GestorArchivos): Encargado de leer el archivo de zonas.
        municipios (list): Municipios cargados en memoria.
        api (API): Cliente para consultar Open-Meteo.
    """

    def __init__(self):
        """
        Deja la aplicacion lista para iniciar, con sus colaboradores creados y la
        lista de municipios todavia vacia.
        """
        self.gestorArchivos = GestorArchivos()
        self.municipios = []
    
    def iniciar(self):
        """
        Pone en marcha la aplicacion: carga los datos, muestra el reporte de
        carga y repite el menu leyendo la opcion del usuario hasta que se decide
        salir. Si la carga falla, termina sin abrir el menu.
        """
        self.cargarDatos()
        if len(self.municipios) == 0:
            return
        self.mostrarReporteCarga()
        self.menu()


    def cargarDatos(self):
        """
        Solicita al gestor la lista de municipios y avisa si el archivo no pudo
        leerse. Ademas prueba la conexion con Open-Meteo para informar si se
        podran hacer consultas.
        """
        print("Cargando zonas de Caracas...")
        self.municipios = self.gestorArchivos.leerZonas()
        if len(self.municipios) == 0:
            print("No se pudo cargar el archivo zonas_caracas.json.")
            return
        print("Se cargaron", len(self.municipios), "municipios.")
        if self.api.conectar():
            print("Open-Meteo disponible.")
        else:
            print("Sin conexion con Open-Meteo; podra ver los datos pero no consultar el clima.")

    def mostrarReporteCarga(self):
        """
        Recorre los municipios y muestra, para cada uno, cuantas localidades se
        cargaron, cuantas tienen coordenadas, cuantas no, y el porcentaje que si
        las tiene.
        """
        print("\n===== REPORTE DE CARGA =====")
        for municipio in self.municipios:
            cargadas = municipio.contarLocalidades()
            conCoord = municipio.contarConCoordenadas()
            sinCoord = municipio.contarSinCoordenadas()
            porcentaje = round(municipio.porcentajeConCoordenadas(), 2)
            print(municipio.nombre + ":")
            print("   cargadas =", cargadas, "| con coord =", conCoord, "| sin coord =", sinCoord, "| % con coord =", porcentaje)

    def menu(self):
        """
        Imprime las opciones disponibles del menu principal.
        """
        while True:
            print("\n===== METEOCARACAS =====")
            print("1) Clima por municipio y localidad")
            print("2) Buscar localidad por nombre")
            print("3) Ver reporte de carga")
            print("4) Salir")

            opcion = input("Ingrese la opcion que desea ejecutar: ")
            while not opcion.isdigit() or not int(opcion) in range(1,5):
                print("Opción inválida. Intente nuevamente.")
                opcion = input("Ingrese la opcion que desea ejecutar: ")
            
            if opcion == "1":
                self.consultarPorMunicipio()
            elif opcion == "2":
                self.buscarPorNombre()
            elif opcion == "3":
                self.mostrarReporteCarga()
            else:
                print("Hasta pronto")
                break

    def consultarPorMunicipio(self):
        pass

    def buscarPorNombre(self):
        pass

    def mostrarReporteCarga(self):
        pass

    