"""



in this file we change the colours of the numbers to be more user friendly.


"""


def printing(Arr, a, b, c):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if Arr[i][j] == None:
                print(" ", end=" ")
            elif Arr[i][j] == a or Arr[i][j] == b or Arr[i][j] == c:
                print(f"\033[93m{Arr[i][j]}\033[0m", end=" ")
            else:
                print(Arr[i][j], end=" ")
        print()
