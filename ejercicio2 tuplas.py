#escribir una funcion mayor_y_menor(tuplas_numeros) que recipa una tupla con numeros y retorne el número mayor y menor como tupla


def mayor_y_menor(tupla):
    return (max(tupla), min(tupla))

def main():

    tupla = (7, 8, 3, 9, 8, 10, 1, 4, 6, 2, 100)
    print(tupla)

    resultado = mayor_y_menor(tupla)

    print(f"la suma de la fila es: {resultado}")

if __name__=="__main__":
    main()