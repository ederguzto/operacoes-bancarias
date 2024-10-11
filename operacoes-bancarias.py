tela = (f'''\n    ------- MENU ------\n    [e] - Extrato\n    [d] - Depostiar\n    [s] - Sacar\n    [q] - Sair''')

transacoes = []
deposito = 0
saque = 0
entrada = 0
saida = 0
saldo = 0
SAQUE_DIARIO = 3




while True:
    print(f'''{tela}    \n''')
    opcao = input(f'''    Digite uma operação: ''').lower()
    match opcao:
        case 't':
            print(f'''  \nVocê cancelou a operação anterior!
        {tela}''')    
            opcao = input(f'''    Digite uma operação: ''').lower()

        case 'e':
            print(f'''\n    ----- EXTRATO -----''')
            for transacao in transacoes:
                tipo, valor = transacao
                if tipo == 'd':
                    
                    print(f'    Entrada: R${valor:.2f}')
                elif tipo == 's':
                    print(f'    Saída: R${valor:.2f}')
                else:
                    print(f'Sem transações')
            print(f'    Saldo atual: {saldo}')

        case 'd':
            deposito = input(f'''\n    ---- DEPOSITAR ----\n    Digite o valor de depósito: ''')
            if float(deposito) > 0:
                transacoes.append (('d', (float(deposito))))
                entrada += float(deposito)
                saldo += float(deposito)
                print(f'''    Você depositou R${deposito}''')
            
            else:
                deposito = input('''    Digite um valor válido: ''')

        case 's':
            saque = float(input(f'''\n    ------ SACAR ------\n    Digite o valor de saque ou [t] para cancelar: '''))
            if SAQUE_DIARIO != 0 and saldo != 0: # posso usar len() pra ver quantos tipo 's' tem na variavel transacoes e se = 3 ele nao deixa realizar o saque
                saida += saque
                saldo -= saque
                SAQUE_DIARIO -= 1
                transacoes.append (('s', float(saque)))
                print(f'''    Você sacou R${saque}''')
            elif saque > saldo:
                print('''    Saldo insuficiente''')
            else:
                print('''    Limite de saque diário atingido!''')

        case 'q':
            break

        case _:
            opcao = input(f'''    {tela}\n    Digite uma operação válida: ''').lower()