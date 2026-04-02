# DP para soma de minkowski iterada, modelo 1

def MinkowskiSumRec(vetor, n, sum, k, pk, memo):
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
        memo[k][sum] = MinkowskiSumRec(vetor, n - 1, sum, k, pk, memo)
    else:
        memo[k][sum] = (MinkowskiSumRec(vetor, n - 1, sum, k, pk, memo) or 
                MinkowskiSumRec(vetor, n - 1, sum - vetor[n - 1], k, pk+1, memo))
    return memo[k][sum]

def MinkowskiSum(vetor, sum, k):
    n = len(vetor)
    memo = [[-1 for _ in range(sum + 1)] for _ in range(k + 1)]
    if sum > max(vetor) * k:
        return False 
    return MinkowskiSumRec(vetor, n, sum, k, 0, memo)

if __name__ == "__main__":
    
    vetor = [1, 3, 7]
    k = 3
    print('V = {}'.format(vetor))
    print('k = {}'.format(k))
    V = []
    for i in range(1, k+1):
        V = V + vetor
    
    for i in range(1, max(V)*k + 1):
        if MinkowskiSum(V, i, k):
            print("{}".format(i))

    
# Complexidade da op: O(maxV*k*k*n)
# Espaco da tentativa: O(maxV*k*k)
# Recursivo
