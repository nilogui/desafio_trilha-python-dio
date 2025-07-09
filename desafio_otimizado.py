menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuário
[c] Criar Conta Corrente
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
lista_usuarios = []
lista_contas_correntes = []
AGENCIA = "0001"
numero_da_conta = 0

# def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
#     print(modelo, ano, placa, marca, motor, combustivel)

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def funcao_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(lista_usuarios):
    nome_usuario = str(input("Informe o nome do usuário: "))
    data_nascimento = str(input("Informe a data de nascimento do usuário: "))
    cpf = str(input("Informe o cpf do usuário: "))
    cpf_numeros = ''.join([c for c in cpf if c.isdigit()])
    cpf = cpf_numeros
    endereco = str(input("Informe o endereço do usuário (logradouro, nro - bairro - cidade/sigla estado): "))
    usuario = dict(nome_usuario = nome_usuario, data_nascimento = data_nascimento, cpf = cpf, endereco = endereco)
    novo_cpf = True
    if lista_usuarios != []:
        for user in lista_usuarios:
            if user["cpf"] == cpf:
                novo_cpf = False
    if novo_cpf:
        lista_usuarios.append(usuario)
        print("Usuário Criado!")
    else:
        print("Usuário já cadastrado!")
    # print(lista_usuarios)

def criar_conta_corrente(AGENCIA, numero_da_conta, lista_usuarios, lista_contas_correntes):
    cpf = str(input("Informe o cpf do usuário: "))
    encontrou_cpf = False
    if lista_usuarios != []:
        for user in lista_usuarios:
            if user["cpf"] == cpf:
                encontrou_cpf = True
                usuario_encontrado = user
    if encontrou_cpf:
        numero_da_conta += 1
        conta_corrente = dict(agencia = AGENCIA, numero_da_conta = numero_da_conta, usuario = usuario_encontrado)
        lista_contas_correntes.append(conta_corrente)
        print("Conta Criada!")
    else:
        print("Usuário inexistente!")
    # print(lista_contas_correntes)

    return numero_da_conta

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
        funcao_extrato(saldo, extrato=extrato)

    elif opcao == "u":
        criar_usuario(lista_usuarios)

    elif opcao == "c":
        numero_da_conta = criar_conta_corrente(AGENCIA, numero_da_conta, lista_usuarios, lista_contas_correntes)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
