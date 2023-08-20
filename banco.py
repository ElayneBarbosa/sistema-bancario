operação=-1
saldo = 0
limite = 500
extrato = ""
n_saques = 0
limite_saques = 3


while operação != 4:
    operação = int(input("Qual operação você deseja realizar: \n[1]depósito \n[2]saque \n[3]extrato \n[4]sair \n:"))
    if operação == 1:
        valor = float(input("Informe o valor para depósito "))
        if valor >= 0:
            saldo += valor
            print("O saldo atual é: ", saldo)  
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else: 
            print("Digite um número maior que 0") 
    elif operação == 2:
        excedeu_saques = n_saques >= limite_saques
        valor = float(input("Informe o valor do saque "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        
        if excedeu_saldo:
            print("Você não possui saldo suficiente para realizar a operação")
        elif excedeu_limite:
            print("Você não possui mais limite para realizar a operação")
        elif excedeu_saques:
            print("Você realizou todos os saques possíveis")

        elif valor <=  saldo:
            valor >= 0
            saldo -= valor
            print("O saldo atual é: ", saldo)
            extrato += f"Saque: R$ {valor:.2f}\n"
            n_saques += 1
        else:
            valor < 0
            print("Digite valores positivos")
    elif operação == 3: 
        print("\nEXTRATO BANCÁRIO \n")
        print("Não foram realizadas movimentações.\n" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}\n")
        input("Pressione [enter] para continuar")

    elif operação == 4:
        print("Você solicitou o encerramento das operações.")
    else:
        print("Opção invalida, selecione a operação desejada")

print(f"Seu saldo é {saldo}. Obrigada por utilizar nossos serviços!")