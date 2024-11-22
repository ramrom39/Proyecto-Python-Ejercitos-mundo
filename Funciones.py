from typing import List, Dict

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


