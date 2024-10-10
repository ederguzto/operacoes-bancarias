tela = (f'''
    ------- MENU ------
    [e] - Extrato
    [d] - Depostiar
    [s] - Sacar
    [q] - Sair
    ''')

transacoes = []
deposito = 0
saque = 0
entrada = 0
saida = 0
saldo = 0
SAQUE_DIARIO = 3

print(f'''{tela}
    ''')
opcao = input(f'''    Digite uma operação: ''').lower()

while True:
    match opcao:
        case 't':
            print(f'''
    Você cancelou a operação anterior!
        {tela}
    ''')    
            opcao = input(f'''    Digite uma operação: ''').lower()

        case 'e':
            print(f'''
    ----- EXTRATO -----''')
            for transacao in transacoes:
                tipo, valor = transacao
                if tipo == 'd':
                    
                    print(f'    Entrada: R${valor:.2f}')
                elif tipo == 's':
                    print(f'    Saída: R${valor:.2f}')
                else:
                    print(f'Sem transações')
            print(f'    Saldo atual: {saldo}')
            opcao = input(f'''{tela}
    Digite uma operação: ''').lower()

        case 'd':
            deposito = input(f'''
    ---- DEPOSITAR ----
        
    Digite o valor de depósito: ''')
            if float(deposito) > 0:
                transacoes.append (('d', (float(deposito))))
                entrada += float(deposito)
                saldo += float(deposito)
                opcao = input(f'''
    Você depositou R${deposito}{tela}
    Digite uma operação: ''').lower()
            
            else:
                deposito = input('''
    Digite um valor válido: ''')
            
                opcao = input(f'''    Digite uma operação: ''').lower()

        case 's':
            saque = float(input(f'''
    ------ SACAR ------
        
    Digite o valor de saque ou [t] para cancelar: '''))
            if SAQUE_DIARIO != 0 and saldo != 0: # posso usar len() pra ver quantos tipo 's' tem na variavel transacoes e se = 3 ele nao deixa realizar o saque
                transacoes.append (('s', float(saque)))
                saida += saque
                saldo -= saque
                SAQUE_DIARIO -= 1
                print(f'''
    Você sacou R${saque}''')
                print(tela)
                opcao = input(f'''    
    Digite uma operação: ''').lower()
            elif saque > saldo:
                print('''
    Saldo insuficiente''')
                print(tela)
                opcao = input(f'''    
    Digite uma operação: ''').lower()
            else:
                print('''
    #### Limite de saque diário atingido! ###''')
                print(tela)
            
                opcao = input(f'''    
    Digite uma operação: ''').lower()

        case 'q':
            break

        case _:
            opcao = input(f'''    {tela}
    Digite uma operação válida: ''').lower()