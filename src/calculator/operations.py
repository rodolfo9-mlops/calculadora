def sumar(a: float, b: float) -> float:
    """
    Args:
      a:float:
      b:float:

    Returns:float:

    """
    return a + b

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