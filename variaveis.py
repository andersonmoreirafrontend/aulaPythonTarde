"""
nome = "Anderson"

numero = 6

troco = 4.65

is_login = True #sempre com primeira letra maiuscula True
print(type(nome))
print(type(numero))
print(type(troco))
print(type(is_login))
"""

nomes = ["Maria","João" "Fabio","Ana","Ze"]
print(type(nomes)) #mostrar o tipo list
print(nomes)#mostrar a list
# print(nomes [1]) # mostra a posição 2
print(nomes.pop()) # exclui a ultima posição e mostra o nome
print(nomes) # mostra a lista novamente
nomes.pop() #exclui a ultima posição
print(nomes)
nomes.append("Ana") #adicionar um nome no final da lista
nomes.append("Lorenzo")
print(nomes)

for x in nomes:
    print(x)
