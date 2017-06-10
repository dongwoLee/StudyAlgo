
def col_reading(list):
    result = ''

    for i in range(0,15):
        for j in range(0,5):
            if(list[j][i]==''):
                continue
            result = str(result) + str(list[j][i])

    print(result)


if __name__ == '__main__':

    matrix=[]
    matrix = [['' for col in range(15)] for row in range(5)]

    for i in range(0,5):
        n=input()

        for j in range(0, len(n)):
            matrix[i][j] = n[j]


    (col_reading(matrix))

