#ANALIZADOR BASICO DE SENTIMIENTOS
from textblob import TextBlob 

class AnalizadorSentimientos:
    def analizar_sentimiento(self, texto):
        analisis = TextBlob(texto)
        if analisis.sentiment.polarity > 0:
            return "Positive"
        elif analisis.sentiment.polarity == 0:
            return "Neutral"
        else:
            return "Negative"
        
        
analizador = AnalizadorSentimientos()
resultado = analizador.analizar_sentimiento("this is so tired but if i doit maybe can be the best programmer of the world")
print(resultado)