import os
 
 
def excluir_arquivo(nome_arquivo):
    os.remove(nome_arquivo)
    print(f"Arquivo '{nome_arquivo}' excluído com sucesso.")
 
 
if __name__ == "__main__":
    excluir_arquivo("teste.txt")
 