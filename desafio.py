import textwrap

def menu():
    menu = """
    ****************************MENU********************************
    D - DEPOSITAR
    S - SACAR
    E - EXIBIR EXTRATO
    CU - CRIAR USUARIO
    CC - CRIAR CONTA
    LU - LISTAR USUARIOS
    FC - FILTRAR CONTA
    Q - SAIR
    _ _ _ _ """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depositado:\tR$ {valor:.2f}\n"
        print("Depositado com sucesso!")
    else:
        print("Valor inválido")

    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    over_budget = valor > saldo
    over_limit = valor > limite
    over_withdraw = numero_saques >= limite_saques

    if over_budget:
        print("Você não pode sacar, saldo excedido")
    elif over_limit:
        print("Você não pode sacar, saque limite excedido")
    elif over_withdraw:
        print("Você não pode sacar, quantidade de saque excedida")
    elif valor > 0:
        saldo -= valor
        extrato += f"Sacado:\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Você não pode sacar, valor inválido")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print(f"Saldo: R$ {saldo:.2f}")
    print(extrato)

def criar_usuario(usuarios):
    cpf = input("CPF (somente números): ")
    usuario = filtrar_usuario(cpf=cpf, usuarios=usuarios)
    if usuario:
        print("Usuário já existe")
        return 
    nome = input("Nome: ")
    data_nascimento = input("Data Nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla do estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("CPF (somente números): ")
    usuario = filtrar_usuario(cpf=cpf, usuarios=usuarios)
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("Usuário não encontrado. Conta não criada.")
        return None

def filtrar_usuario(*, cpf, usuarios):
    filtered = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return filtered[0] if filtered else None

def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        option = menu().strip().lower()

        if option == "d":
            valor = float(input("Quanto você deseja depositar? "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif option == "s":
            valor = float(input("Valor de saque? "))
            saldo, extrato = sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)

        elif option == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif option == "cu":
            criar_usuario(usuarios)

        elif option == "cc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif option == "lu":
            for usuario in usuarios:
                print(usuario)

        elif option == "fc":
            cpf = input("CPF (somente números): ")
            usuario = filtrar_usuario(cpf=cpf, usuarios=usuarios)
            if usuario:
                contas_usuario = [conta for conta in contas if conta["usuario"]["cpf"] == cpf]
                for conta in contas_usuario:
                    print(conta)
            else:
                print("Usuário não encontrado.")

        elif option == "q":
            print(f"Seu saldo é de R$ {saldo:.2f}")
            print(extrato)
            break

if __name__ == "__main__":
    main()
