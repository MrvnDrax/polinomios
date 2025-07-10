# 📐 Polinomios en Python

Este repositorio contiene dos implementaciones para la suma de polinomios en Python:

- **`vanilla.py`**: suma polinomios de forma manual usando listas y ciclos `for`, sin depender de librerías externas.
- **`polipy.py`**: suma polinomios utilizando la clase `numpy.poly1d`, que facilita las operaciones algebraicas con polinomios.

---

## 📂 Archivos incluidos

### `vanilla.py`

Implementa la suma de polinomios mediante listas y bucles simples.

- Los polinomios se representan como listas de coeficientes, **del término independiente al de mayor grado**.
- Permite sumar polinomios de distinta longitud manejando adecuadamente los índices.

### `polipy.py`

Utiliza `numpy.poly1d` para trabajar con polinomios como objetos matemáticos.

- Los coeficientes se representan **del mayor al menor grado**, como requiere `poly1d`.
- Permite sumar, imprimir y manipular polinomios de forma sencilla.

---

## 🚀 Requisitos

Para ejecutar `polipy.py` necesitas tener instalada la librería `NumPy`.

Se incluye un archivo `requirements.txt` con las dependencias necesarias para este proyecto:




### ¿Qué es `requirements.txt`?

Es un archivo de texto que lista todas las librerías que tu proyecto necesita para funcionar correctamente. Esto facilita que otros desarrolladores (o tú mismo en otro equipo/entorno) puedan instalar todas las dependencias con un solo comando.

---

## 🧪 Cómo usar

### Instalar dependencias

Ejecuta este comando para instalar las librerías indicadas en `requirements.txt`:

```bash
pip install -r requirements.txt

## Ejecutar

python3 vanilla.py   # Ejecuta la suma sin librerías externas
python3 polipy.py    # Ejecuta la suma usando NumPy
