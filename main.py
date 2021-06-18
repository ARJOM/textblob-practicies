from textblob import TextBlob


def analise_de_sentimento(frase):
    analise = TextBlob(frase)

    # frases em português tem polaridade e subjetividade 0
    if analise.sentiment.polarity == 0 and analise.sentiment.subjectivity == 0:
        # traduzimos a frase para inglês
        analise = analise.translate(to="en")

    print(50*"-")
    if analise.sentiment.polarity < 0:
        resultado = "negativa"
    elif analise.sentiment.polarity > 0:
        resultado = "positiva"

    print(frase)
    print(f"De maneira geral, a frase acima foi definida como {resultado}")

if __name__ == '__main__':
    analise_de_sentimento("I'm kinda sick today")
    analise_de_sentimento("Hello everyone, nice to meet you all")
    analise_de_sentimento("Que ódio eu tenho de você")
