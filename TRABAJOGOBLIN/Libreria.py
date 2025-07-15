

import random

Donde_ir=" "
Fuerza=10
Constitucion=10
Destreza=10
puntos=3
monedas_totales=300
mochila=["puños"]
Utensilio_combate=" "
Utensilio_defensa=" "
experiencia_personaje=0
dano_ataque=0+(Fuerza-10)
recibir_dano=0+(Destreza-10)
Vida_personaje=20+ ((Constitucion-10)*2)
pocion_vida=0

def tutorial():
    print(
        "Usted caballero fue acogido por una familia de este reino despues de que enfrente de sus ojos el odioso ogro... Se comiese a su madre sin dejar pieza de ella. ")
    input(
        "Usted juro venganza por ella con tan solo 7 años de edad , algo que nadie se tomaba en serio , ya que veian al ogro como un ser indestructible")
    input("Ahora usted joven tiene la oportunidad de cobrar la venganza si le pone ganas y ambicion")
    COMIENZO = input("Desea usted luchar por su madre (si/no): ").lower()
    if COMIENZO == "si":
        input("Al comienzo de esta historia usted se encuentra en el pueblo de este hermoso reino , Vananhail")
        input("Cuando usted este en el pueblo siempre podra elegir varias opciones donde puede ir: ")
        input("Usted tendra un inventario que podra abrir denominado mochila , donde tendra sus diferentes utiles")
        input(
            "Tienda del pueblo : Aqui podra comprar cuando recaude monedas las armas que le acompañaran el el viaje y los utensilios principales")
        input(
            "Alcantarillado: Lugar lleno de ratas gigantes donde podra entrenar con un infinito numero de estas y conseguir monedas para la tienda")
        input(
            "Cueva de goblins: Lugar peligroso , donde se encontrara con una cueva llena de goblins donde podra encontrar monedas , conseguir experiencia y si tiene suerte armas de estos odiosos seres")
        input(
            "EL OGRO : BOSS FINAL al que se debe ir preparado , es el terror del reino y si consigues acabar con el , se terminara el miedo y el terror que llena este lugar")
        input("El hechicero, cuando tenga la experiencia suficiente , el le hara magia para que se le agreguen cualidades")

    else:
        print("No le verguenza , tira y lucha por tu madre carajo" )






























def creacion_basica():
    print("Bienvenido a goblin slayer")
    nombre=input("Diganos su nombre de personaje: ")
    print("Perfecto ", nombre ,"un placer tenerle aquí")
    sexo=input("Que sexo es su personaje: Hombre, mujer o no identifica ")
    print("Prosigamos")
    edad=int(input("¿Cual es su edad?: "))
    if edad < 18:
        print("Un pequeño guerrero con gran valor, excelente")
    else:
        print("Un gran guerrero hecho y derecho, excelente")

#creacion_basica()


def cualidades_personaje(Fuerza, Constitucion, Destreza, puntos,Vida_personaje):
    print("Al comienzo de este viaje su personaje tiene 10 puntos en sus tres habilidades principales")
    print("Las cuales son: Fuerza, Destreza y Constitución")
    print(
        "El jefe del pueblo quiere compensar tu valentía con tres puntos más, los cuales puedes dar a cualquier habilidad")
    while puntos > 0:

        habilidad = input("¿A qué habilidad quieres asignarle un punto? ")
        if habilidad == "Fuerza":
            Fuerza = Fuerza + 1
            puntos -= 1
            print("Ahora tiene ", Fuerza, " puntos de fuerza")
        elif habilidad == "Destreza":
            Destreza = Destreza+  1
            puntos -= 1
            print("Ahora mismo tiene ", Destreza, "puntos de destreza")
        elif habilidad == "Constitucion":
            Constitucion= Constitucion+ 1
            Vida_personaje= Vida_personaje
            puntos -= 1
            print("Ahora tiene ", Constitucion, "puntos de constitución")
        else:
            print("Se ha equivocado intentelo de nuevo")

    else:
        print("Ya ha gastado todos los puntos que tenia , ahora eres algo más fuerte que antes")
        return Fuerza,Constitucion,Destreza,puntos,Vida_personaje

#Fuerza,Constitucion,Destreza,puntos,Vida_personaje=cualidades_personaje(Fuerza, Constitucion, Destreza, puntos,Vida_personaje)

def pueblo(Vida_personaje,Constitucion,Donde_ir,experiencia_personaje):
    Vida_personaje=20 + ((Constitucion-10)*2)
    Donde_ir=" "
    print("Bienvenido Guerrero")
    input("¿Como le va?")
    print("Le informamos que usted tiene un total de ", experiencia_personaje , " puntos de experiencia actualmente")
    print("Usted puede ir a numerosos lugares desde aqui")
    print("1: Tienda , 2:Alcantarillado , 3:Cueva de goblins, 4:OGRO, 5:Hechicero, 6:Un punto mas")
    Lugar_donde_ir = " "
    while Lugar_donde_ir != "else":
        Lugar_donde_ir = input("Donde quiere ir : ")
        if Lugar_donde_ir == "1":
            print("Perfecto, vamos a comprar algunos objetos")
            Donde_ir= "tienda"
            return Vida_personaje,Donde_ir,experiencia_personaje
        elif Lugar_donde_ir == "2":
            print("No se diga más , a entrenar!!!")
            Donde_ir="alcantarillado"
            return Vida_personaje,Donde_ir,experiencia_personaje
        elif Lugar_donde_ir == "3":
            print("Tenga, cuidado. Vamos a por esos bichejos verdes")
            Donde_ir="cueva de goblins"
            return Vida_personaje,Donde_ir,experiencia_personaje
        elif Lugar_donde_ir == "4":
            print("Mucha suerte compañero , le deseo mucha suerte y que cumpla con su cometido")
            Donde_ir= "ogro"
            return Vida_personaje,Donde_ir,experiencia_personaje
        elif Lugar_donde_ir == "5":
            Donde_ir= "hechicero"
            return Vida_personaje,Donde_ir,experiencia_personaje
        elif Lugar_donde_ir == "6":
            Donde_ir="tengo un punto mas"
            return Vida_personaje,Donde_ir,experiencia_personaje
        else:
            print("Se ha equivocado de lugar señorito")
            continue

#Vida_personaje,Donde_ir=pueblo(Vida_personaje,Donde_ir)




