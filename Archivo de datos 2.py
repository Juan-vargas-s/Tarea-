"""
Ejercicio b) Archivos (nivel Prog 2)
1) Leer N carreras (codigo, descripcion, total alumnos) y guardarlas en un archivo binario.
2) Leer ese binario a un vector de registros.
3) Mostrar el vector y el total de alumnos de la institución.
4) Guardar en un archivo secuencial de texto la cantidad y los datos del vector.
"""

import pickle


def leer_carreras(cantidad):
	carreras = []
	for i in range(cantidad):
		print(f"Carrera {i+1}")
		codigo = input("Codigo: ").strip()
		descripcion = input("Descripcion: ").strip()
		total = int(input("Total alumnos cursantes: "))
		carreras.append([codigo, descripcion, total])
	return carreras


def guardar_binario(nombre, carreras):
	with open(nombre, "wb") as f:
		pickle.dump(carreras, f)


def leer_binario(nombre):
	with open(nombre, "rb") as f:
		carreras = pickle.load(f)
	return carreras


def imprimir_carreras(carreras):
	print("\nCarreras leidas:")
	total_general = 0
	if not carreras:
		print("(sin carreras)")
	else:
		for i, car in enumerate(carreras, start=1):
			print(f"{i}. {car[0]} - {car[1]} - {car[2]} alumnos")
			total_general = total_general + car[2]
	print(f"Total alumnos en la institucion: {total_general}")
	return total_general


def guardar_secuencial(nombre, carreras):
	with open(nombre, "w", encoding="utf-8") as f:
		f.write(str(len(carreras)) + "\n")
		for car in carreras:
			linea = f"{car[0]}|{car[1]}|{car[2]}\n"
			f.write(linea)


def demo():
	print("Demostracion rapida")
	carreras = [
		["INF", "Informatica", 120],
		["ADM", "Administracion", 80],
		["DER", "Derecho", 150],
	]

	guardar_binario("carreras.bin", carreras)
	leidas = leer_binario("carreras.bin")
	imprimir_carreras(leidas)
	guardar_secuencial("carreras.txt", leidas)
	print("Archivos generados: carreras.bin y carreras.txt")


def main():
	nombre_bin = "carreras.bin"
	nombre_txt = "carreras.txt"

	n = int(input("Cantidad de carreras (N): "))
	carreras = leer_carreras(n)
	guardar_binario(nombre_bin, carreras)

	print("\nLeyendo desde archivo binario...")
	cargadas = leer_binario(nombre_bin)
	imprimir_carreras(cargadas)
	guardar_secuencial(nombre_txt, cargadas)
	print(f"Datos guardados en {nombre_txt}")


if __name__ == "__main__":
	usar_demo = input("¿Usar datos de prueba? (s/n): ").strip().lower().startswith("s")
	if usar_demo:
		demo()
	else:
		main()
