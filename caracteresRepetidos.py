## Devuelve un diccionario con las repeticiones de cada caracter de un palabra dada.
## TODO : Optimizar para que las claves solo sean las de las letras de la palabra.
import operator
import string
def repeticionesDeCaracter(palabra):
    repeticiones = {}
    alfabeto = list(string.ascii_uppercase)
    for letra in alfabeto:
        repeticiones[letra] = 0
    for letra in palabra:
        if letra in palabra:
            repeticiones[letra] += 1
    return repeticiones

def puntajeMaximo(palabra):
    puntaje = 0
    repeticionesOrdenadas =dict(sorted(repeticionesDeCaracter(palabra).items(),key=operator.itemgetter(1),reverse=True))
    print(repeticionesOrdenadas)
    print("¨¨¨")
    for posicion,letra in enumerate(repeticionesOrdenadas):
       puntaje += repeticionesOrdenadas[letra]*(26-posicion)

    return puntaje
def main():
    palabra = input('Ingrese palabra: ')
    print(puntajeMaximo(palabra))    

main()