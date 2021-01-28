import random
def zero_mat(mat,M,N):
    mat_zero = mat.copy()
    has_first_row_zero,has_first_column_zero = False,False
    for i in range(M):
        if mat_zero[i][0] == 0:
            has_first_column_zero = True

    for i in range(N):
        if mat_zero[0][i] == 0:
            has_first_row_zero = True
    for i in range(1,M):
        for j in range(1,N):
            if mat_zero[i][j] == 0:
                mat_zero[i][0],mat_zero[0][j] = 0,0
    
    # Set Zero
    for i in range(1,M):
        if mat_zero[i][0] == 0:
            mat_zero[i] = [0] * N
        
    for j in range(1,N):
        if mat_zero[0][j] == 0:
            for i in range(1,M):
                mat_zero[i][j] = 0
    
    if has_first_row_zero == True:
        mat_zero[0] = [0] * N

    if has_first_column_zero == True:
        for i in range(0,M):
                mat_zero[i][0] = 0
    return mat_zero


def get_random_mat(M,N):
    return [[random.randint(-10,10) for i in range(N)] for i in range(M)]

def print_mat(mat,M,N):
    for i in range(M):
        for j in range(N):
            print("{0:4d}".format(mat[i][j]),end=" ")
        print()

if __name__ == "__main__":
    M,N = 10,10
    a = get_random_mat(M,N)
    print_mat(a,M,N)
    print_mat(zero_mat(a,M,N),M,N)