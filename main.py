from GestorArchivos import GestorArchivos

def main():
    gestor = GestorArchivos()
    municipios = gestor.leerZonas()

    print("Municipios cargados:", len(municipios))
    for municipio in municipios:
        print(municipio.nombre, "-", municipio.contarLocalidades(), "localidades,", municipio.contarConCoordenadas(), "con coordenadas")

main()