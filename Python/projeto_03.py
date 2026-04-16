# faça um program que peça uma nota, entre 0 e 10 . mostre uma mensagem caso o valor seja invalido e continue pedindo ate que o usuario informe um valor valido
nota = float(input('digite um valor de 0 a 10:'))
while nota < 0 or nota > 10:
    if nota < 0 or nota > 10:
        print('valor invalido, tente novamente')
        nota = float(input('digite um valor de 0 a 10:'))
else:
    print('valor valido, obrigado')
