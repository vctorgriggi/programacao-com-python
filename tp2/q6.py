def primo(numero):
    if numero < 2:
        return False
    
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
        
    return True

print("Caro usuário, informe o intervalo para encontrar números primos:")
intervalo_inferior = int(input("Primeiramente, digite o limite inferior do intervalo: "))
intervalo_superior = int(input("Agora, digite o limite superior do intervalo: "))

primos = [] 

for numero in range(intervalo_inferior, intervalo_superior + 1):
    if primo(numero):
        primos.append(numero)

print("Ok, esses são os números primos encontrados no intervalo informado:", ', '.join(map(str, primos)))
print("E a quantidade de números primos encontrados foi:", len(primos))
