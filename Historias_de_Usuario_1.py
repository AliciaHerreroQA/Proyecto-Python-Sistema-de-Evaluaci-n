#el sistema debe pedir el nombre del estudiante
nombre_estudiante = input("Introduce tu nombre: ")
print("El nombre del estudiante es: ", nombre_estudiante)

#el sistema debe pedir 3 notas del estudiante
nota1=float(input("Introduce la primera nota: "))
nota2=float(input("Introduce la segunda nota: "))
nota3=float(input("Introduce la tercera nota: "))

#el sistema debe calcular la nota final, q será la media de las 3 notas introducidas
suma = nota1 + nota2 + nota3
media = (nota1 + nota2 + nota3) / 3
#el sistema debe mostrar la nota final del estudiante
print("La media de las notas es: ", media)

#el sistema debe mostrar el nombre del estudiante en mayúscula
nombre_estudiante_mayusculas = nombre_estudiante.upper()
print("Este es el nombre del estudiante en mayúsculas: ", nombre_estudiante_mayusculas)



#HISTORIA DE USUARIO 2

def notaFinal(nota):
    if nota <5:
        print("SUSPENSO") 
    elif nota >= 5 and nota < 7:
        print("APROBADO")
    elif nota >= 7 and nota < 9:
        print("NOTABLE")
    else:
        print("SOBRESALIENTE")



nota = float(input("Introduce las notas del examen del estudiante: "))
mensaje = notaFinal(nota)
print(mensaje)


#HISTORIA DE USUARIO 3


def calificacion(nota):
    if nota <5:
       return "SUSPENSO" 
    elif nota >= 5 and nota < 7:
        return "APROBADO"
    elif nota >= 7 and nota < 9:
        return "NOTABLE"
    else:
        return "SOBRESALIENTE"
    
for i in range(5):
    nombre = input("Nombre del estudiante: ").upper()

    nota1=float(input("Nota 1: "))
    nota2=float(input("Nota 2: "))
    nota3=float(input("Nota 3: "))
    notaFinal = (nota1 + nota2 + nota3) /3
    resultado=calificacion(notaFinal)

    print(nombre + " -  Nota final: " + str(notaFinal) + " - Calificación: " + resultado ) 
    
