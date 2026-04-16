# BOLEANOS 
#condição verdadeira 
True 
#condição falsa
False

# condicionais
# se condicao
# else = se não
if True:
    print(" bloco IF vai ser executado")
else:
    print(" bloco ELSE não vai ser executado")



# operaqdores logicos : and e or 

#AND 
if True and True:
    print(" ambos os blocos vai ser executados ")
if True and False:
    print("  blocos não  vai ser executado ")
if False and False:
    print("  blocos não  vai ser executado ") 

#OR
if True or False:  
    print("bloco OR vai ser executado")
if False or False:
    print("  bloco OR não  vai ser executado ") 
if True or True:
    print("bloco OR vai ser executado")


# LISTA 
# declaracao

minha_lista = [1, 2, 3, 4, 5, 6,7,8]

#exibindo a lista 
print("Minha lista de exemplo: ", minha_lista)

#exibindo a lista 
minha_lista[0] = "python" #mudanca do primeiro elemento da lista
print("Minha lista de exemplo: ", minha_lista)

print("minha_lista[0]: ", minha_lista[0])
print("minha_lista[5]: ", minha_lista[5])#exibindo o sexto elemento da lista
print("minha_lista[1:7]: ", minha_lista[1:7])#exibindo do segundo elemento até o sexto elemento da lista
print("minha_lista[:6]: ", minha_lista[:6])#exibindo do primeiro elemento até o sexto elemento da lista
print("minha_lista[2:]: ", minha_lista[2:])#exibindo do terceiro elemento até o final da lista

# Metodos de lista 

#metodo append() - adiciona um elemento no final da lista
minha_lista.append("6")
print(" apos append(6): ", minha_lista)

# metodo index() - retorna o indice do elemento especificado
indice = minha_lista.index("6")
print(" indice do elemento '6': ", indice)

# metodo insert() - adiciona um elemento em um indice especifico
minha_lista.insert(2, 10)
print(" apos insert(2, 10): ", minha_lista)

# metodo pop - remove o elemento do indice especificado e retorna o valor removido
elemento_removido = minha_lista.pop(3)
print(" elemneto removido: ", elemento_removido)
print(" apos pop(3): ", minha_lista)

# metodo remove() - remove a primeira ocorrencia do elemento especificado
minha_lista.remove( 8)
print(" apos remove(8): ", minha_lista)

# metodo sort() - ordena os elementos da lista em ordem crescente
minha_lista.sort()
print(" apos sort(): ", minha_lista)

# TUPLAS : Coleção de elementos imutáveis, ou seja, não podem ser modificados após a criação da tupla.

#criando uma tupla de exemplo 
minha_tupla = (1,  2, 3, 4, )

print("Minha tupla  : ", minha_tupla)

print("minha_tupla[0]: ", minha_tupla[0])
print("minha_tupla[2]: ", minha_tupla[2])
print("minha_tupla[-1]: ", minha_tupla[-1])


# metodo count() - retorna o numero de vezes que um elemento aparece na tupla
contagem = minha_tupla.count(2)
print(" quantidade de vezes que o elemento '2' aparece: ", contagem)

indice = minha_tupla.index(3)
print(" indice da primeira ocorrencia do elemento '3': ", indice)

# DICIONARIO : Coleção de pares chave-valor

#  criando um diciionario de exemplo
pessoa = {"nome": "Joao", "idade": 30, "cidade": "Sao Paulo"}

# exibindo o dicionario 
print(" meu dicionario de exemplo: ", pessoa)

#acessando valores por chave
print(" nome: ", pessoa["nome"])
print(" idade: ", pessoa["idade"])
print(" cidade: ", pessoa["cidade"])

pessoa["sobrenome"] = "martins" # adicionou sobrenome ao dicionario
print("sobrenome: ", pessoa["sobrenome"])
print(" Meu dicionario de excemplo:", pessoa)

pessoa["idade"] = 31 # modificou a idade no dicionario'
print(" idade atualizada: ", pessoa["idade"])

#removendo um par de chave-valor do dicionario
del pessoa["sobrenome"]
print(" Meu dicionario de excemplo:", pessoa)

#metodo: keys(), values(), items()
chaves = list(pessoa.keys()) # obtendo todas as chaves do dicionario e convertendo para uma lista
print(" chaves do dicionario: ", chaves) #exibindo todas as chaves do dicionario
print('primeira chave: ', chaves[0]) #exibindo a primeira chave do dicionario

#metodos values 
valores = list(pessoa .values()) # obtendo todos os valores do dicionario 
print(" valores do dicionario: ", valores) # exibindo todos os valores do dicionario
print(" primeiro valor do dicionario: ", valores[0]) # exibindo o primeiro valor do dicionario







