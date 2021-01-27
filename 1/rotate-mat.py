def rotate(mat,N:int):
    rotated = [[0 for i in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            rotated[j][N-(i+1)] = mat[i][j]
    return rotated


if __name__ == "__main__":
    print(rotate([[1,2,3],[4,5,6],[7,8,9]],3))


