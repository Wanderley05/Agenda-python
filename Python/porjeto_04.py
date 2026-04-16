# faça um program que peça as quatros notas de 10 alunos, calcule e armazene num vetor a media de cada aluno, imprima o numero de alunos maior ou igual a 7.0
aluno_1= [1,2,3,4]
aluno_2 = [7,8,6,7]
aluno_3 = [5,4,3,10] 
aluno_4 = [10, 10, 6, 8]

media_aluno_1 = sum(aluno_1) / len(aluno_1)# sum soma os elementos de uma lista e len conta o numero de elementos da lista
media_aluno_2 = sum(aluno_2) / len(aluno_2) # sum soma os elementos de uma lista e len conta o numero de elementos da lista
media_aluno_3 = sum(aluno_3) / len(aluno_3)# sum soma os elementos de uma lista e len conta o numero de elementos da lista
media_aluno_4 = sum(aluno_4) / len(aluno_4)# sum soma os elementos de uma lista e len conta o numero de elementos da lista

medias = [media_aluno_1, media_aluno_2, media_aluno_3, media_aluno_4]
alunos = ['aluno_1', 'aluno_2', 'aluno_3', 'aluno_4']

alunos_acima_7 = []
for i, media in enumerate(medias):# enumerate retorna o indice e o valor de cada elemento da lista
    if media > 7.0:
        alunos_acima_7.append(alunos[i])#i e o indice do aluno na lista de alunos, e append adiciona o nome do aluno na lista de alunos_acima_7

print("Alunos com média maior que 7.0:")
for aluno in alunos_acima_7:
    print(f"- {aluno}")

print(f"Total: {len(alunos_acima_7)} alunos")

