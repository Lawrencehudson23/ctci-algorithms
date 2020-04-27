# 1.7 Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
# Hints: 51, 0100
# array = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]


def rotateMatrix(mat):
    for i in range(len(mat)-1):
        for j in range(i, (len(mat)-1-i)):
            mat[i][j], mat[i+j][len(mat)-1-i] = mat[i +
                                                    j][len(mat)-1-i], mat[i][j]
            mat[i+j][len(mat)-1-i], mat[len(mat)-1-i][len(mat) - 1 -
                                                      j] = mat[len(mat)-1-i][len(mat) - 1-j], mat[i+j][len(mat)-1-i]
            mat[len(mat)-1-i][len(mat)-1-j], mat[len(mat)-1 -
                                                 j][i] = mat[len(mat)-1-j][i], mat[len(mat)-1-i][len(mat)-1-j]


print(rotateMatrix(array))
[13, 9, 5, 1]
[14, 10, 6, 2]
[15, 11, 7, 3]
[16, 12, 8, 4]
