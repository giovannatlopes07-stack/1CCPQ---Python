from model import model_lead
import control

def add_lead():
    name = input('Nome:')
    email = input('E-mail:')
    stage = input('Etapa no funil:')

    # valida os dados aqui!!
    # depois de validado, precisamos modelar o lead com um dict
    # para isso, usamos o model
    print(model_lead(name,email,stage))

    # agora...com o meu lead modelado com um dict...
    # precisamos enviar esse lead para leads.json
    # para isso, vamos usar o control
    control.create_lead(model_lead(name,email,stage))

    print('Lead adicionado (func)')

def list_leads():
    leads = control.read_leads()
    print(leads)

# +1 desafio: formatar como tabela

def main():
    while True:
        print('/nMini CRM de Leads')
        print('[1] Adicionar lead')
        print('[2] Listar leads')
        print('[0] Sair do progrma')

        opt = input('Escolha uma opções')

        if opt == '1':
            add_lead()
        elif opt == '2':
            list_leads()
        elif opt == '0':
            print('Até mais...')
            break
        else:
            print('Opções inválida')


if __name__ == '__main__':
    main()