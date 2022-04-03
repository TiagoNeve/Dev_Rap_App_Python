arquivo = open("dados.txt", "r")

conteudo = arquivo.readlines()

print("Tipo do conteúdo: ", type(conteudo))

print("Conteúdo retornado pelo readline:")
print(repr(conteudo))

arquivo.close()
