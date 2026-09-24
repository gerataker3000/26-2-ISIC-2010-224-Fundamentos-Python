taquerias = {
    "Taqueria 1": {
        "Nombre": "tacos emilio",
        "empleados": 12,
        "Combos": ["2 por 1","Otro combito"]
    },
    "Taqueria 2": {
        "Nombre": "tacos grillos",
        "empleados": 5,
        "Combos": ["2 por 2","Otro combito 2"]
    }
}

for clave,valor in taquerias.items():
    print("=========================")
    print(clave)
    print(valor['Nombre'])
    print(valor['empleados'])
    for lista in valor['Combos']:
        print("cada combo: ",lista)
