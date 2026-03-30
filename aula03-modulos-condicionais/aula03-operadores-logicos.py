# LÓGICA E (and)

verifica_email = True
verifica_senha = False

verifica_login = verifica_email and verifica_senha
print(verifica_login)

if verifica_login:
    print("Entrar no programa!")

# LÓGOCA OU (or)

logica_ou = False or False or True
print(logica_ou)

# OPERADOR DE NEGAÇÃO
negacao = not False
print(negacao)

if not verifica_login:
    print("Loga certo ai...")