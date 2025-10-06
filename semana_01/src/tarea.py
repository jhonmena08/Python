
personas: list[dict] = [
    {"nombre": "Ana", "edad": 23, "frutas": ("manzana", "pera", "uva")},
    {"nombre": "Luis", "edad": 30, "frutas": ("pera", "sandía")},
    {"nombre": "María", "edad": 20, "frutas": ("uva", "manzana", "kiwi")},
    {"nombre": "Juan", "edad": 25, "frutas": ("naranja", "pera")},
    {"nombre": "Sofía", "edad": 28, "frutas": ("mango", "manzana")},
    {"nombre": "Carlos", "edad": 35, "frutas": ("sandía", "pera", "mango")},
    {"nombre": "Elena", "edad": 22, "frutas": ("kiwi", "manzana", "uva")},
    {"nombre": "Pedro", "edad": 27, "frutas": ("naranja", "sandía")}
]

# Mostrar los nombres de todas las personas encuestadas
def mostrar_nombres() -> None:
    for p in personas:
        print(p['nombre'])


# Calcular el promedio de edad.
def promedio_edad() -> int:
    for p in personas:
        print(p['edad'])


# Crear un set con todas las frutas distintas que consumieron
def set_frutas() -> set[str]:
    ...


# Contar cuántas veces se mencionó cada fruta
def cantidad_frutas(patron: str) -> int:
    ...


# Definir una función que reciba la lista de personas y devuelva la fruta más popular
def fruta_popular(frutas: list[str]) -> str:
    ...
    

def main()-> int:
    print()
    
    # mostrar_nombres()
    promedio_edad()

    print()
    return 0


if __name__ == '__main__':
    main()