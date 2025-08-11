nome =input("digite seu nome: ")

peso =float(input("Digite seu peso:"))
altura = float(input("digite sua altura: "))

imc  = peso / (altura * altura)

if imc < 18.5:
    print("ABAIXO DO PESO")
elif imc < 24.9:
    print   

print(f"o IMC do aluno {nome} é : {imc}")