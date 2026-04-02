# DP para soma de minkowski iterada, modelo 1

dp = []

def Rec(vetor, sum, k, pk):
    # casos base e de parada
    if k > pk:
        for j in range(sum+1):
            if dp[pk-1][j] == True:
                for i in vetor:
                    dp[pk][i + j] = True
        Rec(vetor, sum, k, pk+1)
    

def IteratedMinkowskiSum(vetor, k):
    global dp
    sum = k * max(vetor)
    dp = [[-1 for _ in range(sum + 1)] for _ in range(k)]
    
    for i in vetor:
        dp[0][i] = True
    if sum > max(vetor) * k:
        return
    Rec(vetor, sum, k, 1)


if __name__ == "__main__":
    
    V = [1, 3, 7, 11]
    k = 3
    print('V = {}'.format(V))
    print('k = {}'.format(k))

    IteratedMinkowskiSum(V, k)
    for i in range(max(V) * k + 1):
        if dp[k-1][i] == True:
            print('{}'.format(i))


    
# Complexidade da op: O(maxV*k*k*n)
# Espaco ocupado: O(maxV*k*k)
# Recursivo
