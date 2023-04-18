nota1 = int(input("Digite a nota do primeiro Bimestre! "))
nota2 = int(input("Digite a nota do segundo Bimestre! "))

media = (nota1 + nota2) / 2
 
if media >= 7:
    print("Aprovado por Média! ")
elif 2 <= media < 7:
    print("Em recuperação! ")
elif media < 2:
    (print("Reprovado"))
