#Coleta dos dados:
nome = input("Seu nome: ")
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em kg: "))

#Calculo do IMC:
total = peso / (altura ** 2)

#Formatação do IMC:
imc_formatado = f"{total:.2f}"

#Criação do txt:
with open("imc2.txt", 'a') as arquivo:
    #Adiciona as informações no txt:
    arquivo.write("Ola "+nome+ ", seu IMC eh: "+str(imc_formatado) + '\n')
