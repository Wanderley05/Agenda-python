numero = int(input(' digite o fatorial que deseja calcular: '))
if numero > 0 and type(numero) == int:
    fatorial = 1
    for item in range(1, numero + 1):
        print(f'{fatorial} * {item}')
        fatorial = fatorial * item
        print(f'{fatorial}')
        print(f' o fatorial de { numero} é {fatorial}')     
    else :
        print('favor infromar apenas numeros inteirosd positivos ')   



# exemplo 2 chute o numero 
import random 
numero_secreto = random.randint(1, 10)
acertou = False
while acertou == False:
    chute = int(input('chute um numero entre 1 a 10: '))
if chute > numero_secreto:
    print(' chte um valor mais baixo')
elif chute < numero_secreto:
        print('chute um valor mais alto')
else:
        print('parabens voce acertou')
        acertou = True

