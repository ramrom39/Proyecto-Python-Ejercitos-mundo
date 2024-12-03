from Funciones import*
from typing import List, Dict

ejercitos:List[Dict[str, str|int|float|bool]]=[]

datos:str=""

ejercitos= [
    {
        "Pais":"España",
        "Continente": "Europa",
        "Poblacion": 47000000,
        "Gasto militar": 20000.5,
        "En conflicto": False
    },
    {
        "Pais":"Estados Unidos",
        "Continente": "América",
        "Poblacion": 331000000,
        "Gasto militar": 800000.0,
        "En conflicto": False
    },
    {
        "Pais":"China",
        "Continente": "Asia",
        "Poblacion": 1440000000,
        "Gasto militar": 250000.0,
        "En conflicto": False
    },
    {
        "Pais":"Ucrania",
        "Continente": "Europa",
        "Poblacion": 41000000,
        "Gasto militar": 15000.0,
        "En conflicto": True
    }
]

def menu():
    while True:
        print("\n Menu de opciones: ")
        print("1) Buscar ejército por nombre")
        print("2) Añadir ejército")
        print("3) Editar ejército")
        print("4) Borrar ejército")
        print("5) Volcar los datos en un backup")
        print("6) Recuperar los datos")
        print("7) Mostrar el ejército con mayor gasto militar")
        print("8) Mostrar ejercitos ordenados por gasto militar")
        print("9) Mostrar todos los ejercitos")
        print("0) Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Introduce el nombre del país: ").strip()
            buscar_por_nombre(ejercitos, nombre)
        elif opcion == '2':
            añadir_ejercito(ejercitos)
        elif opcion == '3':
            editar_ejercito(ejercitos)
        elif opcion == '4':
            nombre = input("Introduce el nombre del país a borrar: ").strip()
            borrar_ejercito(ejercitos, nombre)
        elif opcion == '5':
            datos=volcar_datos(ejercitos).strip()
            print("Datos volcados:")
        elif opcion == '6':
            ejercitos.extend(recuperar_datos(datos))
            print("Backup recuperada")
        elif opcion=='7':
            mostrar_mayor_gasto_militar(ejercitos)
        elif opcion == '8':
            ordenar_por_gasto(ejercitos)
        elif opcion=='9':
            listar_ejercitos(ejercitos)
        elif opcion == '0':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")
if __name__ == "__main__":
    menu()