def tienda(monedas_totales, mochila):
    monedas_espada = 10
    monedas_pocion = 20
    monedas_escudo = 0
    monedas_armadura = 30
    monedas_hacha_a_dos_manos = 30
    monedas_espada_magica = 200
    print("Bienvenido de nuevo a la tienda de Charly")
    print("Tenemos numerosos utensilios que le pueden ser de ayuda")

    while True:

        util = int(input(
            "Pulse 1 = pocion de vida. Pulse 2 = Espada. Pulse 3 = Escudo. Pulse 4 = Armadura. Pulse 5 = Hacha a dos manos. Pulse 6 = Espada magíca: "))
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
            return monedas_totales, mochila

#monedas_totales,mochila= tienda(monedas_totales, mochila)

#monedas_totales, mochila = tienda(monedas_totales, mochila)






def subir_experencia(experiencia_personaje,Vida_personaje,puntos):

    if experiencia_personaje >= 250 and experiencia_personaje <=500:
        print("Usted a subido de nivel , enhorabuena esta haciendose un guerrero mas fuerte, su calificación actual es de AFICIONADO")
        print("Como recompensa se lanzara un dado para ver cuantos puntos de vida se le suman a su personaje")
        dado_experiencia = random.randint(1, 8)
        Vida_personaje+=dado_experiencia
        print("Ahora tiene un total de ", Vida_personaje, " puntos der vida")
        return Vida_personaje, experiencia_personaje, puntos
    elif experiencia_personaje > 500 and experiencia_personaje <=1000:
        print("Enhorabuena maestro , usted esta subiendo de nivel , ahora su calificación es MAESTRO")
        print("Como recompensa se lanzaran los dados para ver cuantos puntos de vida sube ")
        dado_experiencia=random.randint(1,8)
        Vida_personaje += dado_experiencia
        print("Ahora tiene un total de ", Vida_personaje, " puntos der vida")

        return Vida_personaje, experiencia_personaje, puntos
    elif experiencia_personaje > 1000:
        print("Impresionante, usted a conseguido lograr el range de JEFE ALDEA")
        print("Como recompensa se lanzara un dado para ver cuanta vida se le añadira a tu persoanje")
        dado_experiencia=random.randint(1,8)
        Vida_personaje+=dado_experiencia
        print("Ahora tiene un total de ", Vida_personaje, " puntos der vida")
        input("Ademas por llegar al nivel de jefe de la aldea se le dara un punto mas para añadirlo a tus cualidades generales")
        puntos+=1


        return Vida_personaje,experiencia_personaje,puntos


    else:
        print("No tiene suficiente experencia para subir de nivel")

#experiencia_personaje,Vida_personaje,puntos=subir_experencia(experiencia_personaje,Vida_personaje,puntos)






