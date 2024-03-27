#código para receber Nome, Cor, Sexo, Tamanho, Peso, Cidade, Idioma, Completo
#pergunta qual variável quer saber e se quer saber mais algo e encerra o while se vier o não
teste = 'cris'
#print(teste.upper()) as built-in function need to go with 2 parenthesis on the end!

nome = str(input('Digite seu nome: '))
cor = str(input('Digite qual é a cor que você se auto declara: '))
sexo = str(input('Digite qual é o sexo que você mais se identifica: '))
altura = float(input('Digite a sua altura em m: '))
peso = float(input('Digite seu peso em kg: '))
cidade = str(input('Digite a cidade de nascimento: '))
idioma = str(input('Digite seu idioma principal: '))

cond = 'S'

while cond == 'S' or cond == 's':
    opcao = int(input('Digite qual é o número correspondente a informação que você deseja saber: \n1 - Nome\n2 - cor\n3 - sexo\n4 - tamanho\n5 - peso\n6 - cidade\n7 - idioma\n8 - Completo\n'))
    if opcao == 1:
        print(f'O nome do cliente é {nome.upper()}.')
        cond = input('Digite S se quiser saber mais algum dado e digite N se não quiser saber outro dado (S / N): ')
    elif opcao == 2:
        print(f'A cor do cliente é {cor.upper()}.')
        cond = input('Digite S se quiser saber mais algum dado e digite N se não quiser saber outro dado (S / N): ')
    elif opcao == 3:
        print(f'O sexo que o cliente mais se identifica é o {sexo.upper()}.')
        cond = input('Digite S se quiser saber mais algum dado e digite N se não quiser saber outro dado (S / N): ')
    elif opcao == 4:
        print(f'A altura do cliente é {altura} m.')
        cond = input('Digite S se quiser saber mais algum dado e digite N se não quiser saber outro dado (S / N): ')
    elif opcao == 5:
        print(f'O peso do cliente é {peso} kg.')
        cond = input('Digite S se quiser saber mais algum dado e digite N se não quiser saber outro dado (S / N): ')
    elif opcao == 6:
        print(f'O cliente nasceu na cidade de {cidade.upper()}.')
        cond = input('Digite S se quiser saber mais algum dado e digite N se não quiser saber outro dado (S / N): ')
    elif opcao == 7:
        print(f'O idioma principal do cliente é o {idioma.upper()}.')
        cond = input('Digite S se quiser saber mais algum dado e digite N se não quiser saber outro dado (S / N): ')
    elif opcao == 8:
        print(f'O nome do cliente é {nome.upper()}, sua cor é {cor.upper()}, o sexo que mais se identifica é o {sexo.upper()}, mede {altura} m, pesa {peso} kg, nasceu em {cidade.upper()} e fala o {idioma.upper()} como principal idioma.')
        cond = input('Digite S se quiser saber mais algum dado e digite N se não quiser saber outro dado (S / N): ')
    else:
        print('\n\nDigite uma opção válida, ou seja, digite um número entre 1 e 8.\n\n')
    
              

