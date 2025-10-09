import pandas as pd
import os

df = pd.read_csv('C:\\Users\\Jhonm\\repos\\curso_python\\semana2\\cars2_raw.csv')
pd.set_option('display.max_colwidth', 15)
# pd.options.display.float_format = '${:,.0f}'.format


def main() -> int:
    os.system('cls')

    # filtrar
    df2 = df[df['price'] == df['price'].max()]
    print(df2)

    print()
    return 0


if __name__ == "__main__":
    main()
