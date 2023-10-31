# Exercício Python 30: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.
mediaidade = 0
somaidade = 0 
Hnomemaisvelho = " "
maioridadeH = 0
Mmenorque20 = 0
for i in range(1,5):
    nome = str(input(f"digite o nome da {i}ª pessoa: "))
    idade = int(input("Qual é a sua idade: "))
    sexo = str(input("digite M para MASCULINO \n F para FEMININO: \n "))
    sexo = sexo.upper()
    
    somaidade += idade

    if sexo == "M" and idade >= maioridadeH:
        maioridadeH = idade
        homemmaisvelho = nome
    if sexo == "F" and idade < 20:
        Mmenorque20 += 1
    else:
        print("sexo infalido")
   

mediaidade = somaidade/4

print(f'A média de idade do grupo é de {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadeH} anos e se chama {Hnomemaisvelho}.')
print(f'Ao todo são {Mmenorque20} mulheres com menos de 20 anos.')
