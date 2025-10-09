import polars as pl
# import pandas as pd

def main():
    # abrir archivo
    df = pl.read_csv('C:/Users/Jhonm/proy/datos.csv')

    df2 = df.filter([
        pl.col('price') < 40_000_000,
        pl.col('kilometraje') < 40_000
    ])

    print(df2)


if __name__ == "__main__":
    main()
