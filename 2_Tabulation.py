def isSubsetSum(vetor, k):
    n = len(vetor)
    sum = max(vetor) * k
    dp = [[False] * (sum + 1) for _ in range(k)]
    
    for i in range(sum + 1):
        if i in vetor:
            dp[0][i] = True
    for z in range(1, k):
        for i in range(0, n):
            for j in range(1, sum + 1):
                if dp[z-1][j] == True:
                    dp[z][j+vetor[i-1]] = True
    return dp


if __name__ == "__main__":
    V = [1,2,3,4,70]
    k = 3
    res = isSubsetSum(V, k)
    for i in range(max(V) * k + 1):
        if res[k-1][i] == True:
            print('{}'.format(i))