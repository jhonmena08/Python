import os

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
def listado_nombres() -> list[str]:
    return [p['nombre'] for p in personas]


# Calcular el promedio de edad.
def promedio_edad() -> int:
    promedio: float = sum(p['edad'] for p in personas) / len(personas)
    return promedio


# Crear un set con todas las frutas distintas que consumieron
def set_frutas() -> set[str]:
    frutas_personas = list(p['frutas'] for p in personas)
    frutas = set(fruta for tupla_frutas in frutas_personas for fruta in tupla_frutas)
    return frutas


# Contar cuántas veces se mencionó cada fruta
def contador_frutas() -> dict[str, int]:
    frutas_personas = list(p['frutas'] for p in personas)
    frutas_consumidas = list(fruta for tupla_frutas in frutas_personas for fruta in tupla_frutas)

    todas_frutas = tuple(set_frutas())

    my_dict: dict[str, int] = {}
    for fruta in todas_frutas:
        counter: int = 0
        for consumidas in frutas_consumidas:
            if fruta == consumidas:
                counter =  counter + 1
        
        my_dict[str(fruta)] = counter

    return my_dict


# Definir funcion que devuelva la fruta más popular
def fruta_popular() -> list[str]:
    conteo_frutas: dict[str, int] = contador_frutas()
    maximo: int = max(conteo_frutas.values())
    return [k for k, v in conteo_frutas.items() if v == maximo ]
    
    

def main()-> int:
    os.system('clear')
    
    print('-' * 100)
    print(f'Personas encuestadas: {listado_nombres()}')
    print('-' * 100)

    print(f'Edad promedio: {promedio_edad()} años')
    print('-' * 100)

    print(f'Frutas consumidas: {set_frutas()}')
    print('-' * 100)

    print(f'Conteo de frutas: {contador_frutas()}')
    print('-' * 100)
    
    print(f'Fruta mas popular: {fruta_popular()}')
    print('-' * 100)
    
    return 0


if __name__ == '__main__':
    main()