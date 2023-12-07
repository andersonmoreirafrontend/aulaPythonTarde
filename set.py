lista = ("tarefa1", "tarefa2", "tarefa3")
print(lista) #mosta lista
print(type(lista))# mostra tipo de lista -> tuple
x = list(lista)
print(type(x))
x.append("tarefa4")
lista = tuple(x)
print(lista)
print(type(lista))
