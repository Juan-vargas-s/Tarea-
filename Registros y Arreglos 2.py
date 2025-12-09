"""Resolución en estilo sencillo para el enunciado b)."""


def leer_alumnos(cantidad, titulo):
	alumnos = []
	print(titulo)
	for i in range(cantidad):
		cedula = input(f"Alumno {i+1} - Cédula: ").strip()
		nombre = input(f"Alumno {i+1} - Apellido y nombres: ").strip()
		alumnos.append([cedula, nombre])

	alumnos.sort()  # aseguramos orden por cédula (se compara por primer elemento)
	return alumnos


def leer_cedulas(cantidad, titulo):
	cedulas = []
	print(titulo)
	for i in range(cantidad):
		cedula = input(f"Cédula {i+1}: ").strip()
		cedulas.append(cedula)

	cedulas.sort()
	return cedulas


def fusionar_base_ingresos(base, ingresos):
	# ambas listas están ordenadas por cédula
	i = 0
	j = 0
	resultado = []

	while i < len(base) and j < len(ingresos):
		ced_base = base[i][0]
		ced_ing = ingresos[j][0]

		if ced_base == ced_ing:
			# si coinciden, nos quedamos con el que viene en ingresos
			resultado.append(ingresos[j])
			i += 1
			j += 1
		elif ced_base < ced_ing:
			resultado.append(base[i])
			i += 1
		else:
			resultado.append(ingresos[j])
			j += 1

	# agregamos lo que falte
	while i < len(base):
		resultado.append(base[i])
		i += 1

	while j < len(ingresos):
		resultado.append(ingresos[j])
		j += 1

	return resultado


def aplicar_retiros(lista_alumnos, retiros):
	retiros_set = set(retiros)
	filtrados = []
	for alumno in lista_alumnos:
		if alumno[0] not in retiros_set:
			filtrados.append(alumno)
	return filtrados


def imprimir_lista(alumnos, titulo):
	print(f"\n{titulo}")
	if not alumnos:
		print("(sin alumnos)")
		return
	for idx, alumno in enumerate(alumnos, start=1):
		print(f"{idx}. {alumno[0]} - {alumno[1]}")


def calcular_lista_definitiva(base, ingresos, retiros):
	con_ingresos = fusionar_base_ingresos(base, ingresos)
	definitiva = aplicar_retiros(con_ingresos, retiros)
	return definitiva


def demo():
	base = [
		["V-101", "Ana Perez"],
		["V-102", "Luis Torres"],
		["V-104", "Jose Lara"],
	]

	ingresos = [
		["V-103", "Mia Gomez"],
		["V-105", "Carlos Ruiz"],
	]

	retiros = ["V-102"]

	imprimir_lista(base, "Lista base")
	imprimir_lista(ingresos, "Ingresos")
	imprimir_lista([[c, ""] for c in retiros], "Retiros (solo cédula)")

	definitiva = calcular_lista_definitiva(base, ingresos, retiros)
	imprimir_lista(definitiva, "Lista definitiva")


def main():
	cant_base = int(input("Cantidad de alumnos base: "))
	base = leer_alumnos(cant_base, "Ingrese alumnos base (orden ascendente por cédula):")

	cant_ingresos = int(input("Cantidad de alumnos que ingresaron luego: "))
	ingresos = leer_alumnos(cant_ingresos, "Ingrese alumnos ingresados (orden ascendente por cédula):")

	cant_retiros = int(input("Cantidad de alumnos que retiraron: "))
	retiros = leer_cedulas(cant_retiros, "Ingrese cédulas de retiros (orden ascendente):")

	definitiva = calcular_lista_definitiva(base, ingresos, retiros)

	imprimir_lista(base, "Lista base")
	imprimir_lista(ingresos, "Ingresos")
	imprimir_lista([[c, ""] for c in retiros], "Retiros (solo cédula)")
	imprimir_lista(definitiva, "Lista definitiva")


if __name__ == "__main__":
	usar_demo = input("¿Usar datos de prueba? (s/n): ").strip().lower().startswith("s")
	if usar_demo:
		demo()
	else:
		main()