def cueva_goblins(Vida_personaje, experiencia_personaje,mochila,recibir_dano,dano_ataque,Fuerza):
    print("Acaba de llegar a la cueva de los goblins")
    numero_goblins_totales = random.randint(1, 6)
    numero_goblins_escudo = random.randint(1, numero_goblins_totales)
    numero_goblins_espada = numero_goblins_totales - numero_goblins_escudo
    print("El numero de goblins con espada en esta cueva es de ", numero_goblins_espada)
    print("El numero de goblins con escudo en esta cueva es de ", numero_goblins_escudo)
    print("El numero total de goblins es ", numero_goblins_totales) #GOBLINS ALEATORIOS

    cuestion_huida_goblins_1=input("Quiere abandonar la cueva (si/no): ") #COMIENZO HUIDA 1
    if cuestion_huida_goblins_1 == "si":
        dado_goblin_huida_1=random.randint(1,20)
        print("Para poder huir tiene que sacar un dado de 5 o mayor sobre 20")
        print("Usted ha sacado un ", dado_goblin_huida_1)
        if dado_goblin_huida_1 >= 5:
            print("Usted puede huir")
            return Vida_personaje,experiencia_personaje,mochila,recibir_dano,dano_ataque
        else:
            print("Usted no puede huir",)
            while numero_goblins_totales > 0:
                print("Acaba de aparecer el primer goblin")

                cuestion_huida_goblin2 = input("Desea usted huir (si/no): ")  # CUESTION DE HUIDA 2 EN CASO VALIENTE
                if cuestion_huida_goblin2 == "si":
                    huida_goblins = 10
                    huida_total_goblins = huida_goblins + numero_goblins_totales
                    dado_huida_total = random.randint(1, 20)
                    print("Debe sacar un total de ", huida_total_goblins)
                    print("Usted a sacado un ", dado_huida_total)
                    if dado_huida_total >= huida_total_goblins:
                        input ("Usted puede huir")
                        return Vida_personaje,experiencia_personaje,mochila,recibir_dano,dano_ataque
                    else:
                        print ("Usted debera de continuar luchando")
                        eleccion_goblin = int(input("Que goblin desea escoger (espada:1/escudo:2): "))
                        if eleccion_goblin == 1:

                            while numero_goblins_espada > 0:
                                vida_goblin_espada = random.randint(1, 8)
                                while vida_goblin_espada > 0:

                                    dano_ataque_goblin_espada = random.randint(1, 8)
                                    ataque_impacto_humano_goblin = random.randint(1, 20)
                                    ataque_humano = random.randint(1,dano_ataque) + (Fuerza - 10)
                                    dad_ataque_goblin_humano = random.randint(1, 20)
                                    input("Tu turno humano vayamos con todo (Lanza el dado)")
                                    print("Usted a sacado un ", ataque_impacto_humano_goblin)
                                    if ataque_impacto_humano_goblin >= 12 :
                                        print("Has conseguido acertarle el daño sera de ", ataque_humano)
                                        vida_goblin_espada -= ataque_humano
                                        if vida_goblin_espada > 0:
                                            input(
                                                "El goblin aun sigue con vida , por lo que ahora es su turno de atacarle")
                                            print("El goblin a sacado un ", dad_ataque_goblin_humano)
                                            if dad_ataque_goblin_humano >= 12 + recibir_dano:
                                                print("El goblin le ha alcanzado")
                                                Vida_personaje = Vida_personaje - dano_ataque_goblin_espada
                                                print("Su vida restante es de ", Vida_personaje)
                                                if Vida_personaje > 0:
                                                    continue
                                                else:
                                                    print("Usted a muerto en combate")
                                                    return Vida_personaje, experiencia_personaje, mochila, recibir_dano, dano_ataque




                                            else:
                                                input("El goblin no ha conseguido alcanzarle")
                                        else:
                                            print("El goblin a muerto")
                                            experiencia_personaje = experiencia_personaje + 20
                                            print("Su experiencia actual es de ", experiencia_personaje)
                                            input("Veamos si le ha dado su espada")
                                            porcentaje_espada_goblin = random.randint(1, 100)
                                            if porcentaje_espada_goblin <= 20:
                                                print(
                                                    "El golblin a soltado su espada enhorabuena")  # AÑADIDO DE ESPADA GOBLIN A MOCHILA
                                                mochila.append("espada goblin")


                                            else:
                                                print("No ha tenido suerte , no se le ha caido su espada")
                                            numero_goblins_espada = numero_goblins_espada - 1
                                            numero_goblins_totales -= 1
                                            print("Quedan ", numero_goblins_espada, " goblins con espada")
                                    else:
                                        print("Usted a fallado el ataque")
                                        input("Ahora es turno del goblin")
                                        print("El goblin a sacado un ", dad_ataque_goblin_humano)
                                        if dad_ataque_goblin_humano >= 12 + recibir_dano:
                                            print("El goblin le ha alcanzado")
                                            print("Usted a recibido un daño de ", dano_ataque_goblin_espada)
                                            Vida_personaje = Vida_personaje - dano_ataque_goblin_espada
                                            print("Su vida restante es de ", Vida_personaje)
                                            if Vida_personaje > 0:
                                                continue
                                            else:
                                                print("Usted a muerto en combate")
                                                return Vida_personaje, experiencia_personaje, mochila, recibir_dano, dano_ataque
                                        else:
                                            print("El goblin no ha conseguido alcanzarle")





                                else:

                                    input("Muy bien hecho , uno menos")
                            else:
                                print("All right")





                                # AQUI VA EL DEF COMBATE GOBLIN ESPADA
                        else:

                             while numero_goblins_escudo > 0:
                                 vida_goblin_escudo = random.randint(1, 8)
                                 while vida_goblin_escudo > 0:

                                     dano_ataque_goblin_escudo = random.randint(1, 6)
                                     ataque_impacto_humano_goblin_escudo = random.randint(1, 20)
                                     ataque_humano = random.randint(1,dano_ataque) + (Fuerza - 10)
                                     dad_ataque_goblin_escudo_humano = random.randint(1, 20)
                                     input("Tu turno humano vayamos con todo (Lanza el dado)")
                                     print("Usted a sacado un ", ataque_impacto_humano_goblin_escudo)
                                     if ataque_impacto_humano_goblin_escudo >= 13:
                                         print("Has conseguido acertarle el daño sera de ", ataque_humano)
                                         vida_goblin_escudo -= ataque_humano
                                         if vida_goblin_escudo > 0:
                                             input(
                                                 "El goblin aun sigue con vida , por lo que ahora es su turno de atacarle")
                                             print("El goblin a sacado un ", dad_ataque_goblin_escudo_humano)
                                             if dad_ataque_goblin_escudo_humano >= 12 + recibir_dano:
                                                 print("El goblin le ha alcanzado")
                                                 Vida_personaje = Vida_personaje - dano_ataque_goblin_escudo
                                                 print("Su vida restante es de ", Vida_personaje)
                                                 if Vida_personaje > 0:
                                                     continue
                                                 else:
                                                     print("Usted a muerto en combate")
                                                     return Vida_personaje, experiencia_personaje, mochila, recibir_dano, dano_ataque
                                             else:
                                                 input("El goblin no ha conseguido alcanzarle")
                                         else:
                                             print("El goblin a muerto")
                                             experiencia_personaje = experiencia_personaje + 20
                                             print("Su experiencia total es de ", experiencia_personaje)
                                             input("Veamos si le ha dado su espada")
                                             porcentaje_escudo_goblin = random.randint(1, 100)
                                             if porcentaje_escudo_goblin <= 20:
                                                 print(
                                                     "El golblin a soltado su espada enhorabuena")  # AÑADIDO DE ESCUDO GOBLIN A MOCHILA
                                                 mochila.append("escudo goblin")

                                             else:
                                                 print("No ha tenido suerte , no se le ha caido su espada")
                                             numero_goblins_escudo = numero_goblins_escudo - 1
                                             numero_goblins_totales -= 1
                                             print("Quedan ", numero_goblins_escudo, " goblins con espada")
                                     else:
                                         print("Usted a fallado el ataque")
                                         input("Ahora es turno del goblin")
                                         print("El goblin a sacado un ", dad_ataque_goblin_escudo_humano)
                                         if dad_ataque_goblin_escudo_humano >= 12 + recibir_dano:
                                             print("El goblin le ha alcanzado")
                                             print("Usted a recibido un daño de ", dano_ataque_goblin_escudo)
                                             Vida_personaje = Vida_personaje - dano_ataque_goblin_escudo
                                             print("Su vida restante es de ", Vida_personaje)
                                             if Vida_personaje > 0:
                                                 continue
                                             else:
                                                 print("Usted a muerto en combate")
                                                 return Vida_personaje, experiencia_personaje, mochila, recibir_dano, dano_ataque
                                         else:
                                             print("El goblin no ha conseguido alcanzarle")





                                 else:

                                     input("Muy bien hecho , uno menos")
                             else:
                                 print("All right")

                else:
                    print("Usted caballero luchara contra el goblin")
                    eleccion_goblin=int(input("Que goblin desea escoger (espada:1/escudo:2): "))
                    if eleccion_goblin == 1:

                        while numero_goblins_espada > 0:
                            vida_goblin_espada = random.randint(1, 8)
                            while vida_goblin_espada > 0:

                                dano_ataque_goblin_espada = random.randint(1, 8)
                                ataque_impacto_humano_goblin = random.randint(1, 20)
                                ataque_humano = random.randint(1,dano_ataque) + (Fuerza - 10)
                                dad_ataque_goblin_humano = random.randint(1, 20)
                                input("Tu turno humano vayamos con todo (Lanza el dado)")
                                print("Usted a sacado un ", ataque_impacto_humano_goblin)
                                if ataque_impacto_humano_goblin >= 12:
                                    print("Has conseguido acertarle el daño sera de ", ataque_humano)
                                    vida_goblin_espada -= ataque_humano
                                    if vida_goblin_espada > 0:
                                        input(
                                            "El goblin aun sigue con vida , por lo que ahora es su turno de atacarle")
                                        print("El goblin a sacado un ", dad_ataque_goblin_humano)
                                        if dad_ataque_goblin_humano >= 12 + recibir_dano:
                                            input("El goblin le ha alcanzado")
                                            Vida_personaje = Vida_personaje - dano_ataque_goblin_espada
                                            print("Su vida restante es de ", Vida_personaje)
                                            if Vida_personaje > 0:
                                                continue
                                            else:
                                                print("Usted a muerto en combate")
                                                return Vida_personaje, experiencia_personaje, mochila, recibir_dano, dano_ataque
                                        else:
                                            print("El goblin no ha conseguido alcanzarle")
                                    else:
                                        print("El goblin a muerto")
                                        experiencia_personaje = experiencia_personaje + 20
                                        print("Su experiencia actual es de ", experiencia_personaje)
                                        input("Veamos si le ha dado su espada")
                                        porcentaje_espada_goblin = random.randint(1, 100)
                                        if porcentaje_espada_goblin <= 20:
                                            print(
                                                "El golblin a soltado su espada enhorabuena")  # AÑADIDO DE ESPADA GOBLIN A MOCHILA
                                            mochila.append("espada goblin")


                                        else:
                                            print("No ha tenido suerte , no se le ha caido su espada")
                                        numero_goblins_espada = numero_goblins_espada - 1
                                        numero_goblins_totales -= 1
                                        print("Quedan ", numero_goblins_espada, " goblins con espada")
                                else:
                                    print("Usted a fallado el ataque")
                                    input("Ahora es turno del goblin")
                                    print("El goblin a sacado un ", dad_ataque_goblin_humano)
                                    if dad_ataque_goblin_humano >= 12 + recibir_dano:
                                        print("El goblin le ha alcanzado")
                                        print("Usted a recibido un daño de ", dano_ataque_goblin_espada)
                                        Vida_personaje = Vida_personaje - dano_ataque_goblin_espada
                                        print("Su vida restante es de ", Vida_personaje)
                                        if Vida_personaje > 0:
                                            continue
                                        else:
                                            print("Usted a muerto en combate")
                                            return Vida_personaje, experiencia_personaje, mochila, recibir_dano , dano_ataque
                                    else:
                                        print("El goblin no ha conseguido alcanzarle")





                            else:

                                input("Muy bien hecho , uno menos")
                        else:
                            print("All right")

                    else:

                        while numero_goblins_escudo > 0:
                            vida_goblin_escudo = random.randint(1, 8)
                            while vida_goblin_escudo > 0:

                                dano_ataque_goblin_escudo = random.randint(1, 6)
                                ataque_impacto_humano_goblin_escudo = random.randint(1, 20)
                                ataque_humano = random.randint(1,dano_ataque) + (Fuerza - 10)
                                dad_ataque_goblin_escudo_humano = random.randint(1, 20)
                                input("Tu turno humano vayamos con todo (Lanza el dado)")
                                print("Usted a sacado un ", ataque_impacto_humano_goblin_escudo)
                                if ataque_impacto_humano_goblin_escudo >= 13:
                                    print("Has conseguido acertarle el daño sera de ", ataque_humano)
                                    vida_goblin_escudo -= ataque_humano
                                    if vida_goblin_escudo > 0:
                                        input(
                                            "El goblin aun sigue con vida , por lo que ahora es su turno de atacarle")
                                        print("El goblin a sacado un ", dad_ataque_goblin_escudo_humano)
                                        if dad_ataque_goblin_escudo_humano >= 12 + recibir_dano:
                                            print("El goblin le ha alcanzado")
                                            Vida_personaje = Vida_personaje - dano_ataque_goblin_escudo
                                            print("Su vida restante es de ", Vida_personaje)
                                            if Vida_personaje > 0:
                                                continue
                                            else:
                                                print("Usted a muerto en combate")
                                                return Vida_personaje, experiencia_personaje, mochila, recibir_dano, dano_ataque
                                        else:
                                            print("El goblin no ha conseguido alcanzarle")
                                    else:
                                        print("El goblin a muerto")
                                        experiencia_personaje = experiencia_personaje + 20
                                        print("Su experiencia total es de ", experiencia_personaje)
                                        input("Veamos si le ha dado su espada")
                                        porcentaje_escudo_goblin = random.randint(1, 100)
                                        if porcentaje_escudo_goblin <= 20:
                                            print(
                                                "El golblin a soltado su espada enhorabuena")  # AÑADIDO DE ESCUDO GOBLIN A MOCHILA
                                            mochila.append("escudo goblin")

                                        else:
                                            print("No ha tenido suerte , no se le ha caido su espada")
                                        numero_goblins_espada = numero_goblins_escudo - 1
                                        numero_goblins_totales -= 1
                                        print("Quedan ", numero_goblins_escudo, " goblins con espada")
                                else:
                                    print("Usted a fallado el ataque")
                                    input("Ahora es turno del goblin")
                                    print("El goblin a sacado un ", dad_ataque_goblin_escudo_humano)
                                    if dad_ataque_goblin_escudo_humano >= 12 + recibir_dano:
                                        print("El goblin le ha alcanzado")
                                        print("Usted a recibido un daño de ", dano_ataque_goblin_escudo)
                                        Vida_personaje = Vida_personaje - dano_ataque_goblin_escudo
                                        print("Su vida restante es de ", Vida_personaje)
                                        if Vida_personaje > 0:
                                            continue
                                        else:
                                            print("Usted a muerto en combate")
                                            return Vida_personaje, experiencia_personaje, mochila , recibir_dano, dano_ataque
                                    else:
                                        print("El goblin no ha conseguido alcanzarle")


                            else:

                                input("Muy bien hecho , uno menos")
                        else:
                            print("All right")

            else:
                print("Usted a acabado con todos los goblins de la cueva")
                return Vida_personaje, experiencia_personaje, mochila, recibir_dano, dano_ataque



    elif cuestion_huida_goblins_1 == "no":
        print("Muy valiente por su parte")

        print("Acaba de aparecer un goblin")
        while numero_goblins_totales >0:

            cuestion_huida_goblin2 = input("Desea usted huir (si/no): ") #CUESTION DE HUIDA 2 EN CASO VALIENTE
            if cuestion_huida_goblin2 == "si":
                huida_goblins = 10
                huida_total_goblins = huida_goblins + numero_goblins_totales
                dado_huida_total = random.randint(1, 20)
                print("Debe sacar un total de ", huida_total_goblins)
                print("Usted a sacado un ", dado_huida_total)
                if dado_huida_total >= huida_total_goblins:
                    print ("Usted puede huir")
                    return Vida_personaje, experiencia_personaje, mochila, recibir_dano , dano_ataque
                else:
                    print ("Usted debera de continuar luchando")
                    eleccion_goblin=int(input("Que goblin desea escoger (espada:1/escudo:2): "))
                    if eleccion_goblin == 1:

                        while numero_goblins_espada > 0:
                            vida_goblin_espada = random.randint(1, 8)
                            while vida_goblin_espada > 0:

                                dano_ataque_goblin_espada = random.randint(1, 8)
                                ataque_impacto_humano_goblin = random.randint(1, 20)
                                ataque_humano = random.randint(1,dano_ataque) + (Fuerza - 10)
                                dad_ataque_goblin_humano = random.randint(1, 20)
                                input("Tu turno humano vayamos con todo (Lanza el dado)")
                                print("Usted a sacado un ", ataque_impacto_humano_goblin)
                                if ataque_impacto_humano_goblin >= 12:
                                    print("Has conseguido acertarle el daño sera de ", ataque_humano)
                                    vida_goblin_espada -= ataque_humano
                                    if vida_goblin_espada > 0:
                                        input(
                                            "El goblin aun sigue con vida , por lo que ahora es su turno de atacarle")
                                        print("El goblin a sacado un ", dad_ataque_goblin_humano)
                                        if dad_ataque_goblin_humano >= 12 + recibir_dano:
                                            print("El goblin le ha alcanzado")
                                            Vida_personaje = Vida_personaje - dano_ataque_goblin_espada
                                            print("Su vida restante es de ", Vida_personaje)
                                            if Vida_personaje > 0:
                                                continue
                                            else:
                                                print("Usted a muerto en combate")
                                                return Vida_personaje, experiencia_personaje, mochila, recibir_dano, dano_ataque
                                        else:
                                            print("El goblin no ha conseguido alcanzarle")
                                    else:
                                        print("El goblin a muerto")
                                        experiencia_personaje = experiencia_personaje + 20
                                        print("Su experiencia actual es de ", experiencia_personaje)
                                        input("Veamos si le ha dado su espada")
                                        porcentaje_espada_goblin = random.randint(1, 100)
                                        if porcentaje_espada_goblin <= 20:
                                            print(
                                                "El golblin a soltado su espada enhorabuena")  # AÑADIDO DE ESPADA GOBLIN A MOCHILA
                                            mochila.append("espada goblin")


                                        else:
                                            print("No ha tenido suerte , no se le ha caido su espada")
                                        numero_goblins_espada = numero_goblins_espada - 1
                                        numero_goblins_totales -= 1
                                        print("Quedan ", numero_goblins_espada, " goblins con espada")
                                else:
                                    print("Usted a fallado el ataque")
                                    input("Ahora es turno del goblin")
                                    print("El goblin a sacado un ", dad_ataque_goblin_humano)
                                    if dad_ataque_goblin_humano >= 12 + recibir_dano:
                                        print("El goblin le ha alcanzado")
                                        print("Usted a recibido un daño de ", dano_ataque_goblin_espada)
                                        Vida_personaje = Vida_personaje - dano_ataque_goblin_espada
                                        print("Su vida restante es de ", Vida_personaje)
                                        if Vida_personaje > 0:
                                            continue
                                        else:
                                            print("Usted a muerto en combate")
                                            return Vida_personaje, experiencia_personaje, mochila, recibir_dano , dano_ataque
                                    else:
                                        print("El goblin no ha conseguido alcanzarle")





                            else:

                                input("Muy bien hecho , uno menos")
                        else:
                            print("All right")





                            #AQUI VA EL DEF COMBATE GOBLIN ESPADA
                    else:

                        while numero_goblins_escudo > 0:
                            vida_goblin_escudo = random.randint(1, 8)
                            while vida_goblin_escudo > 0:

                                dano_ataque_goblin_escudo = random.randint(1, 6)
                                ataque_impacto_humano_goblin_escudo = random.randint(1, 20)
                                ataque_humano = random.randint(1,dano_ataque) + (Fuerza - 10)
                                dad_ataque_goblin_escudo_humano = random.randint(1, 20)
                                input("Tu turno humano vayamos con todo (Lanza el dado)")
                                print("Usted a sacado un ", ataque_impacto_humano_goblin_escudo)
                                if ataque_impacto_humano_goblin_escudo >= 13:
                                    print("Has conseguido acertarle el daño sera de ", ataque_humano)
                                    vida_goblin_escudo -= ataque_humano
                                    if vida_goblin_escudo > 0:
                                        input(
                                            "El goblin aun sigue con vida , por lo que ahora es su turno de atacarle")
                                        print("El goblin a sacado un ", dad_ataque_goblin_escudo_humano)
                                        if dad_ataque_goblin_escudo_humano >= 12 + recibir_dano:
                                            print("El goblin le ha alcanzado")
                                            Vida_personaje = Vida_personaje - dano_ataque_goblin_escudo
                                            print("Su vida restante es de ", Vida_personaje)
                                            if Vida_personaje > 0:
                                                continue
                                            else:
                                                print("Usted a muerto en combate")
                                                return Vida_personaje, experiencia_personaje, mochila, recibir_dano , dano_ataque
                                        else:
                                            print("El goblin no ha conseguido alcanzarle")
                                    else:
                                        print("El goblin a muerto")
                                        experiencia_personaje = experiencia_personaje + 20
                                        print("Su experiencia total es de ", experiencia_personaje)
                                        input("Veamos si le ha dado su espada")
                                        porcentaje_escudo_goblin = random.randint(1, 100)
                                        if porcentaje_escudo_goblin <= 20:
                                            print(
                                                "El golblin a soltado su espada enhorabuena")  # AÑADIDO DE ESCUDO GOBLIN A MOCHILA
                                            mochila.append("escudo goblin")

                                        else:
                                            print("No ha tenido suerte , no se le ha caido su espada")
                                        numero_goblins_escudo = numero_goblins_escudo - 1 ###################3
                                        numero_goblins_totales -= 1
                                        print("Quedan ", numero_goblins_escudo, " goblins con espada")
                                else:
                                    print("Usted a fallado el ataque")
                                    input("Ahora es turno del goblin")
                                    print("El goblin a sacado un ", dad_ataque_goblin_escudo_humano)
                                    if dad_ataque_goblin_escudo_humano >= 12 + recibir_dano:
                                        print("El goblin le ha alcanzado")
                                        print("Usted a recibido un daño de ", dano_ataque_goblin_escudo)
                                        Vida_personaje = Vida_personaje - dano_ataque_goblin_escudo
                                        print("Su vida restante es de ", Vida_personaje)
                                        if Vida_personaje > 0:
                                            continue
                                        else:
                                            print("Usted a muerto en combate")
                                            return Vida_personaje, experiencia_personaje, mochila, recibir_dano, dano_ataque
                                    else:
                                        print("El goblin no ha conseguido alcanzarle")





                            else:

                                input("Muy bien hecho , uno menos")
                        else:
                            print("All right")





                            #AQUI VA EL DEF COMBATE GOBLIN ESCUDO






            else:
                print("Muy bien caballero a enfrentarse al primer goblin")
                eleccion_goblin=int(input("Que goblin desea escoger (espada:1/escudo:2): "))
                if eleccion_goblin == 1:

                    while numero_goblins_espada > 0:
                        vida_goblin_espada = random.randint(1, 8)
                        while vida_goblin_espada > 0:

                            dano_ataque_goblin_espada = random.randint(1, 8)
                            ataque_impacto_humano_goblin = random.randint(1, 20)
                            ataque_humano = random.randint(1,dano_ataque) + (Fuerza - 10)
                            dad_ataque_goblin_humano = random.randint(1, 20)
                            input("Tu turno humano vayamos con todo (Lanza el dado)")
                            print("Usted a sacado un ", ataque_impacto_humano_goblin)
                            if ataque_impacto_humano_goblin >= 12:
                                print("Has conseguido acertarle el daño sera de ", ataque_humano)
                                vida_goblin_espada -= ataque_humano
                                if vida_goblin_espada > 0:
                                    input("El goblin aun sigue con vida , por lo que ahora es su turno de atacarle")
                                    print("El goblin a sacado un ", dad_ataque_goblin_humano)
                                    if dad_ataque_goblin_humano >= 12 + recibir_dano:
                                        print("El goblin le ha alcanzado")
                                        Vida_personaje = Vida_personaje - dano_ataque_goblin_espada
                                        print("Su vida restante es de ", Vida_personaje)
                                        if Vida_personaje > 0:
                                            continue
                                        else:
                                            print("Usted a muerto en combate")
                                            return Vida_personaje, experiencia_personaje, mochila, recibir_dano, dano_ataque
                                    else:
                                        print("El goblin no ha conseguido alcanzarle")
                                else:
                                    print("El goblin a muerto")
                                    experiencia_personaje = experiencia_personaje + 20
                                    print("Su experiencia actual es de ", experiencia_personaje)
                                    input("Veamos si le ha dado su espada")
                                    porcentaje_espada_goblin = random.randint(1, 100)
                                    if porcentaje_espada_goblin <= 20:
                                        print(
                                            "El golblin a soltado su espada enhorabuena")  # AÑADIDO DE ESPADA GOBLIN A MOCHILA
                                        mochila.append("espada goblin")


                                    else:
                                        print("No ha tenido suerte , no se le ha caido su espada")
                                    numero_goblins_espada = numero_goblins_espada - 1
                                    numero_goblins_totales -= 1
                                    print("Quedan ", numero_goblins_espada, " goblins con espada")
                            else:
                                print("Usted a fallado el ataque")
                                input("Ahora es turno del goblin")
                                print("El goblin a sacado un ", dad_ataque_goblin_humano)
                                if dad_ataque_goblin_humano >= 12 + recibir_dano:
                                    print("El goblin le ha alcanzado")
                                    print("Usted a recibido un daño de ", dano_ataque_goblin_espada)
                                    Vida_personaje = Vida_personaje - dano_ataque_goblin_espada
                                    print("Su vida restante es de ", Vida_personaje)
                                    if Vida_personaje > 0:
                                        continue
                                    else:
                                        print("Usted a muerto en combate")
                                        return Vida_personaje, experiencia_personaje, mochila, recibir_dano ,dano_ataque
                                else:
                                    print("El goblin no ha conseguido alcanzarle")





                        else:

                            input("Muy bien hecho , uno menos")
                    else:
                        input("All right")




                       #AQUI VA EL DEF COMBATE GOBLIN ESPADA
                else:

                    while numero_goblins_escudo > 0:
                        vida_goblin_escudo = random.randint(1, 8)
                        while vida_goblin_escudo > 0:

                            dano_ataque_goblin_escudo = random.randint(1, 6)
                            ataque_impacto_humano_goblin_escudo = random.randint(1, 20)
                            ataque_humano = random.randint(1,dano_ataque) + (Fuerza - 10)
                            dad_ataque_goblin_escudo_humano = random.randint(1, 20)
                            input("Tu turno humano vayamos con todo (Lanza el dado)")
                            print("Usted a sacado un ", ataque_impacto_humano_goblin_escudo)
                            if ataque_impacto_humano_goblin_escudo >= 13:
                                print("Has conseguido acertarle el daño sera de ", ataque_humano)
                                vida_goblin_escudo -= ataque_humano
                                if vida_goblin_escudo > 0:
                                    input("El goblin aun sigue con vida , por lo que ahora es su turno de atacarle")
                                    print("El goblin a sacado un ", dad_ataque_goblin_escudo_humano)
                                    if dad_ataque_goblin_escudo_humano >= 12 + recibir_dano:
                                        print("El goblin le ha alcanzado")
                                        Vida_personaje = Vida_personaje - dano_ataque_goblin_escudo
                                        print("Su vida restante es de ", Vida_personaje)
                                        if Vida_personaje > 0:
                                            continue
                                        else:
                                            print("Usted a muerto en combate")
                                            return Vida_personaje, experiencia_personaje, mochila, recibir_dano, dano_ataque
                                    else:
                                        print("El goblin no ha conseguido alcanzarle")
                                else:
                                    print("El goblin a muerto")
                                    experiencia_personaje = experiencia_personaje + 20
                                    print("Su experiencia total es de ", experiencia_personaje)
                                    input("Veamos si le ha dado su espada")
                                    porcentaje_escudo_goblin = random.randint(1, 100)
                                    if porcentaje_escudo_goblin <= 20:
                                        print(
                                            "El golblin a soltado su espada enhorabuena")  # AÑADIDO DE ESCUDO GOBLIN A MOCHILA
                                        mochila.append("escudo goblin")

                                    else:
                                        print("No ha tenido suerte , no se le ha caido su espada")
                                    numero_goblins_escudo = numero_goblins_escudo - 1
                                    numero_goblins_totales -= 1
                                    print("Quedan ", numero_goblins_escudo, " goblins con espada")
                            else:
                                print("Usted a fallado el ataque")
                                input("Ahora es turno del goblin")
                                print("El goblin a sacado un ", dad_ataque_goblin_escudo_humano)
                                if dad_ataque_goblin_escudo_humano >= 12 + recibir_dano:
                                    print("El goblin le ha alcanzado")
                                    print("Usted a recibido un daño de ", dano_ataque_goblin_escudo)
                                    Vida_personaje = Vida_personaje - dano_ataque_goblin_escudo
                                    print("Su vida restante es de ", Vida_personaje)
                                    if Vida_personaje > 0:
                                        continue
                                    else:
                                        print("Usted a muerto en combate")
                                        return Vida_personaje, experiencia_personaje, mochila, recibir_dano , dano_ataque
                                else:
                                    print("El goblin no ha conseguido alcanzarle")





                        else:

                            input("Muy bien hecho , uno menos")
                    else:
                        input("All right")
        else:
            print("Usted a conseguido acabar con todos los goblins de la cueva")
            return Vida_personaje,experiencia_personaje,mochila, recibir_dano, dano_ataque
