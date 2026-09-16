import os
import platform
import psutil
import getpass

print("Diretório atual:", os.getcwd())

def criarDir():
    # Criar um diretório 
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
    # Criar um arquivo 
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
    # Função para excluir um arquivo que o usuário queira 
    while True:
        escolhaExc = str(input("O arquivo está dentro de algum diretório? S-N \n")).upper()

        if escolhaExc == "S": #So a lista dos diretorios que pode usar
            diretorios = []
            for item in os.listdir("."):
                if os.path.isdir(item):
                    diretorios.append(item)

            print(f"\n {diretorios} \n Diretórios disponíveis. ") 
            nomeDir = str(input("\n Digite em qual diretório está o arquivo: "))

            while nomeDir not in diretorios: #Loop caso o usuario queria zoar com minha face
                print("Diretório não encontrado, por favor tente novamente. \n")
                nomeDir = str(input("\n Digite em qual diretório está o arquivo: "))

            arquivos = [] #Arquivos do diretorio escolhido
            for item in os.listdir(nomeDir):
                if os.path.isfile(os.path.join(nomeDir, item)):
                    arquivos.append(item)

            print(f"\n {arquivos} \n Arquivos disponíveis para a exclusão ")
            nomeArq = input("Digite qual arquivo você gostaria de excluir ")
            caminho = os.path.join(nomeDir, nomeArq)

            if nomeArq in arquivos:  #Se já tiver o arquivo, excluir sem pedir permissão
                os.remove(caminho)
                print(f"Arquivo '{nomeArq}' excluído com sucesso.")
            else:
                print("Arquivo não encontrado.")
                break

        elif escolhaExc == "N": #Nome dos arq que tá na pasta atual
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
 
def lerArq():
    # Função para printar na tela algum arquivo que o usuário criar (txt, caso contrário provavelmente não vai funcionar)

    while True:
        arquivos = [
            arquivo
            for arquivo in os.listdir(".")
            if os.path.isfile(arquivo) and arquivo.endswith(".txt")
        ]

        if not arquivos:
            print("Não existem arquivos .txt neste diretório.")
            break
        print("\nArquivos .txt disponíveis:")

        for arquivo in arquivos:
            print(arquivo)

        nomeArquivo = input("\nDigite o nome do arquivo que deseja ler: ")

        if nomeArquivo in arquivos:

            with open(nomeArquivo, "r") as arquivo:
                conteudo = arquivo.read()

            print("\n----- CONTEÚDO DO ARQUIVO -----")
            print(conteudo)
            print("--------------------------------")
            break
        else:
            print("Arquivo não encontrado. Tente novamente.")

def infoComp():
    # Coleta as informações do computador

    ram = psutil.virtual_memory() #Guarda os valores da memoria na variavel "ram"

    informacoes = (
        f"Sistema: {platform.system()}\n"
        f"Versão: {platform.release()}\n"
        f"Usuário: {getpass.getuser()}\n"
        f"Arquitetura: {platform.machine()}\n"
        f"Processador: {platform.processor()}\n"
        f"RAM total: {ram.total}\n"
        f"RAM disponível: {ram.available}\n"
        f"RAM utilizada: {ram.used}\n"
        f"RAM utilizada (%): {ram.percent}\n"
    )

    # Mostra no terminal
    print("\n" + informacoes)

    while True:

        escolhaSO = input("Deseja escrever as informações em algum arquivo .txt? (S-N) " ).upper()
        if escolhaSO == "S":
            arquivoExiste = input("Deseja escrever em um arquivo já existente? (S-N) ").upper()

            if arquivoExiste == "S":
                # Lista somente os arquivos .txt 
                arquivos = [
                    arquivo
                    for arquivo in os.listdir(".")
                    if os.path.isfile(arquivo) and arquivo.endswith(".txt")
                ]

                if not arquivos:
                    print("Não existem arquivos .txt neste diretório.")
                    continue
                print("\nArquivos .txt disponíveis:")
                for arquivo in arquivos:
                    print(arquivo)
                nomeArquivo = input("\nDigite o nome do arquivo que deseja utilizar: ")
                if nomeArquivo in arquivos:
                    with open(nomeArquivo, "w") as arquivo:
                        arquivo.write(informacoes)
                    print(f"Informações transcritas com sucesso em {nomeArquivo}.")
                    break
                else:
                    print("Arquivo não encontrado.")
            elif arquivoExiste == "N":
                nomeArquivo = input("Digite o nome do novo arquivo .txt: " )
                # Garante que o arquivo tenha .txt
                if not nomeArquivo.endswith(".txt"):
                    nomeArquivo += ".txt"
                with open(nomeArquivo, "w") as arquivo:
                    arquivo.write(informacoes)
                print(f"Arquivo '{nomeArquivo}' criado com sucesso e as informações foram transcritas.")
                break
            else:
                print("Por favor digite uma resposta válida (S-N).")
        elif escolhaSO == "N":
            print("Usuário escolheu não transcrever.")
            break
        else:
            print("Por favor digite uma resposta válida (S-N).")
                  
while True: #Menu principal do programa
    try: 
        escolhaMenu = int(input("\n Bem vindo, o que deseja fazer? \n 1- Criar diretório \n 2- Criar um arquivo \n 3- Excluir Arquivo \n 4- Ler arquivo \n 5- Informações do SO \n 6- Sair \n -"))
        
        match escolhaMenu:
            case 1:
                criarDir()
            case 2:
                criarArq()
            case 3:
                excArq()
            case 4:
                lerArq()
            case 5:
                infoComp()
            case 6:
                print("Programa finalizado.")
                break
            case _:
                print("Por favor digite uma opção válida (1-6) \n")
    except ValueError:
        print("Por favor digite uma opção válida (1-6)\n")

