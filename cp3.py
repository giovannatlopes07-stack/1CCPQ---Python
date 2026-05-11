temperaduras = [
    [28,31,34,33],
    [25,27,29,28],
    [32,35,36,34],
    [24,26,25,27]
]

#PERCORRENDO MATRIZ
for linha in range (len(temperaduras)):
    for coluna in range (len(temperaduras[linha])):
        print(f"Sala {linha + 1}, Horário {coluna + 1}: {temperaduras[linha][coluna]}C")

#MEDIAS DE TEMPERATURAS
print("--- Medias das temperaturas de cada sala ---")
media_sala1 = (28+31+34+33)/4
print(f"A media das temperaturas da sala 1 é: {media_sala1}")

media_sala2 = (25+27+29+28)/4
print(f"A media das temperaturas da sala 2 é: {media_sala2}")

media_sala3 = (32+35+36+34)/4
print(f"A media das temperaturas da sala 3 é: {media_sala3}")

media_sala4 = (24+26+25+27)/4
print(f"A media das temperaturas da sala 4 é: {media_sala4}")

#TEMPERATURAS MAIOR OU IGAUL A 33
print("--- Temperaturas >= 33C por Sala ---")

# PERCORRENDO E CONTANDO
for i in range(len(temperaduras)):
    contador = 0  # Reseta o contador para cada nova sala

    for temp in temperaduras[i]:
        if temp >= 33:
            contador += 1

    print(f"Sala {i + 1}: {contador} temperatura(s) maior(es) ou igual(is) a 33C")

#MOSTRAR A SALA DE MAIOR RISCO
print("--- Sala com maior registro crítico ---")
print(f"A sala que apresenta maior risco é a: Sala 3")