#Vida_personaje,experiencia_personaje,mochila, recibir_dano, dano_ataque=cueva_goblins(Vida_personaje,experiencia_personaje,mochila, recibir_dano, dano_ataque)













def mochila_personaje(pocion_vida,Vida_personaje,mochila,Utensilio_combate,Utensilio_defensa, dano_ataque, recibir_dano,Fuerza):
    while True:

        print("Usted tiene en la mochila: ", mochila)
        Utensilio_c = input("Que utensilio de ataque quiere utilizar: ")
        Utensilio_d = input("Que utensilio de defensa quiere utilizar: ")
        for i in range(len(mochila)):
            if Utensilio_c == mochila[i]:

                Utensilio_combate = mochila[i]
                if Utensilio_combate == "espada":
                    dano_ataque = 8
                    print("Ha obtenido el siguiente objeto para el combate: ", mochila[i])


                elif Utensilio_combate == "hacha a dos manos":
                    dano_ataque = 12
                    print("Ha obtenido el siguiente objeto para el combate: ", mochila[i])

                elif Utensilio_combate == "espada magica":
                    dano_ataque = 8 + 2
                    print("Ha obtenido el siguiente objeto para el combate: ", mochila[i])

                elif Utensilio_combate == "espada goblin":
                    dano_ataque = 6
                    print("Ha obtenido el siguiente objeto para el combate: ", mochila[i])

                elif Utensilio_combate == "puños":
                    dano_ataque = 4

            else:
                if Utensilio_d == mochila[i]:
                    Utensilio_defensa = mochila[i]

                    if Utensilio_defensa == "escudo goblin":
                        recibir_dano = recibir_dano + 1
                        print("Ha obtenido el siguiente objeto para el combate ", mochila[i])
                    elif Utensilio_defensa == "armadura":
                        recibir_dano = recibir_dano +2
                        print("Ha obtenido el siguiente objeto para el combate ", mochila[i])
                    elif Utensilio_defensa == "pocion de vida":
                        pocion_vida+=1
                        Vida_personaje= Vida_personaje + random.randint(1,6)
                        print("Ahora tiene una vida de ", Vida_personaje)
                        mochila.pop(pocion_vida)
                    elif Utensilio_defensa == "escudo":
                        recibir_dano = recibir_dano + 1
                        print("Ha obtenido el siguiente objeto para el combate: ", mochila[i])


        cuestion_mochila = input("Desea coger mas objetos de la mochila (si/no): ")
        if cuestion_mochila == "si":
            continue
        else:
            print("Se abandona la mochila")
            return pocion_vida,Vida_personaje,mochila,Utensilio_combate,Utensilio_defensa, dano_ataque, recibir_dano,Fuerza

