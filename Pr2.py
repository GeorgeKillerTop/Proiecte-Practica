import random
import time
culori = {
    0: "\033[0m",       # Reset (fără culoare)
    1: "\033[31m",      # Roșu
    2: "\033[33m",      # Galben
    3: "\033[32m",      # Verde
    4: "\033[34m"       # Albastru
}
def print_matrix(matrix):
    for row in matrix:
        for value in row:
            color = culori[value]
            print(f"{color}●", end=" ")
        print()
    print()
def drop_candies(matrix):
    n = len(matrix)
    for j in range(n):
        last_non_zero = n - 1
        for i in range(n - 1, -1, -1):
            if matrix[i][j] != 0:
                matrix[last_non_zero][j] = matrix[i][j]
                if last_non_zero != i:
                    matrix[i][j] = 0
                last_non_zero -= 1
        for i in range(last_non_zero + 1):
            matrix[i][j] = random.randint(1,4)
    return matrix
def orizontal_L_T(matrix,i,j,gasit,puncte):
    n = len(matrix)
    if(i<n-2 and matrix[i][j]==matrix[i+1][j]==matrix[i+2][j]):
        matrix[i][j] = matrix[i+1][j] = matrix[i+2][j] = matrix[i][j+1] = matrix[i][j+2] = 0
        gasit=1
        matrix=drop_candies(matrix)
        puncte+=20
    if(i<n-2 and matrix[i][j]==matrix[i+1][j+2]==matrix[i+2][j+2]):
        matrix[i][j] = matrix[i+1][j+2] = matrix[i+2][j+2] = matrix[i][j+1] = matrix[i][j+2] = 0
        gasit=1
        matrix=drop_candies(matrix)
        puncte+=20
    if(i>2 and matrix[i][j]==matrix[i-1][j]==matrix[i-2][j]):
        matrix[i][j] = matrix[i-1][j] = matrix[i-2][j] = matrix[i][j+1] = matrix[i][j+2] = 0
        gasit=1
        matrix=drop_candies(matrix)
        puncte+=20
    if(i>2 and matrix[i][j]==matrix[i-1][j+2]==matrix[i-2][j+2]):
        matrix[i][j] = matrix[i-1][j+2] = matrix[i-2][j+2] = matrix[i][j+1] = matrix[i][j+2] = 0
        gasit=1
        matrix=drop_candies(matrix)
        puncte+=20
    if(i<n-2 and matrix[i][j]==matrix[i+1][j+1]==matrix[i+2][j+1]):
        matrix[i][j] = matrix[i+1][j+1] = matrix[i+2][j+1] = matrix[i][j+1] = matrix[i][j+2] = 0
        gasit=1
        matrix=drop_candies(matrix)
        puncte+=30
    if(i>2 and matrix[i][j]==matrix[i-1][j+1]==matrix[i-2][j+1]):
        matrix[i][j] = matrix[i-1][j+1] = matrix[i-2][j+1] = matrix[i][j+1] = matrix[i][j+2] = 0
        gasit=1
        matrix=drop_candies(matrix)
        puncte+=30
    return matrix,gasit,puncte
def vertical_L_T(matrix,i,j,gasit,puncte):
    n = len(matrix)
    if(i<n-2 and matrix[j][i]==matrix[j+1][i+1]==matrix[j+1][i+2]):
        matrix[j][i] = matrix[j+1][i+1] = matrix[j+1][i+2] = matrix[j+1][i] = matrix[j+2][i] = 0
        gasit=1
        matrix=drop_candies(matrix)
        puncte+=30
    if(i>2 and matrix[j][i]==matrix[j+1][i-1]==matrix[j+1][i-2]):
        matrix[j][i] = matrix[j+1][i-1] = matrix[j+1][i-2] = matrix[j+1][i] = matrix[j+2][i] = 0
        gasit=1
        matrix=drop_candies(matrix)
        puncte+=30
    return matrix,gasit,puncte
