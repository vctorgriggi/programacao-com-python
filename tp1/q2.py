def minutos_para_horas(minutos):
    horas = minutos // 60
    minutos = minutos % 60
    return horas, minutos

def horas_para_minutos(horas, minutos):
    return horas * 60 + minutos

print("Oi! Vamos fazer algumas... operações de conversão?")
inp_minutos = int(input("Por favor, digite a quantidade de minutos: "))
horas, minutos = minutos_para_horas(inp_minutos)

print(f"Show! {inp_minutos} minutos equivalem a {horas} horas e {minutos} minutos.")

print("\nAgora, vamos fazer o contrário!")
inp_horas = int(input("Digite a quantidade de horas: "))
inp_minutos2 = int(input("E quantos minutos? "))

total_minutos = horas_para_minutos(inp_horas, inp_minutos2)

print(f"Ok! {inp_horas} horas e {inp_minutos2} minutos equivalem a {total_minutos} minutos.")