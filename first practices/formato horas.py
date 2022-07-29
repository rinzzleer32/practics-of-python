def calcular_horario(hora:int,minutos:int) -> dict:
    minutos -=60
    hora += 1
    print ("La nueva hora es : ",hora,":",minutos)
    return ()

def calcular_horario_Adicional(hora:int,minutos:int) -> dict:
    minutos -=60
    hora = 0
    print ("La nueva hora es : ",hora,":",minutos)
    return ()

print("bienvenido")
hora = int(input("Escriba las horas: "))
minutos = int(input("Escriba los minutos: "))

if hora >= 25 or minutos >= 61 or hora < 0 or minutos < 0:
    print("formato no valido")

else:
    minutos += 30
    if minutos < 60:
        print ("La nueva hora es : ",hora,":",minutos)
    elif minutos >= 60 and hora == 24:
       calcular_horario_Adicional(hora,minutos)
    elif minutos >=60:  
       calcular_horario(hora,minutos)
    

