import random
ciudades =3
dias =7
semanas =4
temperaturas =[]
for ciudad in range(ciudades):
    ciudad_tem= []
    for semana in range(semanas):
        semana_tem = []
        for dia in range(dias):
            semana_tem.append(random.randint(15,35))
        ciudad_tem.append(semana_tem)
    temperaturas.append(ciudad_tem)
print("Matriz de temperaturas:")
print(temperaturas)

promedios=[]
for ciudad in range(ciudades):
    promedio_ciudad=[]
    promedio_semanal=[]
    for semana in range(semanas):
        promedio_semanal.append(sum(temperaturas[ciudad][semana])/dias)
        promedio_ciudad.append(promedio_semanal)
    promedios.append(promedio_ciudad)
print("Promedios de temperaturas por ciudad:")
print(promedios)

print("nPromedios de temperaturas por ciudad y semana:")
for i, promedio_ciudad in enumerate(promedios):
    print(f"Promedio de temperaturas en la ciudad {i+1}:´{promedio_ciudad}")
