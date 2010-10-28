import random

palavras = open('bingo_dce.txt', 'r').readlines()
cartela = "<center><table border=1>{0}</table></center>"
linha = "<tr><td>{0}</td><td>{1}</td><td>{2}</td></tr>"
linhas = []
conteudo_final = ""
for i in range(0, 3): # Cada cartela possui tres linhas com nove palavras
    random.shuffle(palavras)
    linhas.append(linha.format(palavras[-1], palavras[-2], palavras[-3]))
    palavras = palavras[0:-3]
for linha in linhas:
    conteudo_final = conteudo_final + linha
cartela = cartela.format(conteudo_final)
open('cartela.html', 'w').write(cartela)

