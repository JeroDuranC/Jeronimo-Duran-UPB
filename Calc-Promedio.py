def main():
    print("Ingrese sus 5 calificaciones:")
    calificaciones = []
    
    for i in range(5):
        calificacion = float(input("Calificación {}: ".format(i+1)))
        calificaciones.append(calificacion)
    
    promedio = sum(calificaciones) / len(calificaciones)
    print("El promedio es:", promedio)
    
    if promedio >= 60:
        print("Aprobado")
    elif 40 <= promedio < 60:
        print("En recuperación")
    else:
        print("Reprobado")

if __name__ == "__main__":
    main()
