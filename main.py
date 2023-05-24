from src.Logica.OperacionesEnteros import OperacionesEnteros

if __name__ == '__main__':
    cantidadNumeros = int(input("Ingrese la Cantidad de números: "))
    numeros = []
    for i in range(cantidadNumeros):
        print(f"Ingrese Número {i+1:2}: ", end="", flush=True)
        numeros.append(int(input("")))

    print(f"Números Ingresados = {numeros}")
    operacionesEnteros = OperacionesEnteros(numeros)
    print(f"El MCD es = {operacionesEnteros.calcularMCD()}")
