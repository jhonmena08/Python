import numpy as np

def main() -> int:
    edades = {'Wilmar':30, 'Jenny':28, 'Herney':35}

    # promedio de manera manual
    count: int = len(edades)
    suma: int = 0
    for k, v in edades.items():
        suma += v

    print(f'promedio: {suma/count}')

    # promedio con la funcion mean del paquete numpy
    print(f'promedio {np.mean(list(edades.values()))}')
    
    return 0


if __name__ == "__main__":
    main()
