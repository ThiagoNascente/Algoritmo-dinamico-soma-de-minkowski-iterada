# DP para soma de minkowski iterada, modelo 1

memo = []

def MinkowskiSumRec(vetor, sum, k, pk):
    # casos base e de parada
    if k > pk:
        for j in range(sum+1):
            if memo[pk-1][j] == True:
                for i in vetor:
                    memo[pk][i + j] = True
        MinkowskiSumRec(vetor, sum, k, pk+1)
    

def MinkowskiSum(vetor, k):
    global memo
    sum = k * max(vetor)
    memo = [[-1 for _ in range(sum + 1)] for _ in range(k)]
    
    for i in vetor:
        memo[0][i] = True
    if sum > max(vetor) * k:
        return
    MinkowskiSumRec(vetor, sum, k, 1)


if __name__ == "__main__":
    
    V = [1, 3, 7, 11]
    k = 3
    print('V = {}'.format(V))
    print('k = {}'.format(k))

    MinkowskiSum(V, k)
    for i in range(max(V) * k + 1):
        if memo[k-1][i] == True:
            print('{}'.format(i))


    
# Complexidade da op: O(maxV*k*k*n)
# Espaco ocupado: O(maxV*k*k)
# Recursivo
