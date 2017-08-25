import sys
 
saida = open('resultado.txt', 'w') # abrindo arquivo de saida
 
for linha in sys.stdin:
    linha = linha.split(';')
    aluno = linha[0]
    trabalho1 = int(linha[1])
    trabalho2 = int(linha[2])
    trabalho3 = int(linha[3])
    media = (trabalho1 + trabalho2 + trabalho3) / 3
    saida.write(aluno + ': ') # escrevendo no arquivo
    if media >= 5:
        saida.write('Aprovado\n') # escrevendo no arquivo
    elif media >= 3:
        saida.write('Recuperação\n') # escrevendo no arquivo
    else:
        saida.write('Reprovado\n') # escrevendo no arquivo
 
saida.close() # fechando o arquivo de saida