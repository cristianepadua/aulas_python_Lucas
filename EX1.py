# dados 5 usuarios
# nome, idade, cpf
# banco que tem conta
# saldo
# soma do saldo das contas
# dividir por 5
# if e esle para saber se é milhionario, rico, bem de vida, classe media, pobre

def banco_dados():
    nome_cliente = []
    idade_cliente = []
    cpf_cliente = []
    banco_cliente = []
    saldo_cliente = []
    for i in range (1,6):
        nome_cliente.append(input(f"Digite o nome do {i}º cliente: "))
        idade_cliente.append(int(input(f"Digite a idade do {i}º cliente: ")))
        cpf_cliente.append(input(f"Digite o CPF do {i}º cliente: "))
        banco_cliente.append(int(input(f"Digite o banco do {i}º cliente: ")))
        saldo_cliente.append(int(input(f"Digite o saldo do {i}º cliente: ")))
        print("+"*50)
    return(nome_cliente,idade_cliente,cpf_cliente,banco_cliente,saldo_cliente)

def situacao_cliente(cliente,valor):
    if valor <= 1412:
        print(f"O cliente {cliente} é probre!")
    elif valor > 1413 and valor <= 3000:
        print(f"O cliente {cliente} é da classe média!")
    elif valor > 3001 and valor <= 5000:
        print(f"O cliente {cliente} é bem de vida!")
    elif valor > 5001 and valor <= 1000000:
        print(f"O cliente {cliente} é rico!")
    elif valor > 1000000:
        print(f"O cliente {cliente} é milhionário!")
    else:
        print("*** erro na informação ***")
    return None

nomes,idades,cpfs,bancos,saldos = banco_dados()
media = sum(saldos)/5
print(f"A média de saldo em conta bancária dos clientes informados é: R$ {media}\n")
print("A partir dos dados indicados, podemos inferir que: \n")
for i in range (0,5):
    situacao_cliente(nomes[i],saldos[i])
print("\n*** END ***")




