valores = [True, False] # valores para a tabela verdade

print("p\tq\tr\tT = p and q\tS = T or r") #cria o cabeçalho da tabela, \t é uma tabulação
print("-" * 40) #imprime uma linha de traços para separar visualmente o cabeçalho das respostas

for p in valores:
    for q in valores:
        for r in valores: 
            conjuncao = p and q
            s = conjuncao or r
            print(f"{p}\t{q}\t{r}\t{conjuncao}\t{s}")
"""três loops aninhados um dentro do outro, gerando 8 combinações possíveis de p, q e r com os valores V e F"""