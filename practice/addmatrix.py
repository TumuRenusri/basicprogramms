x=int(input())
y=int(input())
matrix1=[[int(input()) for i in range(x)] for j in range(y)]
matrix2=[[int(input()) for i in range(x)] for j in range(y)]
result =[[0 for i in range(x)] for j in range(y)]
for i in range(x):
    for j in range(y):
        result[i][j]=matrix1[i][j]+matrix2[i][j]
for i in range(x):
    for j in range(y):
        print(format(result[i][j],'<3'),end='')
    print()



