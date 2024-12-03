from typing import List, Dict

from App import ejercitos


def buscar_por_nombre(ejercitos:List[Dict[str, str|int|float|bool]],nombre:str)->None:
    for ejercito in ejercitos:
        if ejercito["Pais"].lower()==nombre.lower():
            print(formatear_ejercito(ejercito))
            return
    print("Ejército no encontrado")

def añadir_ejercito(ejercitos:List[Dict[str, str|int|float|bool]])->None:
    nombre=input("Introduce el nombre del país: ")
    for ejercito in ejercitos:
        if ejercito["Pais"].lower()==nombre.lower():
            print("El ejercito ya está registrado")
            return

    continente=input("Introduce el continente el país: ")
    poblacion=int(input("Introduce la población del país: "))
    gasto_militar=float(input("Introduce el gasto militar anual: "))
    conflicto=input("¿Está en conflicto bélico? (S/N): ")

    if conflicto=="S":
        en_conflicto=True
    else:
        en_conflicto=False

    ejercito={
        "Pais":nombre,
        "Continente":continente,
        "Poblacion":poblacion,
        "Gasto militar":gasto_militar,
        "En conflicto":en_conflicto
    }
    ejercitos.append(ejercito)
    print("Ejercito añadido correctamente")


def editar_ejercito(ejercitos: List[Dict[str, str | int | float | bool]]) -> None:
    nombre = input("Introduce el nombre del país que deseas editar: ")
    for ejercito in ejercitos:
        if ejercito["Pais"].lower() == nombre.lower():
            continente = input("Introduce el nuevo continente del país: ")
            poblacion = int(input("Introduce la nueva población del país: "))
            gasto_militar = float(input("Introduce el nuevo gasto militar anual: "))
            conflicto = input("¿Está en conflicto bélico? (S/N): ").strip().upper()

            en_conflicto = conflicto == "S"

            ejercito["Continente"] = continente
            ejercito["Poblacion"] = poblacion
            ejercito["Gasto militar"] = gasto_militar
            ejercito["En conflicto"] = en_conflicto

            print("Ejército actualizado correctamente")
            return
    print("Ejército no encontrado")

def formatear_ejercito(ejercito: Dict[str, str | int | float | bool]) -> str:
    return (f"Pais: {ejercito["Pais"]}\n"
            f"Continente: {ejercito["Continente"]}\n"
            f"Poblacion: {ejercito["Poblacion"]}\n"
            f"Gasto Militar: {ejercito["Gasto militar"]}\n"
            f"En conflicto: {ejercito["En conflicto"]}\n")


def borrar_ejercito(ejercitos: List[Dict[str, str | int | float | bool]],nombre:str)->None:
    for ejercito in ejercitos:
        if ejercito["Pais"].lower()==nombre.lower():
            ejercitos.remove(ejercito)
            print(f"Ejercito de {nombre} eliminado")
            return
    print("Ejercito no encontrado")

def volcar_datos(ejercitos: List[Dict[str, str | int | float | bool]])->str:
    datos=""
    for ejercito in ejercitos:
        datos+=(f"{ejercito["Pais"]},"
                f"{ejercito["Continente"]},"
                f"{ejercito["Poblacion"]},"
                f"{ejercito["Gasto militar"]},"
                f"{ejercito["En conflicto"]}\n")

    return datos


def recuperar_datos(datos: str) -> List[Dict[str, str | int | float | bool]]:
    ejercitos = []
    lineas = datos.strip().split("\n")
    for linea in lineas:
        datosF = linea.split(",")
        ejercito = {
            "Pais": datosF[0],
            "Continente": datosF[1],
            "Poblacion": int(datosF[2]),
            "Gasto militar": float(datosF[3]),
            "En conflicto": datosF[4].strip().lower() == "true"
        }
        ejercitos.append(ejercito)
    return ejercitos


def ordenar_por_gasto(ejercitos: List[Dict[str, str | int | float | bool]])->None:
    ejercitos_orden=sorted(ejercitos, key=lambda x:x["Gasto militar"],reverse=True)
    for ejercito in ejercitos_orden:
        print(formatear_ejercito(ejercito))

def mostrar_mayor_gasto_militar(ejercitos: List[Dict[str, str | int | float | bool]]) -> None:
    if not ejercitos:
        print("No hay ejércitos registrados.")
        return

    max_gasto_ejercito = max(ejercitos, key=lambda x: x["Gasto militar"])
    print("\n--- Ejército con mayor gasto militar ---")
    print(formatear_ejercito(max_gasto_ejercito))

def listar_ejercitos(ejercitos: List[Dict[str, str | int | float | bool]]) -> None:

    if not ejercitos:
        print("No hay ejércitos registrados.")
        return

    print("\n----- Listado de Ejércitos -----")
    for ejercito in ejercitos:
        print(formatear_ejercito(ejercito))
        print("-" * 30)