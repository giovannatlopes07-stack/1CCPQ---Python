endpoints = ["/login", "/produtos", "/pedidos"]
status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]
def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299

#FUNÇÃO PARA DETECTAR 2 ERROS SEGUIDOS DE REQUISIÇÃO EM 1 ENDPOINT
#RETORNAR TRUE CASO TENHA 2 ERROS SEGUIDOS
#[201,500,502,201,500] => LISTA_REQ
def erros_seguidos(lista_req):
    for i in range(len(lista_req) - 1):
        codigo_atual = lista_req[i]
        prox_codigo = lista_req[i+1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True

    return False

# print(erros_seguidos(status[1]))

def analisar_endpoint(lista_req):
    qtd_sucessos = 0

    for codigo in lista_req:
        if eh_sucesso(codigo):
            qtd_sucessos += 1

    qtd_req = len(lista_req)
    qtd_erro = qtd_req - qtd_sucessos

    percentual_sucesso = (qtd_sucessos / qtd_req) * 100

    tem_erros_seguidos = erros_seguidos(lista_req)

    if tem_erros_seguidos:
        classificacao = "CRÍTICO"
    elif percentual_sucesso >= 80:
        classificacao = "ESTÁVEL"
    else:
        classificacao = "INSTÁVEL"

    return (
        qtd_sucessos,
        qtd_erro,
        percentual_sucesso,
        classificacao
    )
maior_qtd_erros = -1
endpoint_maior_erro = ""


for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    status_endpoint = status[i]

    sucessos, erros, percentual, classificacao = analisar_endpoint(status_endpoint)

    print(f"Endpoint: {nome_endpoint}")
    print(f"Sucessos: {sucessos}")
    print(f"Erros: {erros}")
    print(f"Percentual de sucesso: {percentual:.1f}%")
    print(f"Classificacção: {classificacao}")
    print("-" * 30)
    print()

    if erros > maior_qtd_erros:
        maior_qtd_erros = erros
        endpoint_maior_erro = nome_endpoint

print(f"Endpoint com maior número de erros é: {endpoint_maior_erro} ({maior_qtd_erros}")