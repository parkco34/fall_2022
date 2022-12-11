#!/usr/bin/env python
import random

ROWS = 3
COLS = 4

def main():
    values = [[0,0,0,0],
             [0, 0, 0, 0], 
             [0, 0, 0, 0],
             ]

    for row in range(ROWS):
        for col in range(COLS):
            values[row][col] = random.randint(1, 100)

    print(values)

    for row in values:
        for item in row:
            print(item)


if __name__ == "__main__":
    main()

