# Función para procesar notas de alumnos
def cargarEvaluacion(nombreArchivo, puntajeTotal, exigencia):
    # Lista para almacenar la información de los alumnos
    lista_alumnos = []

    # Códigos ANSI para los colores
    color_verde = "\033[92m" #Aprobado
    color_rojo = "\033[91m" #Reprobado
    reset_color = "\033[0m" #Color por defecto

    # Abrir el archivo de texto
    with open(nombreArchivo, 'r', encoding='utf-8') as archivo:
        # Leer cada línea del archivo
        for linea in archivo:
            # Dividir la línea en elementos separados por ';'
            elementos = linea.strip().split(';')

            # Obtener RUT y Nombre del alumno
            rut = elementos[0]
            nombre = elementos[1]

            # Calcular el puntaje total obtenido por el alumno
            puntajes = elementos[2:]

            # Inicializamos la variable puntajeTotalObtenido en 0
            puntajeObtenido = 0

            # Recorremos los puntajes y los sumamos uno a uno
            for puntaje in puntajes:
                puntajeObtenido += int(puntaje)

            # Variables para notas
            notaMaxima = 7.0
            notaMinima = 1.0
            notaAprobacion = 4.0

            # Calcular la nota final (fórmula de https://escaladenotas.cl)
            if puntajeObtenido >= puntajeTotal * exigencia:
                notaFinal = round((notaMaxima - notaAprobacion) * (puntajeObtenido - exigencia * puntajeTotal) / (puntajeTotal * (1 - exigencia)) + notaAprobacion, 1)
                estado = color_verde + "Aprobado" + reset_color
            else:
                notaFinal = round(((notaAprobacion - notaMinima) * puntajeObtenido) / (exigencia * puntajeTotal) + notaMinima, 1)
                estado = color_rojo + "Reprobado" + reset_color

            # Agregar la información del alumno a la lista
            lista_alumnos.append({
                'RUT': rut,
                'Nombre': nombre,
                'Puntaje Total Obtenido': puntajeObtenido,
                'Nota Obtenida': notaFinal,
                'Estado': estado
            })

    return lista_alumnos

#Programa
if __name__ == "__main__":
    # Definir el nombre del archivo y el puntaje total
    nombreArchivo = 'datos_prueba.txt'
    puntajeTotal = 60

    # Solicitar al usuario que seleccione una opción de exigencia
    print("Opción 1: 60% exigencia\nOpción 2: 50% exigencia\nSelecciona respuesta :",end="")
    opcion = input("")

    # Asignar exigencia seleccionada
    if opcion == '1':
        exigencia = 0.6
    elif opcion == '2':
        exigencia = 0.5
    else:
        exigencia = 0.6  # Valor por defecto si la opción no es válida

    # Llamar a la función cargarEvaluacion()
    resultado_evaluacion = cargarEvaluacion(nombreArchivo, puntajeTotal, exigencia)

    # Imprimir la información de los alumnos
    for alumno in resultado_evaluacion:
        print(f"RUT: {alumno['RUT']}")
        print(f"Nombre: {alumno['Nombre']}")
        print(f"Puntaje Total Obtenido: {alumno['Puntaje Total Obtenido']} de {puntajeTotal}")
        print(f"Nota Obtenida: {alumno['Nota Obtenida']:.1f}")
        print(f"Estado: {alumno['Estado']}")
        print()