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
#A continuacion de hara el calculo de las temperaturas por ciudad segun los datos obtenidos por semana.
#se declara una matriz donde se guardara los promedios
promedios=[]
#Se crea un bucle for para promediar
for ciudad in range(ciudades):
    promedio_ciudad=[]
    promedio_semanal=[]
    #se crea otro bucle for donde se hara el promedio de las temperaturas segun la ciudad tomando en cuenta las ciudades
    for semana in range(semanas):
        promedio_semanal.append(sum(temperaturas[ciudad][semana])/dias)
        promedio_ciudad.append(promedio_semanal)
    promedios.append(promedio_ciudad)
#se muestra en pantalla los promedios por ciudad
print("Promedios de temperaturas por ciudad:")
print(promedios)

#Se añade como extra el promedio separado por ciudad y semana
print("nPromedios de temperaturas por ciudad y semana:")
for i, promedio_ciudad in enumerate(promedios):
    print(f"Promedio de temperaturas en la ciudad {i+1}:´{promedio_ciudad}")

