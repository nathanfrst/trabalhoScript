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
                print(diretorios)
                print("Diretórios disponíveis. ")
                nomeDir = str(input("Digite qual dos diretórios acima irá receber o arquivo."))
            elif escolhaArq == "N":
                print("asd")
            else:
                print("asd")
        except ValueError:
            print("Por favor digite uma opção válida (S-N) \n")


def excArq():
    print("C")
                    
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

