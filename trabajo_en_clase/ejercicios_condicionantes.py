
fecha_actual=input("Ingrese fecha actual en el siguiente formato día,DD/MM: dia de semana, Dia del mes/Mes actual: ")
cortar_fecha=fecha_actual.split(",")
print(cortar_fecha)
dia=cortar_fecha[0]
dia_mes=cortar_fecha[1].split("/")

dia_del_mes=int(dia_mes[0])
mes=int(dia_mes[1])


# Dia de semana: 
dia_format=dia.lower()
if dia_format!="lunes" or dia_format!="martes" or dia_format!="miercoles" or dia_format!="jueves" or dia_format!="viernes" or dia_format!="sabado" or dia_format!="domingo":
    print("Día inválido:", dia)
elif dia_format=="sabado" or dia_format=="domingo":
    print("Día incorrecto: corresponde a fin de semana")
else:
    print("DIA DE SEMANA: ", dia)

#Dia de mes: menor a 30 y mayor a 0
if dia_del_mes<=0 or dia_del_mes>30:
    print("Dia del mes ingresado icorrecto")
else:
    print("DIA DE MES: ", dia_del_mes)

#Dia mes: menor a 12 y mayor a 0
if mes<=0 or mes>12:
    print("Mes ingresado incorrcto")
else: 
    print("MES: ", mes)

#transformacion de la cadena a minuscula
dia_format = dia.lower()


if dia_format =="lunes" or dia_format=="martes" or dia_format=="miercoles":
    print(f"El dia {dia_format} se tomo examen")
    numero_de_aprobados=int(input("Ingrese el numero de alumno aprobados: "))
    numero_de_desaprobados=int(input("Ingrese el numero de desaprobados: "))
    total_de_alumnos= numero_de_aprobados+numero_de_desaprobados
    porcentajes_de_desaprobados=(numero_de_desaprobados*100)/total_de_alumnos
    print(f"El porcentade de alumnos desaprobado el dia  es de %{porcentajes_de_desaprobados} ")
    porcentajes_de_aprobados=(numero_de_aprobados)*100/total_de_alumnos
    print(f"El porcentade de alumnos aprobado el dia es de %{porcentajes_de_aprobados} ")
else:
    if dia_format == "jueves":
        print("Ese día no se tomarán exámenes")
        porcentaje_asistencia = int(input("Ingrese el porcentaje de asistencia: "))
        if porcentaje_asistencia > 50:
            print("Asistió la mayoría")
        else:
            print("No asistió la mayoría")
    elif dia_format == "viernes" and dia_del_mes == 1 and (mes == 1 or mes == 7):
        print("Comienzo de nuevo ciclo (Inglés para viajeros)")
        alumnos_nuevos = int(input("Ingrese la cantidad de alumnos ingresantes: "))
        arancel_por_alumno = int(input("Ingrese el arancel por alumno en $: "))
        print(f"El arancel por alumno es de ${arancel_por_alumno}")
        print(f"El ingreso total es de ${arancel_por_alumno * alumnos_nuevos}")


