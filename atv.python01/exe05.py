altura = float(input("Qual a altura da parede? "))
largura = float(input("Qual a largura da parede? "))
rendimento = int(input("Qual o rendimento da tinta em m²? ")) #rendimento da tinta


metro_quadrado = (altura/100) * (largura/100) #convertendo de cm para metros

#de_maos = rendimento / 2 #quantidade de demãos que será pintado

litro = (2 * metro_quadrado) / rendimento #quantidade de tinta em litros

print(f"O local mede {metro_quadrado}m²" )
print(f"São necessário {litro} latas para pintar o local. ")
