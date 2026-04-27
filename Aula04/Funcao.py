def verificar_nota(nota):
    while nota < 0 or nota > 10:
        print('A nota deve estar entre 0 e 10')
        nota = float(input('Diite a nota novamente: '))
    return nota

notaA = float(input('Digite a 1 nota: '))
notaA = verificar_nota(notaA)

notaB = float(input('Digite a 2 nota: '))
notaB = verificar_nota(notaB)

media = (notaA + notaB) / 2
print(media)