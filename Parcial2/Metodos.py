def calcular_salario(salario_bruto):
        if(salario_bruto < 9500):
            return salario_bruto
        
        descuento = salario_bruto * 0.26
        return salario_bruto -descuento

def obtenerAguinaldo(salario_bruto):
    salario_diaro = salario_bruto / 30
    print("caunto gano por dia :(",salario_diaro)
    return salario_diaro*15
    


salario = 9000
print("Empresa: GAMA CONSULTORES IA")
print(calcular_salario(salario))
print(obtenerAguinaldo(salario))
print("Desarrollador Java Full Stack Intermedio Senior")
print(calcular_salario(36000.00))
print(obtenerAguinaldo(36000.00))