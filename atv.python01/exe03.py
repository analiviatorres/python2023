eleitores = int(input("Número de Eleitores no Municipio: "))
votos_nulos = int(input("Número de votos Nulos: "))
votos_branco = int(input("Número de votos Branco: "))
total = eleitores - votos_branco - votos_nulos
 

porcent_nulos = (votos_nulos / eleitores) * 100
porcent_brancos = (votos_branco / eleitores) * 100
porcent_validos = (total / eleitores) * 100

print(f"votos nulos é: {porcent_nulos:.2f}%, votos branco é: {porcent_brancos:2f}% e votos válidos é: {porcent_validos:2f}%")
