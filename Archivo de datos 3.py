"""
Ejercicio c) Archivos (nivel Prog 2):
1) Leer A y B (enteros).
2) Guardar pares en PARES.TXT (texto) y impares en IMPARES.TXT (binario con pickle).
3) Leer ambos archivos y mostrarlos en pantalla.
"""

import pickle


def generar_rango(a, b):
	if a <= b:
		inicio, fin = a, b
	else:
		inicio, fin = b, a
	return list(range(inicio, fin + 1))


def escribir_pares(nombre, numeros):
	with open(nombre, "w", encoding="utf-8") as f:
		for n in numeros:
			if n % 2 == 0:
				f.write(str(n) + "\n")


def escribir_impares_bin(nombre, numeros):
	impares = []
	for n in numeros:
		if n % 2 != 0:
			impares.append(n)
	with open(nombre, "wb") as f:
		pickle.dump(impares, f)


def leer_pares(nombre):
	pares = []
	with open(nombre, "r", encoding="utf-8") as f:
		for linea in f:
			try:
				pares.append(int(linea.strip()))
			except ValueError:
				pass
	return pares


def leer_impares_bin(nombre):
	with open(nombre, "rb") as f:
		impares = pickle.load(f)
	return impares


def demo():
	print("Demostracion rapida (A=3, B=10)")
	a, b = 3, 10
	numeros = generar_rango(a, b)
	escribir_pares("PARES.TXT", numeros)
	escribir_impares_bin("IMPARES.TXT", numeros)
	print("Pares:", leer_pares("PARES.TXT"))
	print("Impares:", leer_impares_bin("IMPARES.TXT"))


def main():
	a = int(input("Ingrese A (entero): "))
	b = int(input("Ingrese B (entero): "))

	numeros = generar_rango(a, b)

	escribir_pares("PARES.TXT", numeros)
	escribir_impares_bin("IMPARES.TXT", numeros)

	pares = leer_pares("PARES.TXT")
	impares = leer_impares_bin("IMPARES.TXT")

	print("\nContenido de PARES.TXT:")
	print(pares)
	print("Contenido de IMPARES.TXT:")
	print(impares)


if __name__ == "__main__":
	usar_demo = input("¿Usar datos de prueba? (s/n): ").strip().lower().startswith("s")
	if usar_demo:
		demo()
	else:
		main()
