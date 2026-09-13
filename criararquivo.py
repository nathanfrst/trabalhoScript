import os

def criar_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, "w")
    arquivo.close()
    print(f"Arquivo '{nome_arquivo}' criado com sucesso.")


if __name__ == "__main__":
    criar_arquivo("teste.txt")