import os

def criarDir():
    criado = False
    while not criado: 
    
        nomeDir = str(input("Como deverá se chamar o seu diretório \n"))
        try:
            os.mkdir(nomeDir)
            print(f"Diretório '{nomeDir}' criado com sucesso ")
            criado = True
        except FileExistsError:
            print("Já existe um diretório com esse nome, por favor tente novamente. \n")

def criarArq():
    while True: 
        try: 
            escolhaArq = str(input("Deseja criar este arquivo dentro de algum diretório já existente? S-N \n")).upper()

            if escolhaArq == "S":
                diretorios = []
                for item in os.listdir("."):
                    if os.path.isdir(item):
                        diretorios.append(item)

                print(f"\n {diretorios} \n Diretórios disponíveis. ")
                nomeDir = str(input("Digite qual dos diretórios acima irá receber o arquivo."))

                if nomeDir in diretorios:
                    nomeArq = input("\n Digite o nome do arquivo ")
                    caminho = os.path.join(nomeDir, nomeArq)
                    with open(caminho, "w") as arquivo:
                        print(f"Arquivo '{nomeArq}',criado com sucesso dentro do diretório '{nomeDir}'")
                        break
                else:
                    print("Diretório não existe")

            elif escolhaArq == "N":
                nomeArq = input("\n Digite o nome do arquivo ")
                caminho = os.path.join(nomeArq)
                with open(caminho, "w") as arquivo:
                    print(f"\n Arquivo '{nomeArq}',criado com sucesso.")
                    break
            else:
                print("Ocorreu um erro tente novamente.")

        except ValueError:
            print("Por favor digite uma opção válida (S-N) \n")


def excArq():
    while True:
        try: #loopzin cachorro
            escolhaExc = str(input("O arquivo está dentro de algum diretório? S-N \n")).upper()
 
            if escolhaExc == "S": #so a lista dos diretorios que ta podendo usar
                diretorios = []
                for item in os.listdir("."):
                    if os.path.isdir(item):
                        diretorios.append(item)
 
                print(f"\n {diretorios} \n Diretórios disponíveis. ") 
                nomeDir = str(input("\n Digite em qual diretório está o arquivo: "))
 
                while nomeDir not in diretorios: #loop caso o usuario queria zoar com minha face
                    print("Diretório não encontrado, por favor tente novamente. \n")
                    nomeDir = str(input("\n Digite em qual diretório está o arquivo: "))
 
                arquivos = [] #arquivos do diretorio q escolheu
                for item in os.listdir(nomeDir):
                    if os.path.isfile(os.path.join(nomeDir, item)):
                        arquivos.append(item)
 
                print(f"\n {arquivos} \n Arquivos disponíveis para a exclusão ")
                nomeArq = input("Digite qual arquivo você gostaria de excluir ")
                caminho = os.path.join(nomeDir, nomeArq)
 
                if nomeArq in arquivos:  #se ja tiver o arquivo, excluir sem pedir permissao
                    os.remove(caminho)
                    print(f"Arquivo '{nomeArq}' excluído com sucesso.")
                else:
                    print("Arquivo não encontrado.")
                break
 
            elif escolhaExc == "N": #nome dos arq q ta na pasta atual
                arquivos = []
                for item in os.listdir("."):
                    if os.path.isfile(item):
                        arquivos.append(item)
 
                print(f"\n {arquivos} \n Arquivos disponíveis para a exclusão ")
                nomeArq = input("Digite qual arquivo você gostaria de excluir ")
 
                if nomeArq in arquivos:
                    os.remove(nomeArq)
                    print(f"Arquivo '{nomeArq}' excluído com sucesso.")
                else:
                    print("Arquivo não encontrado.")
                break
            else:
                print("Ocorreu um erro tente novamente.")
 
        except ValueError:
            print("Por favor digite uma opção válida (S-N) \n")

def lerArq():
    print(".")
                    
while True: 
    try: 
        escolhaMenu = int(input("Bem vindo, o que deseja fazer? \n 1- Criar diretório \n 2- Criar um arquivo \n 3- Excluir Arquivo \n 4- Ler arquivo \n 5- Sair \n"))
        
        match escolhaMenu:
            case 1:
                criarDir()
            case 2:
                criarArq()
            case 3:
                excArq()
            case 4:
                print("D")
            case 5:
                print("Programa finalizado.")
                break
            case _:
                print("Por favor digite uma opção válida (1-5) \n")
    except ValueError:
        print("Por favor digite uma opção válida (1-5)\n")

