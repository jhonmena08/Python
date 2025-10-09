import pandas as pd

def main():
    df = pd.read_csv('C:\\Users\\Jhonm\\repos\\curso_python\\semana2\\cars2_raw.csv')
    print(df[['product', 'price']].head(5))


if __name__ == "__main__":
    main()
