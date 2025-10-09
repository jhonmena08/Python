import pandas as pd

def main():
    df = pd.read_csv('C:\\Users\\Jhonm\\repos\\curso_python\\semana2\\cars2_raw.csv')

    # convertir a int a float
    df['price'] = df['price'].astype(float)

    # Opción para ajustar al contenido (autoajuste)
    pd.set_option('display.max_colwidth', None)

    # Establecer el formato de visualización floats
    pd.options.display.float_format = '${:,.0f}'.format

    # filtrar
    # df2 = df[df['price'] == df['price'].max()]

    print()
    print(df[['product', 'price', 'kilometraje']])
    print()


if __name__ == "__main__":
    main()
