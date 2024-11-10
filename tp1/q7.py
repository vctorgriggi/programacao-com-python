def calcular_imc(peso, altura):
    altura_metros = altura / 100 
    return peso / (altura_metros ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade grau 1"
    elif imc < 40:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"

print("Oi!  Você savia que devemos visar uma vida saudável? Por isso, vamos calcular o seu IMC.")	
peso = float(input("Por favor, me diga, qual é o seu peso? "))
altura = float(input("E sua altura? Em centímetros, por favor. "))

imc = calcular_imc(peso, altura)
print("Olha, com base em minhas análises, seu IMC é", imc, "e você está classificado como", classificar_imc(imc), ".")