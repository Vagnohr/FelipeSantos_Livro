s="camel"
#Concatenação
print("The"+s+"ran away!")
#Interpolação
print("Tamanho de %s=>%d"(s,len(s)))
#String tratada como sequência
for ch in s:
    print(s.upper())
#Strings são objetos
if s.startswith("C"):
    print(s.upper())
#O que acontecerá?
print(3*s)
#3*s é consistente com s+s+s