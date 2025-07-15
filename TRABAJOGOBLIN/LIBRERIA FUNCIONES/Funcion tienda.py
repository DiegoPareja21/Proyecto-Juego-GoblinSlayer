

#
#
import random









def utensilio_que_quiero_utilizar(mochila,Utensilio_uso):
    print(mochila)
    cuestion_herramienta=input("Que utensilio desea utilizar en el proximo combate: ")
    for i in range(len(mochila)):
        if mochila[i] == cuestion_herramienta:
            print("Usted acaba de coger el siguiente utensilio")
            return Utensilio_uso

mochila=["espada","hacha"]
Utensilio_uso=" "
dano_ataque=0
recibir_dano=0
Fuerza=10
def mochila_personaje(mochila,Utensilio_uso,dano_ataque,recibir_dano):
    
    while True:

        print("Usted tiene en la mochila: ", mochila)
        Utensilio = input("Que utensilio desea utilizar: ")
        for i in range(len(mochila)):
            if Utensilio == mochila[i]:
                print("Ha obtenido el siguiente objeto para el combate: ", mochila[i])
                Utensilio_uso=mochila[i]
                if Utensilio_uso == "espada":
                    dano_ataque=+ random.randint(1,8)
                    return dano_ataque
                elif Utensilio_uso == "escudo":
                    recibir_dano=+1
                    return recibir_dano

                elif Utensilio_uso == "armadura":
                    recibir_dano=+2
                    return recibir_dano
                elif Utensilio_uso == "hacha a dos manos":
                    dano_ataque=random.randint(1,12)
                    return dano_ataque
                elif Utensilio_uso == "espada magica":
                    dano_ataque = random.randint(1,8)+2
                    return dano_ataque
                elif Utensilio_uso == "espada goblin":
                    dano_ataque= random.randint(1,6)
                    return dano_ataque
                elif Utensilio_uso == "escudo goblin":
                    recibir_dano =+1
                    return recibir_dano
        cuestion_mochila=input("Desea coger mas objetos de la mochila (si/no): ")
        if cuestion_mochila == "si":
            continue
        else:
            print("Se abandona la mochila")


#print(mochila_personaje(mochila,Utensilio_uso,dano_ataque,recibir_dano))
#
#dano= mochila_personaje(mochila,Utensilio_uso,recibir_dano,dano_ataque)
#dano_ataque=dano+(Fuerza-10)
monedas_totales=500
#
#
#
#
#
#
#
def tienda(monedas_totales,mochila):
    monedas_espada=10
    monedas_pocion=20
    monedas_escudo=0
    monedas_armadura=30
    monedas_hacha_a_dos_manos=30
    monedas_espada_magica=200
    print("Bienvenido de nuevo a la tienda de Charly")
    print("Tenemos numerosos utensilios que le pueden ser de ayuda")



    while True:

        util = int(input("Pulse 1 = pocion de vida. Pulse 2 = Espada. Pulse 3 = Escudo. Pulse 4 = Armadura. Pulse 5 = Hacha a dos manos. Pulse 6 = Espada magíca: "))
        if util == 2:
            if monedas_totales >= 10:
                monedas_totales -= monedas_espada
                print("Acaba de conseguir la espada")
                print("Le quedan un  total de ", monedas_totales, " monedas totales")
                print("Utensilio obtenido")
                mochila.append("espada")
                

            else:
                print("No tienes monedas para este utensilio")

        elif util == 1:
            if monedas_totales >= 20:
                monedas_totales -= monedas_pocion
                print("Acaba de conseguir la pocion de vida")
                print("Le quedan un  total de ", monedas_totales, " monedas totales")
                print("Utensilio obtenido")
                mochila.append("pocion de vida")

            else:
                print("No tiene monedas para este utensilio")

        elif util == 3:
            if monedas_totales >= 10:
                monedas_totales -= monedas_escudo
                print("Acaba de conseguir el escudo")
                print("Le quedan un  total de ", monedas_totales, " monedas totales")
                print("Utensilio obtenido")
                mochila.append("escudo")

            else:
                print("No tiene monedas para este utensilio")

        elif util == 4:
            if monedas_totales >= 30:
                monedas_totales -= monedas_armadura
                print("Acaba de conseguir la armadura")
                print("Le quedan un  total de ", monedas_totales, " monedas totales")
                print("Utensilio obtenido")
                mochila.append("armadura")

            else:
                print("No tiene monedas para este utensilio")


        elif util == 5:
            if monedas_totales >= 30:
                monedas_totales -= monedas_hacha_a_dos_manos
                print("Acaba de conseguir la hacha a dos manos")
                print("Le quedan un  total de ", monedas_totales, " monedas totales")
                print("Utensilio obtenido")
                mochila.append("hacha a dos manos")

            else:
                print("No tiene monedas para este utensilio")

        elif util == 6:
            if monedas_totales >= 200:
                monedas_totales -= monedas_espada_magica
                print("Acaba de comprar la espada magica , enhorabuena")
                print("Le quedan un  total de ", monedas_totales, " monedas totales")
                mochila.append("espada magica")

            else:
                print("No tiene monedas para este util")
        cuestion_tienda = input("Desea usted seguir (si/no)").lower()
        if cuestion_tienda == "si":
            continue
        else:
            return monedas_totales,mochila
            

monedas_totales,mochila=tienda(monedas_totales,mochila)

#
#
#
#tienda(monedas_totales,mochila)

















