import pandas as pd


def get_bronzen_data() -> pd.DataFrame:
    return pd.read_csv('C:\\Users\\Jhonm\\repos\\curso_python\\semana2\\cars2_raw.csv')


def write_gold_data(data: pd.DataFrame) -> None:
    data.to_excel('C:\\Users\\Jhonm\\repos\\curso_python\\semana2\\cars2_gold.xlsx')


def convert_column_to_date(data: pd.DataFrame) -> pd.DataFrame:
    # convertir a datetime
    data['created'] = pd.to_datetime(data['created'].map(lambda x: x[:10]))
    return data


def add_columns_marca_linea(data: pd.DataFrame) -> pd.DataFrame:
    # agregar dos columnas para marca y linea del vehiculo
    data['marca'] = data['product'].str.split(' ').str[0]
    data['linea'] = data['product'].str.split(' ').str[1]
    return data


def reemplazar_espacios_col_state(data: pd.DataFrame) -> pd.DataFrame:
    data['state'] = data['state'].str.replace(' ', '_')
    return data


def antiguedad(data: pd.DataFrame) -> pd.DataFrame:
    data['antiguedad'] = data['created'].dt.year - data['years']
    return data

