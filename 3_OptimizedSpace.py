# DP para soma de minkowski iterada, modelo 3

def MinkowskiSum(vetor, k):
    n = len(vetor)
    sum = max(vetor) * k
    prev = [False] * (sum + 1)
    curr = [False] * (sum + 1)
    aux = [False] * (sum + 1)
    
    for i in range(sum + 1):
        if i in vetor:
            prev[i] = True
            
    for z in range(1, k):
        for i in range(0, n):
            for j in range(1, sum + 1):
                if prev[j] == True:
                    curr[j+vetor[i]] = True
        prev = curr.copy()
        curr = aux.copy()
    return prev


if __name__ == "__main__":
    V = [1,3,7]
    k = 3
    print('V = {}'.format(V))
    print('k = {}'.format(k))
    res = MinkowskiSum(V, k)
    for i in range(max(V) * k + 1):
        if res[i] == True:
            print('{}'.format(i))
            
# Complexidade da op: O(maxV*k*k*n)
# Espaco da tentativa (dp): O(maxV*k)
# Sem recursao