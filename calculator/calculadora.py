
from calculator.operations import sumar, restar, multiplicar, dividir,potencia,raiz_cuad


def calculadora():
    """ """
    print("1 Suma")
    print("2 Resta")
    print("3 Multiplicacion")
    print("4 Division")
    print("5 Potencia")
    print("6 Raiz Cuadrada")

    opcion=input("Elige la operacion ")
    
    num1 = float(input("Ingresa el primer numero: "))
    if opcion !="6":
        num2 = float(input("Ingresa el segundo numero: "))
    
    if opcion == "1":
        print("Resultado: ",sumar(num1,num2))
    elif opcion == "2":
        print("Resultado: ",restar(num1,num2))
    elif opcion == "3":
        print("Resultado: ",multiplicar(num1,num2))
    elif opcion == "4":
        print("Resultado: ",dividir(num1,num2))
    elif opcion == "5":
        print("Resultado: ",potencia(num1,num2))
    elif opcion == "6":
        print("Resultado: ",raiz_cuad(num1))

if __name__ == "__main__":
    calculadora()