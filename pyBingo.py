#!-*- coding: utf-8 -*-
import random
import sys

def gera_cartela(palavras, template, filename):
    palavras = open(palavras, 'r').readlines()
    cartela = open(template, 'r').read()

    linha = "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td></tr>"
    linhas = []
    conteudo_final = ""

    # Cada cartela possui cinco linhas com 25 palavras
    # TODO: colocar nome do projeto na posio central da cartela
    for i in range(0, 5):
        random.shuffle(palavras)
        linhas.append(linha.format(palavras[-1], palavras[-2], palavras[-3], palavras[-4], palavras[-5]))
        palavras = palavras[0:-5]

    for linha in linhas:
        conteudo_final = conteudo_final + linha

    cartela = cartela.format(conteudo_final)
    open(filename, 'w').write(cartela)


def main(argv=None):
    """Gera uma Cartela de Bingo no formato PDF

    Utilizao:
    pyBingo.py lista_de_palavras template_cartela arquivo_saida       
    """
    if argv is None:
        argv = sys.argv

    # TODO:
    # - Fazer validao dos argumentos
    # - Criar pacote para a funo que gera a cartela
    # - Criar interface grfica
    # - ...
    
    gera_cartela(argv[1], argv[2], argv[3])

if __name__ == "__main__":
    sys.exit(main())

