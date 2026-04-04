# DP para soma de minkowski iterada, modelo 1

def Rec(vetor, bigst, k, pk):
    # casos base e de parada
    if k > pk:
        for j in range(bigst+1):
            if dp[pk-1][j] == True:
                for i in vetor:
                    dp[pk][i + j] = True
        Rec(vetor, bigst, k, pk+1)
    

def IteratedMinkowskiSum(vetor, k):
    global dp
    bigst = k * max(vetor)
    dp = [[-1 for _ in range(bigst + 1)] for _ in range(k)]
    
    for i in vetor:
        dp[0][i] = True
    Rec(vetor, bigst, k, 1)
    return dp


if __name__ == "__main__":
    
    V = [1, 3, 7, 11]
    k = 3
    print('V = {}'.format(V))
    print('k = {}'.format(k))

    res = IteratedMinkowskiSum(V, k)
    for i in range(max(V) * k + 1):
        if res[k-1][i] == True:
            print('{}'.format(i))


    
# Complexidade da op: O(maxV*k*k*n)
# Espaco ocupado: O(maxV*k*k)
# Recursivo
