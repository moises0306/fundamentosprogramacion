#crear una funcion contar_ocurrencias(palabras) que resiva una lista de palabras y retorne un diccionario con el conteo de cada uno


def contar_ocurrencias(palabras):

    conteo= {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0)+1
    
    return conteo


def main():

    lista_palabras = ["hola", "uno", "dos", "hola"]
    resultado = contar_ocurrencias(lista_palabras)

    print(resultado)

if __name__=="__main__":
    main()