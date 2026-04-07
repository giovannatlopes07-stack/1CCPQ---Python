#PARECE UM PRINT#
# FUNÇÃO COM PARAMETRO SEM RETORNO
def boas_vindas(nome):
    print(f"Olá, {nome}!! Seja bem-vindo!")

nome_digitado = input("Digite o seu nome: ")
boas_vindas(nome_digitado)

# FUNÇÃO COM PARAMETRO E COM RETORNO
def soma(num_a, num_b):
    soma = num_a + num_b
    return soma #return SÓ RETORNA A INFORMAÇÃO NÃO PRINT

resultado_soma = soma(1, 2)
print(resultado_soma)
