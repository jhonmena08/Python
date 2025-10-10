import pandas as pd
import os

# configuraciones
pd.set_option('display.max_colwidth', 15)


def get_bronzen_data() -> pd.DataFrame:
    return pd.read_csv('C:\\Users\\Jhonm\\repos\\curso_python\\semana2\\cars2_raw.csv')


def write_gold_data(data: pd.DataFrame) -> None:
    data.to_excel('C:\\Users\\Jhonm\\repos\\curso_python\\semana2\\cars2_gold.xlsx')


def convert_date(data: pd.DataFrame) -> pd.DataFrame:
    # corregir las fechas al formato 2025-10-28
    data['created'] = data['created'].map(lambda x: x[:10])
    return data


def add_columns(data: pd.DataFrame) -> pd.DataFrame:
    # agregar dos columnas para marca y linea del vehiculo
    data['marca'] = data['product'].str.split(' ').str[0]
    data['linea'] = data['product'].str.split(' ').str[1]
    return data



def main() -> int:
    os.system('cls')

    print('Iniciando procesamiento ..')
    df = get_bronzen_data()
    convert_date(df)
    add_columns(df)

    write_gold_data(df)
    print(df)


    return 0


if __name__ == "__main__":
    main()
