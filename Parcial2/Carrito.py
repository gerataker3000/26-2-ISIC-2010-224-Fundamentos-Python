def es_eficiente(km = 20,lt = 1):
    rendimiento = km/lt
    if(rendimiento >=15):
        return True

    return False

print(es_eficiente())