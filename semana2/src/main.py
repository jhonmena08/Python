import pandas as pd

def main():
    df = pd.read_csv('C:\\Users\\Jhonm\\repos\\curso_python\\semana2\\cars2_raw.csv')

    # convertir a int a float
    df['price'] = df['price'].astype(float)

    # Establecer el formato de visualización floats
    pd.options.display.float_format = '${:,.0f}'.format

    # filtrar
    # df2 = df[df['price'] == df['price'].max()]

    print()
    print(df[df['price'] == df['price'].min()][['product', 'price', 'kilometraje']])
    print()


if __name__ == "__main__":
    main()
