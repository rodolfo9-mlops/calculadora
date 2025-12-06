import math

def multiplicar(a: float, b: float ) -> float:
    """
    Args:
      a:float:
      b:float:

    Returns:float:

    """
    return a * b

def sumar(a: float, b: float) -> float:
    """
    Args:
      a:float:
      b:float:

    Returns:float:

    """
    return a + b

def potencia(a: float, b: float) -> float:
    """
    Args:
      a:float:
      b:float:

    Returns:float:

    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Tanto a como b deben ser enteros o flotantes")
    if a == 0 and b < 0:
        raise ZeroDivisionError("0 no puede ser elevado a ningún exponente negativo")
    if a < 0 and not float(b).is_integer():
        raise ValueError("Ningún número negativo puede elevarse a una potencia no entera (para esta calculadora de reales)")

    try:
        result = a ** b
    except OverflowError:
        raise OverflowError("El resultado es muy largo para ser represntado")
    except Exception as e:
        raise RuntimeError(f"Error al computar {a} ** {b}: {e}")

    return result


def decorador(func):
    """
    Args:
      func: 

    Returns:float:
    """
    def inner(a, b):
        """
        Args:
          a:
          b:
        Returns:float:
        """
        if b == 0:
            raise ValueError("No es posible dividir por 0")
        else:
            return func(a,b)    
    return inner
        
@decorador
def dividir(a:float, b:float) -> float:
    """
    Args:
      a:float:
      b:float:

    Returns:float:

    """    
    return a / b

def raiz_cuad(a:float)->float:
    """
    Args:
      a:float:

    Returns:float:

    """    

    if a is None:
        raise TypeError("El input no puede ser nulo")

    if not isinstance(a, (int, float)):
        raise TypeError("El input debe ser entero o flotante")

    if math.isnan(a):
        raise ValueError("El input no puede ser NaN")

    if a < 0:
        raise ValueError("No es posible calcular la raiz cuadrada de un negativo")

    # Case 5: All good
    return math.sqrt(a)

def restar(a: float, b: float ) -> float:
    """
    Args:
      a:float:
      b:float:

    Returns:float:

    """
    return a - b

if __name__ == "__main__":
   print(
      "------ Pruebas unitarias ------ \n",
      f"suma 1 + 2: {sumar(1, 2)} \n", 
      f"resta 1 - 2: {restar(1, 2)} \n", 
      f"multiplicar 1 * 2 : {multiplicar(1, 2)} \n",   
      f"dividir 1 + 2: {dividir(1, 2)}\n",
      "dividir 1 / 0: \n"
   ) 
   dividir(1, 0)