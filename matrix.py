matrix1=[[2,3],[3,5]]
matrix2=[[9,8],[9,4]]
result =[[matrix1[i][j] +matrix2[i][j]for i in range(2)]for j in range(2)]
for rows in result:
    print(rows)
