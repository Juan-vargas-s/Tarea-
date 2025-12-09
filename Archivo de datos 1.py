"""
Ejercicio de archivos (nivel Prog 2):
1) Pedir N y leer N asignaturas (codigo, descripcion, creditos) desde teclado.
   Guardarlas en un archivo secuencial de texto.
2) Leer P y cargar P asignaturas desde el archivo de texto a un vector de registros.
3) Ordenar el vector ascendentemente por creditos.
4) Guardar el vector ordenado en un archivo binario.
"""

import pickle


def leer_asignaturas(cantidad):
	asignaturas = []
	for i in range(cantidad):
		print(f"Asignatura {i+1}")
		codigo = input("Codigo: ").strip()
		descripcion = input("Descripcion: ").strip()
		creditos = int(input("Unidades de credito: "))
		asignaturas.append([codigo, descripcion, creditos])
	return asignaturas


def guardar_secuencial(nombre_archivo, asignaturas):
	with open(nombre_archivo, "w", encoding="utf-8") as f:
		for codigo, descripcion, creditos in asignaturas:
			f.write(f"{codigo}|{descripcion}|{creditos}\n")


def leer_secuencial(nombre_archivo, cantidad):
	leidas = []
	with open(nombre_archivo, "r", encoding="utf-8") as f:
		for _ in range(cantidad):
			linea = f.readline()
			if not linea:
				break
			partes = linea.strip().split("|")
			if len(partes) != 3:
				continue
			codigo, descripcion, creditos = partes[0], partes[1], int(partes[2])
			leidas.append([codigo, descripcion, creditos])
	return leidas


def ordenar_por_creditos(asignaturas):
	# seleccion ascendente sin lambda
	n = len(asignaturas)
	for i in range(n - 1):
		idx_min = i
		for j in range(i + 1, n):
			if asignaturas[j][2] < asignaturas[idx_min][2]:
				idx_min = j
		if idx_min != i:
			temp = asignaturas[i]
			asignaturas[i] = asignaturas[idx_min]
			asignaturas[idx_min] = temp
	return asignaturas


def guardar_binario(nombre_archivo, asignaturas):
	with open(nombre_archivo, "wb") as f:
		pickle.dump(asignaturas, f)


def demo():
	print("Demostracion rapida")
	asignaturas = [
		["INF101", "Intro a la prog", 5],
		["MAT102", "Calculo I", 4],
		["FIS103", "Fisica I", 3],
	]
	guardar_secuencial("asignaturas.txt", asignaturas)
	leidas = leer_secuencial("asignaturas.txt", 3)
	ordenar_por_creditos(leidas)
	guardar_binario("asignaturas_ordenadas.bin", leidas)
	print("Archivo texto: asignaturas.txt")
	print("Archivo binario: asignaturas_ordenadas.bin")


def main():
	nombre_txt = "asignaturas.txt"
	nombre_bin = "asignaturas_ordenadas.bin"

	n = int(input("Cantidad de asignaturas (N): "))
	asignaturas = leer_asignaturas(n)
	guardar_secuencial(nombre_txt, asignaturas)

	p = int(input("Cantidad a leer desde archivo (P): "))
	desde_archivo = leer_secuencial(nombre_txt, p)
	ordenar_por_creditos(desde_archivo)
	guardar_binario(nombre_bin, desde_archivo)

	print("\nVector ordenado por creditos:")
	for codigo, desc, cred in desde_archivo:
		print(f"{codigo} - {desc} - {cred} uc")
	print(f"Datos guardados en {nombre_bin}")


if __name__ == "__main__":
	usar_demo = input("¿Usar datos de prueba? (s/n): ").strip().lower().startswith("s")
	if usar_demo:
		demo()
	else:
		main()
