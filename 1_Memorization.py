# DP para soma de minkowski iterada, modelo 1

def isSubsetSumRec(vetor, n, sum, k, pk, memo):
    # casos base e de parada
    
    if sum == 0 and pk == k:
        return True
    if n <= 0:
        return False
    if k == pk:
        return False
    if memo[pk][sum] != -1:
        return memo[pk][sum]
    if vetor[n - 1] > sum:
        memo[k][sum] = isSubsetSumRec(vetor, n - 1, sum, k, pk, memo)
    else:
        memo[k][sum] = (isSubsetSumRec(vetor, n - 1, sum, k, pk, memo) or 
                isSubsetSumRec(vetor, n - 1, sum - vetor[n - 1], k, pk+1, memo))
    return memo[k][sum]

def isSubsetSum(vetor, sum, k):
    n = len(vetor)
    memo = [[-1 for _ in range(sum + 1)] for _ in range(k + 1)]
    if sum > max(vetor) * k:
        return False 
    return isSubsetSumRec(vetor, n, sum, k, 0, memo)

if __name__ == "__main__":
    
    vetor = [1, 3, 7]
    k = 3
    
    V = []
    for i in range(1, k+1):
        V = V + vetor
    print(V)
    
    for i in range(1, max(V)*k + 1):
        if isSubsetSum(V, i, k):
            print("{}".format(i))

    
# buscar complexidade da op: O(maxV*k*n)
# Espaco da tentativa: O(maxV*k*k)
# Recursivo
