# endpoints = ["/login", "/produtos", "/pedidos"]
# status = [
#     [200, 200, 401, 200, 500],
#     [200, 200, 200, 200, 200],
#     [201, 500, 502, 201, 500]
# ]
#
#
# def analisar_api(endpoints, status):
#     endpoint_com_mais_erros = ""
#     maior_qtd_erros = -1
#
#     for i in range(len(endpoints)):
#         nome = endpoints[i]
#         lista_codigos = status[i]
#
#         sucessos = 0
#         erros = 0
#         dois_erros_seguidos = False
#
#         for j in range(len(lista_codigos)):
#             codigo = lista_codigos[j]
#
#             if 200 <= codigo <= 299:
#                 sucessos += 1
#             else:
#                 erros += 1
#
#             if j > 0:
#                 if status[i][j - 1] > 299 and codigo > 299:
#                     dois_erros_seguidos = True
#
#         porcentagem = (sucessos / len(lista_codigos)) * 100
#
#         if dois_erros_seguidos:
#             classificacao = "CRÍTICO"
#         elif porcentagem >= 80:
#             classificacao = "ESTÁVEL"
#         else:
#             classificacao = "INSTÁVEL"
#
#         if erros > maior_qtd_erros:
#             maior_qtd_erros = erros
#             endpoint_com_mais_erros = nome
#
#         print(f"Endpoint: {nome}")
#         print(f"  - Taxa de Sucesso: {porcentagem:.0f}%")
#         print(f"  - Erros seguidos: {'Sim' if dois_erros_seguidos else 'Não'}")
#         print(f"  - Status: {classificacao}\n")
#
#     print(f"--> Endpoint com mais erros: {endpoint_com_mais_erros}")
#
#
# analisar_api(endpoints, status)

endpoints = ["/login", "/produtos", "/pedidos"]
status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]

# print(endpoints[0])
# print(status[0])

# def eh_sucesso(lista_codigos):
#     sucessos = 0
#     for codigo in lista_codigos:
#         if 200 <= codigo <= 299:
#             sucessos += 1
#     return sucessos
#
# print(eh_sucesso(status[0]))

def eh_sucesso(codigo):
    return 200 <= codigo <= 299

for lista_de_codigos in status:
    for codigo in lista_de_codigos:
        print(codigo, eh_sucesso(codigo))