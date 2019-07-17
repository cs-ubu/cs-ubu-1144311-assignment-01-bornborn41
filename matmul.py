
# 1. read mt A from 'A.csv'


# 2. read mt b from'b.csv


# 3. find the result of c = A*b


# 4.print C


def readm(name):
    a =open(name,'r')
    b =[]
    for i in a.readlines():
        b.append([float(x) for x  in i.strip().split(',')])
    a.close()
    return b
def matmul(A,b):
    m,n = len(A),len(b[0])

    if len(A[0])==len(b):
        C = [ [0]*n]*m
        for r in range(m):
            for c in range(n):
                C[r][c]=sum(A[r][j]*b[j][c] for j in  range(len(A[0])))
        return C
    else : 
        return []