#pocion_vida,Vida_personaje,mochila,Utensilio_combate,Utensilio_defensa,dano_ataque,recibir_dano,Fuerza, = mochila_personaje(pocion_vida,Vida_personaje,mochila, Utensilio_combate, Utensilio_defensa, dano_ataque, recibir_dano, Fuerza )








def combate_rata(Vida_personaje,monedas_totales, recibir_dano, dano_ataque,Fuerza):



    while Vida_personaje > 0:

        print("Se adentra y aparece una rata")
        cuestion_huida_rata = input("¿Desea usted huir?: ").lower()
        if cuestion_huida_rata == "si":
            print("Se procede a lanzar el dado")
            dado_huida_rata = random.randint(1, 20)
            print("Usted a sacado un ", dado_huida_rata)
            if dado_huida_rata >= 8:
                print ("Usted puede huir")
                return Vida_personaje,monedas_totales
            else:
                print("Debe de luchar jefe")
                rata_vida = 4

                while rata_vida > 0:
                    dad0_ataque = random.randint(1, 20)
                    golpe_rata = random.randint(1, 4)

                    dado_golpe_rata = random.randint(1, 20)
                    input("Es su turno de atacarla, lancemos el dado ")
                    if dad0_ataque >= 10:
                        print("Usted a sacado un ", dad0_ataque, " por lo que el daño que le hara a la rata sera de: ")
                        rata_vida = rata_vida - (random.randint(1,dano_ataque) + (Fuerza - 10))
                        print("La vida restante de la rata es ", rata_vida)
                        if rata_vida > 0:
                            input("La dichosa rata aun sigue con vida")
                        else:
                            input("La rata fallecio en combate")
                            numero_moneda_rata = random.randint(1, 100)
                            input("Veamos si has podido conseguir alguna moneda")
                            if numero_moneda_rata <= 40:
                                moneda_aleatoria_rata = random.randint(1, 4)
                                monedas_totales += moneda_aleatoria_rata
                                print("Has conseguido ", moneda_aleatoria_rata, " monedas")
                                print(("Tiene un total de ", monedas_totales, " monedas"))
                            else:
                                print("No ha habido suerte")
                                print("No has podido conseguir ninguna moneda")


                    else:
                        input("Ha fallado su ataque , ahora es turno de la rata")
                        print("La rata a sacado un ", dado_golpe_rata)
                        if dado_golpe_rata >= (12 + recibir_dano):
                            print("La rata a conseguido alcanzarte con un dado de ", dado_golpe_rata)
                            print("Ella le ha hecho un daño de ", golpe_rata, " puntos")
                            Vida_personaje = Vida_personaje - golpe_rata
                            print("Le quedan un total de ", Vida_personaje, " puntos de vida")
                        else:
                            print("La rata no ha conseguido alcanzarte")
                else:
                    print("Usted volvera al poblado")
                    print("Se ha llevado un total de ", monedas_totales, "monedas de oro")
                    return Vida_personaje, monedas_totales , recibir_dano , dano_ataque


        elif cuestion_huida_rata == "no":
                print ("Vamos a por esa rata")
                rata_vida = random.randint(1,4)

                while rata_vida > 0:
                    dad0_ataque = random.randint(1, 20)
                    golpe_rata = random.randint(1, 4)
                    ataque_humano = random.randint(1,dano_ataque) + (Fuerza-10)
                    dado_golpe_rata = random.randint(1, 20)
                    input("Es su turno de atacarla, lancemos el dado ")
                    if dad0_ataque >= 10:
                        print("Usted a sacado un ", dad0_ataque, " por lo que el daño que le hara a la rata sera de: ")
                        print(ataque_humano, " puntos de vida")
                        rata_vida = rata_vida - ataque_humano
                        print("La vida restante de la rata es ", rata_vida)
                        if rata_vida > 0:
                            input("La dichosa rata aun sigue con vida")
                            input("Ha fallado su ataque , ahora es turno de la rata")
                            print("La rata a sacado un ", dado_golpe_rata)
                            if dado_golpe_rata >= (12 + recibir_dano):
                                print("La rata a conseguido alcanzarte con un dado de ", dado_golpe_rata)
                                print("Ella le ha hecho un daño de ", golpe_rata, " puntos")
                                Vida_personaje = Vida_personaje - golpe_rata
                                print("Le quedan un total de ", Vida_personaje, " puntos de vida")
                                if Vida_personaje > 0:
                                    continue
                                else:
                                    break
                            else:
                                print("La rata no ha conseguido alcanzarte")
                        else:
                            input("La rata fallecio en combate")
                            numero_moneda_rata = random.randint(1, 100)
                            input("Veamos si has podido conseguir alguna moneda")
                            if numero_moneda_rata <= 40:
                                moneda_aleatoria_rata = random.randint(1, 4)
                                monedas_totales += moneda_aleatoria_rata
                                print("Has conseguido ", moneda_aleatoria_rata, " monedas")
                                print("Usted tiene un total de ", monedas_totales, " monedas totales")
                            else:
                                print("No ha habido suerte")
                                print("No has podido conseguir ninguna moneda")


                    else:
                        input("Ha fallado su ataque , ahora es turno de la rata")
                        print("La rata a sacado un ", dado_golpe_rata)
                        if dado_golpe_rata >= (12 + recibir_dano):
                            print("La rata a conseguido alcanzarte con un dado de ", dado_golpe_rata)
                            print("Ella le ha hecho un daño de ", golpe_rata, " puntos")
                            Vida_personaje = Vida_personaje - golpe_rata
                            print("Le quedan un total de ", Vida_personaje, " puntos de vida")
                            if Vida_personaje > 0:
                                continue
                            else:
                                break
                        else:
                            print("La rata no ha conseguido alcanzarte")
        else:
            print("Usted volvera al poblado")
            print("Se ha llevado un total de ", monedas_totales, "monedas de oro")
            return Vida_personaje, monedas_totales
    else:
        print("Usted a muerto Game over")
        return Vida_personaje, monedas_totales




