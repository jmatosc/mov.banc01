import textwrap 
import datetime

def exibir_extrato (saldo,/,*,extrato):
    print("\n===================== EXTRATO =======================")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\n Saldo:\t\t R${saldo:.2f}")
    print("________________________________________________________")
def menu ():
    menu = """\n 
    ========================== MENU =======================
    [D]\t Depositar
    [S]\t Saque
    [E]\t Extrato 
    [NC]\t Nova Conta
    [LC]\t Listar contas
    [NU]\t Novo usuário
    [Q]\t Sair
    """
    return input(textwrap.dedent(menu))

def depositar(saldo,valor,extrato,/): 
    if valor > 0:
        saldo +=valor
        data_deposito = datetime.datetime.now() 
        data_deposito = data_deposito.strftime("%d-%m-%Y")
        extrato += f"Deposito\n Data: {data_deposito} \n Valor do Deposito: R$ {valor:.2f}\n"
    else:
        print("\n Valor informado invalido")
    return saldo, extrato
def saque(*,saldo,valor,extrato,limite,total,limite_saque):
    if valor > limite :
        print("Valor de saque excedido")
    elif valor > saldo:
        print (f"Saldo insuficiente, seu saldo atual é de: R$ {saldo:.2f}")
    elif valor <= 0:
        print("Transação invalida")
    elif total > limite_saque:
        print('Limite de saque diário atigido')
    else:
        saldo -= valor
        total += 1
        data_saque = datetime.datetime.now() 
        data_saque = data_saque.strftime("%d-%m-%Y")
        extrato += f"Saque\n Data: {data_saque} \n Valor do Saque: R$ {valor:.2f}\n"
    return saldo, extrato
def criar_usuario(usuarios):
    cpf = input("Informe seu número de CPF(apenas números): ")
    usuario = filtrar_usuario(cpf,usuarios)
    if usuario:
        print("\n Usuário já existente")
        return 
    nome = input("Informe o seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento:")
    endereco = input("Informe seu endereço: ")
    usuarios.append({"nome":nome,"data_nascimento":data_nascimento,"cpf":cpf,"endereco":endereco})

    print("==== Usuário criado com sucesso! ====") 
def criar_conta(agencia, numero_conta,usuarios):
    cpf = input("Informe o CPF do usuário")
    usuario = filtrar_usuario(cpf,usuarios)
    if usuario:
        print ('Conta criada com sucesso')
        return{"agencia":agencia, "numero_conta":numero_conta,"usuario":usuario}
    print("usuario não encontrado")
    return None  

def filtrar_usuario(cpf,usuarios):

    usuarios_filtrados=[usuario for usuario in usuarios if usuario ["cpf"]==cpf]
    return usuarios_filtrados[0]if usuarios_filtrados else None
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta["agencia"]}
            C\C:\t\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
        print(textwrap.dedent(linha))

def main():
    agencia = "0001"
    saldo = float(0)
    total = 0
    extrato = "" 
    limite = 500
    usuarios = []
    contas = []
    limite_saque = 3
    numero_conta = 0
    while True: 
        respcli = menu()

        if respcli == "s" :
            valor = float(input(f"Transação saque selecionada.\nInforme o valor que deseja sacar:"))
         
            if valor > 0:
                valor= float(input("Informe o valor do deposito: "))
                saldo, extrato = saque(
                saldo=saldo,
                valor=valor, 
                extrato=extrato,
                limite=limite, 
                total=total, 
                limite_saque=limite_saque,
                )         
        if respcli == "d" :
            valor = float(input(f"Transação deposito selecionada.\nInforme o valor que deseja depositar:"))
            if valor > 0:
                saldo, extrato = depositar(saldo,valor,extrato)
            else:
                print("Valor invalido ")
        if respcli == "e":
            exibir_extrato (saldo,extrato=extrato)
       
        if respcli == "nu":
            criar_usuario(usuarios)
        if respcli == "nc":
            numero_conta = len (contas) + 1
       
            conta = criar_conta(agencia, numero_conta,usuarios)
            if conta:
                contas.append(conta)
        if respcli == "lc":
            listar_contas(contas)
        elif respcli== "q" :
            print("Atendimento encerrado.")
            break
main()
