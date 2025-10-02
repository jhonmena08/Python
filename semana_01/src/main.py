from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

    def __str__(self) -> str:
        return f'x:{self.x}, y:{self.y}'


def main():
    p1: Point = Point(102, 236)
    print(p1)


if __name__ == "__main__":
    main()
