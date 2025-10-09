
def counter(limit: int) -> None:
    x: int = 0

    while True:
        x += 1
        print(f'{x} ', end='')

        if x >= limit:
            print()
            return


def main() -> None:
    n: int = int(input('contar hasta -> '))
    counter(n)


if __name__ == '__main__':
    main()
