#  File: MagicSquare.py


import math
import random


def make_square(n):
    square = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        square.append(row)

    row = n-1
    col = (n-1)//2 #indices start at 0
    magic_number = 1
    square[row][col] = magic_number
    while magic_number < (n**2):
        magic_number += 1
        col += 1
        row += 1 #1 cycle
        if row > (n-1):
            row = 0
        if col > (n-1):
            col = 0
        if square[row][col] > 0:
            row -= 1
            col -= 1
            row -= 1
        square[row][col] = magic_number
    return square


def print_square(magic_square):
    n = len(magic_square)
    custom_space = len(str(n**2))
    for row in range(len(magic_square)):
        for col in range(len(magic_square[row])):
            print(format(magic_square[row][col],">"+str(custom_space)+"d"), end=" ")
        print()




def check_square(magic_square):
    n_side = len(magic_square)
    canonical_sum = n_side * ((n_side**2 + 1) / 2)
    l = len(magic_square)


    for i in range(l):
        row_sum = 0
        col_sum = 0

        for j in range(l):
            row_sum += magic_square[i][j]
        if row_sum != canonical_sum:
            return False
        for j in range(l):
            col_sum += magic_square[j][i]
        if col_sum != canonical_sum:
            return False
    sum_diag_1 = int(sum(magic_square[i][i] for i in range(l)))
    if sum_diag_1 != canonical_sum:
        return False
    sum_diag_2 = int(sum(magic_square[l-i-1][i] for i in range(l)))
    if sum_diag_2 != canonical_sum:
        return False
    else:
        return True


def main():
    while True:
        try:
            n = eval(input("Please enter an odd number: "))
            magic_square = make_square(n)
            canonical_sum = n * ((n ** 2 + 1) / 2)
            if n % 2 == 1 and n > 0:
                if check_square(magic_square) == True:
                    print()
                    print("Here is a", len(magic_square), "x", len(magic_square), "magic square:")
                    print()
                    print_square(magic_square)
                    print()
                    print("This is a magic square and the canonical sum is", int(canonical_sum))
                    break
                elif check_square(magic_square) == False:
                    print()
                    print("Here is a", len(magic_square), "x", len(magic_square), " square:")
                    print()
                    print_square(magic_square)
                    print()
                    print("This is not a magic square")
                    break
            elif n % 2 == 0:
                continue
            elif n <= 0:
                continue
            else:
                continue
        except:
            print("Invalid input.") 



if __name__ == "__main__":
    main()