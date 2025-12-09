def main():
    score = []
    studentName = []
    idCard = []
    DataEnter(score, studentName, idCard)
    Print(score, studentName, idCard)
    return


def DataEnter(score, studentName, idCard):
    cantidad = int(input("Cuantos estudiantes?: "))
    while(cantidad <= 0): # con este while evitamos que ingrese una cantidad de estudiantes que no tenga sentido y nos pueda dar problemas en el preoceso del codigo
        cantidad = int(input("Ingreso una cantidad de estudiantes no valida. Intente de nuevo: "))
    
    for student in range(cantidad):
        name = input("Nombre y apellido de estudiante: ")
        studentName.append(name)

        id = input("ingrese su número de cedula: ")
        idCard.append(id)

        studentScore = float(input("Nota: "))
        while(studentScore <= 0 or studentScore > 20):  
        # con este while validamos que la entrada por teclado tenga sentido, en caso de que no tenga sentido obligaremos al usuario a que ingrese una nota valida
            studentScore = float(input("Ingreso una nota no valida. Intente de nuevo: "))
        score.append(studentScore)

        
    return



def Promedie(score):
    totalScore = len(score)
    if totalScore == 0:
        return 0

    totalStudentSum = 0
    for numberScore in range(totalScore): # primeramente sumamos todas las notas de la sección 
        totalStudentSum = totalStudentSum + score[numberScore]

    sectionPromedie = totalStudentSum/totalScore # y ahora hacemos el  calculo del promedio 


    if (sectionPromedie < 0 or sectionPromedie > 20 ): # pequeña validacion para evitar problemas durante la ejecución de código 
        print ("problema durante el promedio")
        return  
    
    return sectionPromedie



def BelowPromedie(score,names):
    studentsBelowThePromedie = []
    studentsScoreBelowThePromedie = []
    
    for i in range(len(score)):
        if(score[i]< Promedie(score)):
            studentsScoreBelowThePromedie.append(score[i])
            studentsBelowThePromedie.append(names[i])

    return studentsScoreBelowThePromedie, studentsBelowThePromedie


def BestStudent(score,names):
    bestStudent = ""
    bestScore = 0
    for i in range(len(score)):
        if bestScore < score[i]:
            bestStudent = names[i]
            bestScore = score[i]

    return bestStudent, bestScore

def Print(score,names,idCard):
    OrdenarNotasDesc(score, names, idCard)

    sectionPromedie = Promedie(score)
    bestStudent,bestScore = BestStudent(score,names)
    studentsScoreBelowThePromedie, studentsBelowThePromedie = BelowPromedie(score,names)

    print("\nListado de estudiantes ordenado por nota (descendente):")
    for i in range(len(score)):
        print(f"{i+1}. {names[i]} - ID {idCard[i]} - Nota {score[i]}")

    print(f"\nPromedio de la sección: {sectionPromedie}")
    print(f"Mejor estudiante: {bestStudent} con nota {bestScore}")
    print("\nEstudiantes con nota por debajo del promedio:")
    for i in range(len(studentsBelowThePromedie)):
        print(f"{studentsBelowThePromedie[i]} - Nota {studentsScoreBelowThePromedie[i]}")

    return

def OrdenarNotasDesc(score, names, id_cards):
    # ordena in-place por selección, sin zip ni tuplas, manteniendo sincronía
    n = len(score)
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if score[j] > score[max_idx]:
                max_idx = j

        if max_idx != i:
            # swap score
            temp = score[i]
            score[i] = score[max_idx]
            score[max_idx] = temp

            # swap names
            temp = names[i]
            names[i] = names[max_idx]
            names[max_idx] = temp

            # swap ids
            temp = id_cards[i]
            id_cards[i] = id_cards[max_idx]
            id_cards[max_idx] = temp

    return

def Demo():
    # datos de prueba para validar salida
    score = [19.5, 12.0, 17.8, 20.0]
    studentName = ["Ana Pérez", "Luis Torres", "Mía Gómez", "José Lara"]
    idCard = ["V-101", "V-102", "V-103", "V-104"]
    Print(score, studentName, idCard)


if __name__ == "__main__":
    usar_demo = input("¿Usar datos de prueba? (s/n): ").strip().lower().startswith("s")
    if usar_demo:
        Demo()
    else:
        main()