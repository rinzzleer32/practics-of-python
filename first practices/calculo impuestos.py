user= input("Ingrese nombre: ")
salario= float(input("Ingrese su salario: "))

cuota_a_pagar_2 = 17.67
cuota_a_pagar_3 = 60.00
cuota_a_pagar_4 = 288.57

p1 = 472.01
p2 = 895.25
p3 = 2038.11

isss = salario* 0.03 if salario* 0.03 < 30 else 30
afp = salario* 0.0725;

def calcular_renta(salarioLessIssAfp):
    if 0.01 <= salarioLessIssAfp <= 472:
        return 0
    elif 472.01 <= salarioLessIssAfp <= 895.24:
        return ((salarioLessIssAfp - p1) * 0.1) + cuota_a_pagar_2
    elif 895.25 <= salarioLessIssAfp <= 2038.10:
        return ((salarioLessIssAfp - p2) * 0.2) + cuota_a_pagar_3
    else:
        return ((salarioLessIssAfp - p3) * 0.3) + cuota_a_pagar_4

def calcular_renta_v2(salarioLessIssAfp):
    return isss + afp + calcular_renta(salarioLessIssAfp)

print("Ingrese el salario: ", salario)
print("Renta: ", calcular_renta(salario- isss - afp))
print("AFP: ", afp)
print("ISSS: ", isss)
print("Descuento total: ", isss + afp + calcular_renta(salario- isss - afp))
print("Salario liquido: ", salario- (isss + afp + calcular_renta(salario- isss - afp)))