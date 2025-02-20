dic={"nome":"Shirley Manson","banda":"Garbage"}
#acessando elementos:
print("Nome:",dic["nome"])
#adicionando elementos:
dic["album"]="Version 2.0"
#Apagando um elemento do dicionário:
del dic["album"]
#Obtendo os items, chaves e valores:
print("items:",dic.items())
print("chaves:",dic.keys())
print("valores:",dic.values())
