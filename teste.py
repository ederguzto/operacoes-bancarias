lista = []
menu = "[t] Cadastrar [x]  Excluir [e] Exibir: "

opcao = input(f'{menu}')
while True:
    if opcao.lower() == "t":
        lista.append(('c', input("Cadastro nome: ")))
        opcao = input(f'{menu}')
    if opcao.lower() == "x":
        lista.append(('e', input("Excluir: ")))
        opcao = input(f'{menu}')
    if opcao.lower() == "e":
        for a in lista:
            print({a})
        opcao = input(f'{menu}')

## #################################################

dia = str(input("TEste: ")).lower()

match dia:
    case "t":
        print("teste")
    case "e":
        print("teste")        

        