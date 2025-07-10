

# ----- Suma de polinomios de forma Vanilla ----- 

def suma_de_polinomios(p1, p2):
    # comprobar que p1 sea el polinomio mas largo
    if len(p2) > len(p1):
        p1, p2 = p2, p1
    
    # Creamos una copia de p1 para no modificar la lista original directamente
    resultado = p1[:]

    # Recorremos cada índice de p2 y sumamos su valor al correspondiente en resultado (que es una copia de p1)
    # Esto asegura que solo se sumen los coeficientes que existen en ambos polinomios
    for i in range(len(p2)):
        print(f"Se esta sumando {resultado[i]} + {p2[i]}")
        resultado[i] += p2[i]
    
    return resultado

# Polinomios representados como listas de coeficientes, del término independiente al de mayor grado
a = [2, 3, 4]   # 2 + 3x + 4x²
b = [5, 6, 7]   # 5 + 6x + 7x²

print("Polinomios originales:", a, b)
print("Resultado de la suma:", suma_de_polinomios(a, b))

