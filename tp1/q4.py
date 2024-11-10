def calculadora(operacao, num1, num2):
    if operacao == "adição":
        return num1 + num2
    elif operacao == "subtração":
        return num1 - num2
    elif operacao == "multiplicação":
        return num1 * num2
    elif operacao == "divisão":
        return num1 / num2 if num2 != 0 else "Oops! Não é possível dividir por zero."
    else:
        return "Oops! Operação inválida"
    
print("Oi! Vamos fazer algumas... operações matemáticas?")
num1 = float(input("Por favor, digite o primeiro número: "))
num2 = float(input("Agora, digite o segundo número: "))
operacao = input("Qual operação você deseja realizar? (adição, subtração, multiplicação, divisão): ").strip().lower()

operacoes = ["adição", "subtração", "multiplicação", "divisão"]

if operacao in operacoes:
    resultado = calculadora(operacao, num1, num2)
    print(f"Ok! O resultado da {operacao} é {resultado}.")
else:
    print("Oops! Operação inválida.")