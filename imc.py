nome = input("Seu nome: ")
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em kg: "))

total = peso / (altura ** 2)

with open("imc.txt", 'w') as arquivo:
    arquivo.write("Ola "+nome+ ", seu IMC eh: "+str(total) + '\n')

with open("imc.txt", 'a') as arquivo:
    arquivo.write("Ola "+nome+ ", seu IMC eh: "+str(total) + '\n')