def orizontal(matrix,mutari,puncte):
    n = len(matrix)
    for length in [5, 4, 3]:
        for i in range(n):
            for j in range(n - length + 1):
                if matrix[i][j] != 0 and all(matrix[i][j] == matrix[i][j + k] for k in range(length)):
                    gasit=0
                    if length==3:
                        matrix,gasit,puncte=orizontal_L_T(matrix,i ,j,gasit,puncte)
                        mutari=1
                    if gasit!=1:
                        for k in range(length):
                            matrix[i][j+k] = 0
                        matrix=drop_candies(matrix)
                        if length==3:
                            puncte+=5
                        elif length==4:
                            puncte+=10
                        elif length==5:
                            puncte+=50
                        mutari=1
    if mutari==0:
        for i in range(n-1):
            for j in range(n-2):
                if matrix[i][j]==matrix[i+1][j+1]==matrix[i][j+2]:
                   matrix[i][j],matrix[i+1][j+1]=matrix[j+1][i],matrix[j][i+1]
                   mutari=1
                if matrix[i][j]==matrix[i+1][j-1]==matrix[i][j+2]:
                   matrix[i][j],matrix[i+1][j-1]=matrix[j+1][i],matrix[j][i+1]
                   mutari=1
                if matrix[i+1][j]==matrix[i][j+1]==matrix[i][j+2]:
                   matrix[i+1][j],matrix[i][j+1]=matrix[j+1][i],matrix[j][i+1]
                   mutari=1
                if matrix[i-1][j]==matrix[i][j+1]==matrix[i][j+2]:
                   matrix[i-1][j],matrix[i][j+1]=matrix[j+1][i],matrix[j][i+1]
                   mutari=1
                if matrix[i][j]==matrix[i][j+1]==matrix[i+1][j+2]:
                   matrix[i][j],matrix[i][j+1]=matrix[j+1][i+1],matrix[j][i+1]
                   mutari=1
                if matrix[i][j]==matrix[i][j+1]==matrix[i-1][j+2]:
                   matrix[i][j],matrix[i][j+1]=matrix[j+1][i-1],matrix[j][i+1]
                   mutari=1
    return matrix,mutari,puncte
def vertical(matrix,mutari,puncte):
    n = len(matrix)
    for length in [5, 4, 3]:
        for i in range(n):
            for j in range(n - length + 1):
                if matrix[j][i] != 0 and all(matrix[j][i] == matrix[j+k][i] for k in range(length)):
                    gasit=0
                    if length==3:
                        matrix,gasit,puncte=vertical_L_T(matrix,i ,j,gasit,puncte)
                        mutari=1
                    if gasit!=1:
                        for k in range(length):
                            matrix[j+k][i] = 0
                        matrix=drop_candies(matrix)
                        if length==3:
                            puncte+=5
                        elif length==4:
                            puncte+=10
                        elif length==5:
                            puncte+=50
                        mutari=1
    if mutari==0:
        for i in range(n-1):
            for j in range(n-2):
                if matrix[j][i]==matrix[j+1][i+1]==matrix[j+2][i]:
                   matrix[j][i],matrix[j+1][i+1]=matrix[j+1][i],matrix[j][i+1]
                   mutari=1
                if matrix[j][i]==matrix[j+1][i-1]==matrix[j+2][i]:
                   matrix[j][i],matrix[j+1][i-1]=matrix[j+1][i],matrix[j][i+1]
                   mutari=1
                if matrix[j][i+1]==matrix[j+1][i]==matrix[j+2][i]:
                   matrix[j][i+1],matrix[j+1][i]=matrix[j+1][i],matrix[j][i+1]
                   mutari=1
                if matrix[j][i-1]==matrix[j+1][i]==matrix[j+2][i]:
                   matrix[j][i-1],matrix[j+1][i]=matrix[j+1][i],matrix[j][i+1]
                   mutari=1
                if matrix[j][i]==matrix[j+1][i]==matrix[j+2][i+1]:
                   matrix[j][i],matrix[j+1][i]=matrix[j+1][i+1],matrix[j][i+1]
                   mutari=1
                if matrix[j][i]==matrix[j+1][i]==matrix[j+2][i-1]:
                   matrix[j][i],matrix[j+1][i]=matrix[j+1][i-1],matrix[j][i+1]
                   mutari=1
    return matrix,mutari,puncte
if __name__ == "__main__":
    puncte_toatale=0
    for i in range(100):
        matrix = [[random.randint(1,4) for _ in range(11)] for _ in range(11)] 
        mutari=0
        puncte =0
        while True:
            matrix,mutari,puncte =vertical(matrix,0,puncte)
            matrix,mutari,puncte =orizontal(matrix,0,puncte)
            if mutari==0 or puncte>10000:
                break
        print(puncte_toatale)
        puncte_toatale+=puncte
    print(puncte_toatale/100)
