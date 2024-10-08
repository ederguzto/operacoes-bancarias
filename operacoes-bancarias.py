menu = ""

saldo = 0

deposito = 0
entrada = 0

saque = 0
saida = 0

SAQUE_DIARIO = 3

print(f'''
    ------- MENU ------
    [e] - Extrato
    [d] - Depostiar
    [s] - Sacar
    [q] - Sair
    -------------------
    ''')

opcao = input(f'''    Digite uma opção: {menu}''')
while True:

    if opcao == "e":
        print(f'''
    -- MOVIMENTAÇÕES --
    Entradas: R${entrada}
    Saídas: R${saida}
    Saldo: R${saldo}
    -------------------
    [e] - Extrato
    [d] - Depostiar
    [s] - Sacar
    [q] - Sair
    ''')
        opcao = input(f'''    Digite uma opção: {menu}''')
        
    if opcao == "d":
        
        deposito = float(input(f'''
    ----- DEPÓSITO -----
    
    Digite o valor de depósito: '''))
        if deposito != 0 and deposito > 0:
            entrada += deposito
            saldo += deposito
            print(f'''
    Você depositou R${deposito}

    --------------------
    [e] - Extrato
    [d] - Depostiar
    [s] - Sacar
    [q] - Sair
    ''')
        else:
            print('''   #### ERRO ###   ''')
        
        opcao = input(f'''    Digite uma opção: {menu}''')

    if opcao == "s":
        
        saque = float(input(f'''
    ------- SACAR -------
    
    Digite o valor de saque: '''))
        if saque != 0 and saque > 0:
            saida -= saque
            saldo -= saque
            print(f'''
    Você sacou R${saque}

    ---------------------
    [e] - Extrato
    [d] - Depostiar
    [s] - Sacar
    [q] - Sair
    ''')
        else:
            print('''   #### ERRO ###   ''')
        
        opcao = input(f'''    Digite uma opção: {menu}''')
    
    if opcao == "q":
        break