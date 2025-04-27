# implemente a tabela verdade da seguinte expressão lógica
# S = ~(p v q) ^ r

valores = [True, False]

print("p\tq\tr\tp or q\tNot T\tS = T e r")
print("-" * 50)

for p in valores:
    for q in valores:
        for r in valores:
            T = p or q
            negacao_T = not T
            S = negacao_T and r
            print(f"{p}\t{q}\t{r}\t{T}\t{negacao_T}\t{S}")