#funções
def read_text(l: int):
    '''Leitura das linhas do texto'''
    fulltext = []
    for index in range(l):
        line = str(input('Escreva uma linha de texto: '))
        fulltext.append(line)
    return fulltext


def read_word(n: int):
    '''Leitura das palavras que serão buscadas'''
    allwords = []
    for index2 in range(n):
        word = str(input('Escreva uma palavra para ser buscada no texto: '))
        allwords.append(word)
    return allwords


def format(string: str):
    '''Formatação das strings'''
    string = string.rstrip('.')
    string = string.rstrip(',')
    string = string.rstrip(':')
    string = string.rstrip('!')
    string = string.rstrip('?')
    string = string.rstrip(';')
    string = string.casefold()
    return string


def search_word(txt: str, word: str):
    '''Verifica a ocorrência das palavras dentro do texto'''
    occurrences = 0
    txt = format(txt)
    word = format(word)
    txt = txt.rsplit()
    for index3 in range(len(txt)):
        if word == txt[index3]:
            occurrences += 1
    return occurrences


def search_similar_word(txt: str, word: str):
    '''Verifica a ocorrência de palavras similares no texto'''
    txt = format(txt)
    word = format(word)
    if (word in txt) == True:
        similar_occurrences = txt.count(word)
    else:
        similar_occurrences = 0
    return similar_occurrences

#principal

L = int(input('Digite a quantidade de linhas em que o texto está contido: '))
fulltext = read_text(L)

N = int(input('Digite quantas palavras serão buscadas no texto: '))
allwords = read_word(N)

for word in allwords:
    occurrences = 0
    similar = 0
    for line in fulltext:
        occurrences += search_word(line, word)
        similar += search_similar_word(line, word)
    print(f'Palavra buscada: {word}')
    print(f'Ocorrência(s): {occurrences}')
    print(f'Palavras similares: {similar - occurrences}')
