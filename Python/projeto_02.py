#   programa que peça um numero inteiro e determine se ele e par ou impar
numero = int(input('digite um numeiro inteiro:'))
if numero % 2 == 0:  # se o numero for divisivel por 2, ou seja, o resto da divisão for igual a zero, ele é par
    print('o numero {} é par'.format(numero))
else:
    print('o numero  {} é impar'. format(numero))
# format é um método de formatação de string que permite inserir valores em uma string de forma mais legível e organizada. Ele é usado para substituir os placeholders
# (chaves {}) por valores específicos. No exemplo acima, o número digitado pelo usuário é inserido na string usando o método format, tornando a mensagem mais clara e fácil de entender.
# {} é um placeholder que será substituído pelo valor do número digitado pelo usuário. O método format() pega o valor de numero e o insere no lugar do placeholder,
#  resultando em uma mensagem personalizada que indica se o número é par ou ímpar.
