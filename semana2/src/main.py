import pandas as pd
from preprocessing import *
import os


# configuraciones
pd.set_option('display.max_colwidth', 20)


def main() -> int:
    os.system('cls')

    print('Iniciando procesamiento ..')
    df: pd.DataFrame = get_bronzen_data()

    convert_column_to_date(df)
    add_columns_marca_linea(df)
    reemplazar_espacios_col_state(df)
    antiguedad(df)

    write_gold_data(df)
    print(df)


    return 0


if __name__ == "__main__":
    main()