#Vida_personaje,monedas_totales,recibir_dano,dano_ataque=combate_rata(Vida_personaje,monedas_totales,recibir_dano,dano_ataque,Fuerza)



def combate_ogro(Vida_personaje,recibir_dano,dano_ataque,monedas_totales,experiencia_personaje,Fuerza):

    Vida_ogro=50

    input("Bienvenido a este monstruoso lugar , donde solo llegan unos pocos.")
    print("Se cierran las compuertas y no hay escapatorio, ahora eres tu contrs el ogro.")
    input("Ogro: Bienvenido muchacho , ¿De verdad quieres enfrentarte a mi?")
    print(" Oh terrible ogro que tiene asustado al reino , no le temo vengo preparado y acabare con tu existencia de una vez por todas")
    input("Ogro: Eso habrá que verlo no dudes en atacarme guerrero")
    input("QUE COMIENCE EL VERDADERO DESAFIO COMPAÑERO")
    while Vida_personaje > 0:

            while Vida_ogro > 0:
                dado_impacto_ogro=random.randint(1,20)
                dado_impacto_humano=random.randint(1,20)
                dano_ogro_humano=random.randint(1,12)+2
                print("Es su turno de atacar , lance el dado: ")
                input("Se procede a lanzar el dado: ")
                print("Usted a sacado un ", dado_impacto_ogro)
                if dado_impacto_ogro >=16:
                    print("Usted a conseguido alcanzar a este ser monstruoso")
                    Vida_ogro = Vida_ogro - (random.randint(1,dano_ataque) + (Fuerza - 10))
                    print("La vida restante del ogro es de ", Vida_ogro)
                    if Vida_ogro >0:
                        input("Ahora es turno del terrible ogro")
                        print("El ogro procede a lanzar su dado: ")
                        if dado_impacto_humano >= 12+recibir_dano:
                            print("El ogro a ha sacado un ", dado_impacto_humano)
                            print("El le ha hecho un daño de ", dano_ogro_humano)
                            Vida_personaje= Vida_personaje - dano_ogro_humano
                            print("A su personaje le queda un total de ", Vida_personaje , " puntos de vida restante")
                            if Vida_personaje > 0:
                                continue
                            else:
                                break
                        else:
                            print("El ogro ha sacado un ", dado_impacto_ogro)
                            input("Este no ha podido alcanzarle")
                            continue
                else:
                    print("No ha poddido alcanzarlo ")
                    if Vida_ogro >0:
                        input("Ahora es turno del terrible ogro")
                        print("El ogro procede a lanzar su dado: ")
                        if dado_impacto_humano >= 12+recibir_dano:
                            print("El ogro a ha sacado un ", dado_impacto_humano)
                            print("El le ha hecho un daño de ", dano_ogro_humano)
                            Vida_personaje= Vida_personaje - dano_ogro_humano
                            print("A su personaje le queda un total de ", Vida_personaje , " puntos de vida restante")
                            if Vida_personaje >0:
                                continue
                            else:
                                break
                        else:
                            print("El ogro ha sacado un ", dado_impacto_ogro)
                            input("Este no ha podido alcanzarle")
                            continue

            else:

                print("Mientras le clava la espada en el corazon , el ogro suplica por su vida")
                print("Ogro: NO PUEDE SER , COMO VOY A MORIR AQUI NOOO")
                input("El ogro es derrribado")
                monedas_totales= monedas_totales + 200
                experiencia_personaje = experiencia_personaje + 500
                print("No me puedo creer que lo haya conseguido, porfin se lo prometi a mi madre y lo cumpli , esto es por ti. Te quiero Mama")
                input("Entre lagrimas , el validoso caballero se dirige hacia ele cofre del ogro y encuentra un botin de 200 monedas de oro")
                print("Agora su personaje consta de ", monedas_totales , " monedas de oro")
                input("Ademas de una  bonificacion de 500 puntos de experiencia")
                print("Ahora su personaje tiene una experiencia total de ", experiencia_personaje)


                print("Finalmente lo conseguiste , ahora puedes ser llamado heroe")

                print("Fin del juego , Creador: Diego Pareja Serrano")
                return Vida_personaje,recibir_dano,dano_ataque,monedas_totales,experiencia_personaje

    else:
        print(
            "Finalmente el ogro acabo con usted y su historia termina aqui , sin poder cumplir su sueño de ser el heroe del reino")
        print("GAME OVER")
        return Vida_personaje, recibir_dano, dano_ataque, monedas_totales, experiencia_personaje

#Vida_personaje,recibir_dano,dano_ataque,monedas_totales,experiencia_personaje= combate_ogro(Vida_personaje, recibir_dano, dano_ataque, monedas_totales, experiencia_personaje)



