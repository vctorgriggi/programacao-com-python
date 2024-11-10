print("Oi! Vamos fazer algumas... operações matemáticas?")
num1 = float(input("Por favor, digite o primeiro número: "))
num2 = float(input("Agora, digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2 if num2 != 0 else "Oops! Não é possível dividir por zero."
divisao_inteira = num1 // num2 if num2 != 0 else "Oops! Não é possível dividir por zero."

print("Ok! Veja o resultado final das operações:")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Divisão inteira: {divisao_inteira}")