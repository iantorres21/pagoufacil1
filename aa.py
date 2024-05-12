from flask import Flask, render_template, request
import pandas as pd

def buscar_cliente(nome_arquivo, termo_busca):
    try:
        # Carregar o arquivo Excel
        df = pd.read_excel(nome_arquivo)

        # Converter o termo de busca para minúsculas
        termo_busca = termo_busca.lower()

        # Filtrar os clientes cujo nome contenha o termo de busca
        encontrados = df[df['Nome'].str.lower().str.contains(termo_busca)]

        if len(encontrados) > 0:
            print("Informações dos Clientes:")
            for index, cliente in encontrados.iterrows():
                print(cliente)
        else:
            print("Cliente não encontrado.")

    except Exception as e:
        print("Ocorreu um erro:", e)

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo Excel: ")
    termo_busca = input("Digite o termo de busca: ")
    buscar_cliente(nome_arquivo, termo_busca)


