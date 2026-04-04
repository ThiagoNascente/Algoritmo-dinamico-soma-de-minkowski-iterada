# BF para soma de minkowski iterada, modelo 0

def Rec(vetor, n, k, pos, sum):

    if pos < n and k > 0:
        Rec(vetor, n, k, pos+1, sum)
        Rec(vetor, n, k-1, pos+1, sum + vetor[pos])
    if k == 0:
        res.add(sum)

    
def IteratedMinkowskiSum(vetor, k):
    v = []
    global res
    res = set()
    
    for i in vetor:
        v = v + [i] * k
    
    Rec(v, len(v), k, 0, 0)
    return res


if __name__ == "__main__":
    
    V = [1, 3, 4, 10, 11]
    k = 7
    print('V = {}'.format(V))
    print('k = {}'.format(k))

    result = IteratedMinkowskiSum(V, k)
    result_ordered = sorted(result)
    for i in result_ordered:
        print('{}'.format(i))


    
# Complexidade da op: O(2^(n * k))
# Recursivo