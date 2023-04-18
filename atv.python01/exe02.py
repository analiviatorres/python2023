print('CALCULANDO AS RAIZES DA EQUAÇÃO')

valor_a = int(input("Digite o valor de A: "))
valor_b = int(input("Digite o valor de B: "))
valor_c = int(input("Digite o valor de C: "))

delta = (valor_b**2) -4 * (valor_a * valor_c)

#print(delta)

equacao = delta**0.5

raiz_1 = (- valor_b + equacao) / (2 * valor_a)
raiz_2 = (- valor_b - equacao) / (2 * valor_a)

print(f"raiz 1:{raiz_1} e raiz 2:{raiz_2}")