# Uma implementacao python para o problema subsetsum
# usando recursao e memorizacao

def isSubsetSumRec(vetor, n, sum, k, pk, memo):
    # Recebe vetor, o tamanho do vetor, a soma e a quantidade de valores do vetor que podem ser considerados...
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
    
    """
    ENTRADAS vetor, e k somas
    """
    
    vetor = [1, 2, 7]
    k = 3
    
    V = []
    for i in range(1, k+1):
        V = V + vetor
    print(V)
    
    for i in range(1, max(V)*k + 2):
        if isSubsetSum(V, i, k):
            print("{} Sim".format(i))
        else:
            print("{} ---".format(i))
    
# fonte: https://www.geeksforgeeks.org/dsa/subset-sum-problem-dp-25/
# para caso geral
# complexidade da fonte: O(sum*n)
# buscar complexidade da tentativa: O(sum*n)
# Espaco da tentativa: O(sum*n)

"""
Constroe-se a tabela sum * k 
"""