Aqui temos um exemplo de algoritmo de soma de minkowski de complexidade aproximada de O(target * k), onde target é o nosso alvo da soma, e k é o número de iterações na soma de minkowski considerando um conjunto C.

A soma de minkowski é tal que sendo dois conjuntos A e B, temos que A + B = {a + b : a pertence a A e b pertence a B}

É nítido que pela definição, a complexidade da soma é de n^m, onde n é o número de elementos do conjunto e m é o número de fatores.

A + A + A + A = O(|A|^4)

OBS.: Para valores k muito grandes, o algoritmo é lento