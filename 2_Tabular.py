# DP para soma de minkowski iterada, modelo 2

def IteratedMinkowskiSum(vetor, k):
    n = len(vetor)
    bigst = max(vetor) * k
    dp = [[False] * (bigst + 1) for _ in range(k)]
    
    for i in vetor:
        dp[0][i] = True
    for z in range(1, k):
        for i in range(n):
            for j in range(bigst + 1):
                if dp[z-1][j] == True:
                    dp[z][j+vetor[i]] = True
    return dp


if __name__ == "__main__":
    V = [1,3,7]
    k = 3
    print('V = {}'.format(V))
    print('k = {}'.format(k))
    res = IteratedMinkowskiSum(V, k)
    for i in range(max(V) * k + 1):
        if res[k-1][i] == True:
            print('{}'.format(i))
            
# Complexidade da op: O(maxV*k*k*n)
# Espaco ocupado (dp): O(maxV*k*k)
# Sem recursao