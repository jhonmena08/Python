import pandas as pd

def main():
    df = pd.read_csv('C:\\Users\\Jhonm\\repos\\curso_python\\semana2\\cars2_raw.csv')

    # Opción para ajustar ancho columnas (20 caracteres)
    pd.set_option('display.max_colwidth', 20)

    # Establecer el formato de visualización floats
    pd.options.display.float_format = '${:,.0f}'.format

    # convertir a int a float
    df['price'] = df['price'].astype(float)


    # filtrar
    # df2 = df[df['price'] == df['price'].max()]

    print()
    print(df)
    print()


if __name__ == "__main__":
    main()
