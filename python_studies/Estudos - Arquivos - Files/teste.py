
# primeiro parametro o nome do arquivos, segundo parametro o modo de abertura

# r - read
# w - write (apaga o conteudo se já existir)
# a - weite (não apaga o conteudo se já existir)
# b - binary
# combinação de modos são válidas ('w+b')


# se o arquivo não existir, cria-se um novo


#FOMAR NORMAL
#-------------------------------------
#arq = open('arquivo.txt', 'w')
##arq.write('data science')
#
#texto = '''
#	Para aprender data science
#	Você tem que começar do zero
#	Aprender Python é muito importante
#'''
#arq.write(texto)
#arq.close()


# FORMA PYTHONICA
#--------------------------------------
"""
#ESCREVER DADOS

texto = '''
	Para aprender data science
	Você tem que começar do zero
	Aprender Python é muito importante
'''

with open('arquivo.txt', 'w') as f:
	f.write(texto)

"""

#CONSUMIR DADOS

with open('dataset.txt', 'r') as arq:
	lista = arq.read().splitlines()

print(len(lista))
print(lista[4]);	