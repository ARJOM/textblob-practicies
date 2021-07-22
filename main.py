from textblob import TextBlob


def analise_de_sentimento(frase, opcao):
    analise = TextBlob(frase)

    if analise.sentiment.polarity <= 0:
        resultado = 'negativa'
    else:
        resultado = "positiva"

    if resultado == opcao:
        return 1
    return 0


if __name__ == '__main__':
    with open("negativo.txt", "r") as arquivo:
        linhas = arquivo.read().split('\n')
        total = len(linhas)
        count_neg = 0
        for linha in linhas:
            count_neg += analise_de_sentimento(linha, 'negativa')
        print(f"{(count_neg/total)*100}% das amostras foram classificadas, corretamente, como negativas")

    with open("positivo.txt", "r") as arquivo:
        linhas = arquivo.read().split('\n')
        total = len(linhas)
        count_pos = 0
        for linha in linhas:
            count_pos += analise_de_sentimento(linha, 'positiva')
        print(f"{(count_pos/total)*100}% das amostras foram classificadas, corretamente, como positivas")
