# variavel
velocidade_internet = 500
print(velocidade_internet)

# numeros inteiros (int)
idade = 25
# numeros decimais (float)
altura = 1.75
# texto(STRING)
nome = "Alice"
# booleano (True ou False)(bool)
estudante = True

print(type(idade))


salario_mensal = float(input("digite seu salario mensal : "))
horas_trabalho_mes = int(
    input("digite quantas horas voce trabalho por mes : "))
valor_hora = salario_mensal / horas_trabalho_mes
print("o valor da sua hora de trabalho é : ", valor_hora)

# condicionais - if elf else 

trabalho_terminado = True 
if trabalho_terminado == True:
    print("Bora!")
else:
    print("Não posso sair ")



estou_livre = False 
if estou_livre == True:
    print("vamos estou livre!")
else:
    print("não posso sair estou ocupado")


#COMPARAR VALORES
atrasos = int(input("quantas faltas voce tem ? : "))
if atrasos >= 3:
    print("você está suspenso!")
elif atrasos == 2:
    print("mais uma falta e estara suspenso !")
elif atrasos == 1:
    print("mais duas faltas e estara suspenso !")
else:
    print("pode entrar!")



valor_primeiro = int(input("digite o primeiro valor : "))
valor_segundo = int(input("digite o segundo valor : "))
if valor_primeiro > valor_segundo:
    print("o primeiro valor e maior que o segundo valor")
elif valor_primeiro < valor_segundo:
    print("o segundo valor e maior que o primeiro valor")
else:
    print(" os valores são iguais ")

# laços de repetição 

# range nunca inclui o ultimo numero 
for item in range(4):
    print(item)

#lista de nomes 
nomes = ["Alice", "Bob", "Charlie", "David"]
for nome in nomes:
    print(nome)


idades = [13,15,18,30,50,75 ]
for idade in idades:
    if idade >= 18:
        print(f"{idade} é maior de idade : ")
    else:
        print(f"{idade} é menor de idade : ")


# validador de semhas
# len conta o numero de caracteres de uma string
senhas = ["senha123", "admin", "123456", "qwerty"]
for senha in senhas:
    if len(senha) >= 6:
        print(f"{senha} é uma senha valida : ")
    else:
        print(f"{senha} é uma senha invalida : ")        

#while
'''
while condição 
# coigo a ser executado 
'''
tentativas = 0 
while tentativas < 3:
    print('tente novamnete')
tentativas = tentativas + 1

# quando queremos que uma ação continue acontecendo ate um criterio seja satifeito 
# so pode logar se digitar a senha certa 
senha = ''
while senha != 'senha123':
    senha = input('digite  a senha correta : ')
print('senha correta, logando...')
# garatir que algo esteja preenchido
# so devo continuar, se o usuario digitar seu nome 
nome =''
while nome =='':
    nome = input ('digite seu nome: ')
    print(f'ola {nome} , seja bem vindo!')


# contadores dentro do while
# ser avisado as 17hrs do por do sol 

horario = 0
while horario <= 17:
    print(horario)
    horario = horario + 1 
    print(' hora de ver o por do sol !')



# EXEMPLO 
usuario = ''
senha = ''
tentativas = 0
while (usuario != 'jhonatan'or senha != 'senha123') and tentativas < 3:
    usuario = input('digite seu usuario :')
senha = input('digite sua senha :')
tentativas += 1
if usuario == 'jhonatan' and senha == 'senha123':
    print('login bem sucedido!')
else:
    print('login falhou, tente novamente mais tarde!')

    # LISTAS 

precos= [10,20,30]
print(precos[0]) # acessando o primeiro elemento da lista
print(precos[1]) # acessando o segundo elemento da lista   

nomes = ["Alice", "Bob", "Charlie", "David"]
print(nomes[0]) # acessando o primeiro elemento da lista
print(nomes[1]) # acessando o segundo elemento da lista

# encontrar o indice automaticamente 
nomes = ["Alice", "Bob", "Charlie", "David"]
print(nomes.index("Charlie")) # retorna o indice do elemento "Charlie"  

#manipular - ad novos itens a lista
salarios = [3000, 4000, 5000]
salario_usuario = float(input("qual e o seu salario: "))
salarios.append(salario_usuario)
print(salarios)



#exemplo calcle o total pago a todos os funcionarios
salarios = [3000, 4000, 5000]
total = 0 
for salario in salarios:
    total = total + salario
    print(total)

# funcoes
# exemplo
def saudacao(nome):
    print(f"ola, {nome}!")

print("\n chamando a função saudacao: ")
saudacao("Alice")
saudacao("Bob")

# funcao com retorno 

def quadrado ( numero):
    resultado = numero ** 2
    return resultado

print("\n chamando a função quadrado: ")
resultado_quadrado = quadrado(5)
print(" resultado da funcao quadrado: ", resultado_quadrado)

# funcao com multiplos parametros

def soma (numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("\n chamando a função soma: ")
resultado_soma = soma(20, 50 )
print(" a soma do numero 20 e numero 50 é : ", resultado_soma)


