import numpy as np

# La clase poly1d() convierte listas de coeficientes (de mayor a menor grado)
# en objetos polinomio con los que podemos hacer operaciones algebraicas

def suma_de_polinomios(a, b):
    # Convertimos las listas en objetos polinomio
    p1 = np.poly1d(a)
    p2 = np.poly1d(b)

    # Sumamos ambos polinomios directamente
    resultado = p1 + p2
    return resultado

# Listas de coeficientes, del término de mayor grado al menor
po1 = [3, 2, 1]  # 3x² + 2x + 1
po2 = [6, 5, 4]  # 6x² + 5x + 4

# Obtenemos el resultado de la suma
resultado = suma_de_polinomios(po1, po2)

# Mostramos el resultado en forma de polinomio visual y como lista de coeficientes
print("Polinomio resultado:")
print(resultado)

print("Coeficientes del polinomio resultante (de mayor a menor grado):")
print(resultado.coefficients)
