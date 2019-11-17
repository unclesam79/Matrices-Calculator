size = 9
matrix1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
matrix2 = [0, -1, -2, -3, -4, -5, -6, -7, -8]

resultant1 = [0 for x in range(size)]
resultant1[0] = (matrix1[0] * matrix2[0]) + (matrix1[1] * matrix2[3]) + (matrix1[2] * matrix2[6])
resultant1[1] = (matrix1[0] * matrix2[1]) + (matrix1[1] * matrix2[4]) + (matrix1[2] * matrix2[7])
resultant1[2] = (matrix1[0] * matrix2[2]) + (matrix1[1] * matrix2[5]) + (matrix1[2] * matrix2[8])
resultant1[3] = (matrix1[3] * matrix2[0]) + (matrix1[4] * matrix2[3]) + (matrix1[5] * matrix2[6])
resultant1[4] = (matrix1[3] * matrix2[1]) + (matrix1[4] * matrix2[4]) + (matrix1[5] * matrix2[7])
resultant1[5] = (matrix1[3] * matrix2[2]) + (matrix1[4] * matrix2[5]) + (matrix1[5] * matrix2[8])
resultant1[6] = (matrix1[6] * matrix2[0]) + (matrix1[7] * matrix2[3]) + (matrix1[8] * matrix2[6])
resultant1[7] = (matrix1[6] * matrix2[1]) + (matrix1[7] * matrix2[4]) + (matrix1[8] * matrix2[7])
resultant1[8] = (matrix1[6] * matrix2[2]) + (matrix1[7] * matrix2[5]) + (matrix1[8] * matrix2[8])

resultant2 = [0 for x in range(size)]
l1 = [(0, 0), (0, 1), (0, 2), (3, 0), (3, 1), (3, 2), (6, 0), (6, 1), (6, 2)]
for i in range(size):
    resultant2[i] = (matrix1[l1[i][0]] * matrix2[l1[i][1]]) + (matrix1[l1[i][0]+1] * matrix2[l1[i][1]+3]) + (matrix1[l1[i][0]+2] * matrix2[l1[i][1]+6])

print(resultant1)
print(resultant2)
if resultant1 == resultant2:print("Yup")
