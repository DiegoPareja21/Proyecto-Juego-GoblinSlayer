#Cueva de los globlins
import random

Fuerza=10
Constitucion=10
Destreza=10
puntos=2
monedas_totales=0
mochila=[]
Utensilio_uso=" "
experiencia_personaje=1001
dano_ataque=0
recibir_dano=0
Vida_personaje=20+((Constitucion-10)*2)

def combate_goblins_espada(Vida_personaje,experiencia_personaje):                                                            #COMBATE GOBLIN ESPADA

    numero_goblin_espada=2
    numero_goblin_totales=3
    while Vida_personaje>0:
        while numero_goblin_espada >0:
            vida_goblin_espada=random.randint(1,8)
            while vida_goblin_espada>0:

                dano_ataque_goblin_espada=random.randint(1,8)
                ataque_impacto_humano_goblin=random.randint(1,20)
                ataque_humano=dano_ataque + (Fuerza-10+1)
                dad_ataque_goblin_humano=random.randint(1,20)
                print("Tu turno humano vayamos con todo (Lanza el dado)")
                print("Usted a sacado un ", ataque_impacto_humano_goblin)
                if ataque_impacto_humano_goblin >= 12:
                    print("Has conseguido acertarle el daño sera de ", ataque_humano )
                    vida_goblin_espada-=ataque_humano
                    if vida_goblin_espada  >0:
                        print("El goblin aun sigue con vida , por lo que ahora es su turno de atacarle")
                        print("El goblin a sacado un ", dad_ataque_goblin_humano)
                        if dad_ataque_goblin_humano >= 12+recibir_dano:
                            print("El goblin le ha alcanzado")
                            Vida_personaje = Vida_personaje -  dano_ataque_goblin_espada
                            print("Su vida restante es de ", Vida_personaje)
                        else:
                            print("El goblin no ha conseguido alcanzarle")
                    else:
                        print("El goblin a muerto")
                        experiencia_personaje= experiencia_personaje + 20
                        print("Su experiencia actual es de ", experiencia_personaje)
                        print("Veamos si le ha dado su espada")
                        porcentaje_espada_goblin=random.randint(1,100)
                        if porcentaje_espada_goblin <=20:
                            print("El golblin a soltado su espada enhorabuena")         #AÑADIDO DE ESPADA GOBLIN A MOCHILA
                            mochila.append("espada goblin")


                        else:
                            print("No ha tenido suerte , no se le ha caido su espada")
                        numero_goblin_espada= numero_goblin_espada - 1
                        numero_goblin_totales-=1
                        print("Quedan ", numero_goblin_espada, " goblins con espada")
                else:
                    print("Usted a fallado el ataque")
                    print("Ahora es turno del goblin")
                    print("El goblin a sacado un ", dad_ataque_goblin_humano)
                    if dad_ataque_goblin_humano >= 12 + recibir_dano:
                        print("El goblin le ha alcanzado")
                        print("Usted a recibido un daño de ", dano_ataque_goblin_espada)
                        Vida_personaje = Vida_personaje - dano_ataque_goblin_espada
                        print("Su vida restante es de ", Vida_personaje)
                    else:
                        print("El goblin no ha conseguido alcanzarle")





            else:


                print("Muy bien hecho , uno menos")
        else:
            print("All right")
            break

    else:
        print("Usted a muerto game over")
        











def combate_goblins_escudo(Vida_personaje,experiencia_personaje):                                            #COMBATE GOBLIN CON ESCUDO

    numero_goblin_escudo=2
    numero_goblin_totales=3
    while Vida_personaje > 0:
        while numero_goblin_escudo > 0:
            vida_goblin_escudo = random.randint(1, 8)
            while vida_goblin_escudo > 0:

                dano_ataque_goblin_escudo = random.randint(1, 6)
                ataque_impacto_humano_goblin_escudo = random.randint(1, 20)
                ataque_humano = dano_ataque + (Fuerza - 10 + 1)
                dad_ataque_goblin_escudo_humano = random.randint(1, 20)
                print("Tu turno humano vayamos con todo (Lanza el dado)")
                print("Usted a sacado un ", ataque_impacto_humano_goblin_escudo)
                if ataque_impacto_humano_goblin_escudo >= 13:
                    print("Has conseguido acertarle el daño sera de ", ataque_humano)
                    vida_goblin_escudo -= ataque_humano
                    if vida_goblin_escudo > 0:
                        print("El goblin aun sigue con vida , por lo que ahora es su turno de atacarle")
                        print("El goblin a sacado un ", dad_ataque_goblin_escudo_humano)
                        if dad_ataque_goblin_escudo_humano >= 12 + recibir_dano:
                            print("El goblin le ha alcanzado")
                            Vida_personaje = Vida_personaje - dano_ataque_goblin_escudo
                            print("Su vida restante es de ", Vida_personaje)
                        else:
                            print("El goblin no ha conseguido alcanzarle")
                    else:
                        print("El goblin a muerto")
                        experiencia_personaje = experiencia_personaje + 20
                        print("Su experiencia total es de ", experiencia_personaje)
                        print("Veamos si le ha dado su espada")
                        porcentaje_escudo_goblin = random.randint(1, 100)
                        if porcentaje_escudo_goblin <= 20:
                            print("El golblin a soltado su espada enhorabuena")      # AÑADIDO DE ESCUDO GOBLIN A MOCHILA
                            mochila.append("escudo goblin")

                        else:
                            print("No ha tenido suerte , no se le ha caido su espada")
                        numero_goblin_espada = numero_goblin_escudo - 1
                        numero_goblin_totales -= 1
                        print("Quedan ", numero_goblin_espada, " goblins con espada")
                else:
                    print("Usted a fallado el ataque")
                    print("Ahora es turno del goblin")
                    print("El goblin a sacado un ", dad_ataque_goblin_escudo_humano)
                    if dad_ataque_goblin_escudo_humano >= 12 + recibir_dano:
                        print("El goblin le ha alcanzado")
                        print("Usted a recibido un daño de ", dano_ataque_goblin_escudo)
                        Vida_personaje = Vida_personaje - dano_ataque_goblin_escudo
                        print("Su vida restante es de ", Vida_personaje)
                    else:
                        print("El goblin no ha conseguido alcanzarle")





            else:

                print("Muy bien hecho , uno menos")
        else:
            print("All right")
            break

    else:
        print("Usted a muerto game over")





def goblin_aleatorios():
    numero_goblins_totales=random.randint(1,6)
    numero_goblins_escudo = random.randint(1,numero_goblins_totales)
    numero_goblins_espada = numero_goblins_totales - numero_goblins_escudo
    print("El numero de goblins con espada en esta cueva es de ", numero_goblins_espada)
    print("El numero de goblins con escudo en esta cueva es de ", numero_goblins_escudo)
    print("El numero total de goblins es ", numero_goblins_totales)
    return numero_goblins_totales







def cueva_goblins(Vida_personaje, experiencia_personaje):
    print("Acaba de llegar a la cueva de los goblins")
    numero_goblins_totales = random.randint(1, 6)
    numero_goblins_escudo = random.randint(1, numero_goblins_totales)
    numero_goblins_espada = numero_goblins_totales - numero_goblins_escudo
    print("El numero de goblins con espada en esta cueva es de ", numero_goblins_espada)
    print("El numero de goblins con escudo en esta cueva es de ", numero_goblins_escudo)
    print("El numero total de goblins es ", numero_goblins_totales) #GOBLINS ALEATORIOS

    cuestion_huida_goblins_1=input("Esta seguro de que quiere adentrarse en esa cueva (si/no): ") #COMIENZO HUIDA 1
    if cuestion_huida_goblins_1 == "si":
        dado_goblin_huida_1=random.randint(1,20)
        print("Para poder huir tiene que sacar un dado de 5 o mayor sobre 20")
        print("Usted ha sacado un ", dado_goblin_huida_1)
        if dado_goblin_huida_1 >= 5:
            print("Usted puede huir")
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
                        print ("Usted puede huir")
                        break
                    else:
                        print ("Usted debera de continuar luchando")
                        eleccion_goblin = int(input("Que goblin desea escoger (espada:1/escudo:2): "))
                        if eleccion_goblin == 1:
                            while Vida_personaje > 0:
                                while numero_goblins_espada > 0:
                                    vida_goblin_espada = random.randint(1, 8)
                                    while vida_goblin_espada > 0:

                                        dano_ataque_goblin_espada = random.randint(1, 8)
                                        ataque_impacto_humano_goblin = random.randint(1, 20)
                                        ataque_humano = dano_ataque + (Fuerza - 10 + 1)
                                        dad_ataque_goblin_humano = random.randint(1, 20)
                                        print("Tu turno humano vayamos con todo (Lanza el dado)")
                                        print("Usted a sacado un ", ataque_impacto_humano_goblin)
                                        if ataque_impacto_humano_goblin >= 12:
                                            print("Has conseguido acertarle el daño sera de ", ataque_humano)
                                            vida_goblin_espada -= ataque_humano
                                            if vida_goblin_espada > 0:
                                                print(
                                                    "El goblin aun sigue con vida , por lo que ahora es su turno de atacarle")
                                                print("El goblin a sacado un ", dad_ataque_goblin_humano)
                                                if dad_ataque_goblin_humano >= 12 + recibir_dano:
                                                    print("El goblin le ha alcanzado")
                                                    Vida_personaje = Vida_personaje - dano_ataque_goblin_espada
                                                    print("Su vida restante es de ", Vida_personaje)
                                                else:
                                                    print("El goblin no ha conseguido alcanzarle")
                                            else:
                                                print("El goblin a muerto")
                                                experiencia_personaje = experiencia_personaje + 20
                                                print("Su experiencia actual es de ", experiencia_personaje)
                                                print("Veamos si le ha dado su espada")
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
                                            print("Ahora es turno del goblin")
                                            print("El goblin a sacado un ", dad_ataque_goblin_humano)
                                            if dad_ataque_goblin_humano >= 12 + recibir_dano:
                                                print("El goblin le ha alcanzado")
                                                print("Usted a recibido un daño de ", dano_ataque_goblin_espada)
                                                Vida_personaje = Vida_personaje - dano_ataque_goblin_espada
                                                print("Su vida restante es de ", Vida_personaje)
                                            else:
                                                print("El goblin no ha conseguido alcanzarle")





                                    else:

                                        print("Muy bien hecho , uno menos")
                                else:
                                    print("All right")
                                    break

                            else:
                                print("Usted a muerto game over")
                                # AQUI VA EL DEF COMBATE GOBLIN ESPADA
                        else:
                            while Vida_personaje > 0:
                                while numero_goblins_escudo > 0:
                                    vida_goblin_escudo = random.randint(1, 8)
                                    while vida_goblin_escudo > 0:

                                        dano_ataque_goblin_escudo = random.randint(1, 6)
                                        ataque_impacto_humano_goblin_escudo = random.randint(1, 20)
                                        ataque_humano = dano_ataque + (Fuerza - 10 + 1)
                                        dad_ataque_goblin_escudo_humano = random.randint(1, 20)
                                        print("Tu turno humano vayamos con todo (Lanza el dado)")
                                        print("Usted a sacado un ", ataque_impacto_humano_goblin_escudo)
                                        if ataque_impacto_humano_goblin_escudo >= 13:
                                            print("Has conseguido acertarle el daño sera de ", ataque_humano)
                                            vida_goblin_escudo -= ataque_humano
                                            if vida_goblin_escudo > 0:
                                                print(
                                                    "El goblin aun sigue con vida , por lo que ahora es su turno de atacarle")
                                                print("El goblin a sacado un ", dad_ataque_goblin_escudo_humano)
                                                if dad_ataque_goblin_escudo_humano >= 12 + recibir_dano:
                                                    print("El goblin le ha alcanzado")
                                                    Vida_personaje = Vida_personaje - dano_ataque_goblin_escudo
                                                    print("Su vida restante es de ", Vida_personaje)
                                                else:
                                                    print("El goblin no ha conseguido alcanzarle")
                                            else:
                                                print("El goblin a muerto")
                                                experiencia_personaje = experiencia_personaje + 20
                                                print("Su experiencia total es de ", experiencia_personaje)
                                                print("Veamos si le ha dado su espada")
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
                                            print("Ahora es turno del goblin")
                                            print("El goblin a sacado un ", dad_ataque_goblin_escudo_humano)
                                            if dad_ataque_goblin_escudo_humano >= 12 + recibir_dano:
                                                print("El goblin le ha alcanzado")
                                                print("Usted a recibido un daño de ", dano_ataque_goblin_escudo)
                                                Vida_personaje = Vida_personaje - dano_ataque_goblin_escudo
                                                print("Su vida restante es de ", Vida_personaje)
                                            else:
                                                print("El goblin no ha conseguido alcanzarle")





                                    else:

                                        print("Muy bien hecho , uno menos")
                                else:
                                    print("All right")
                                    break

                            else:
                                print("Usted a muerto game over")
                                # AQUI VA EL DEF COMBATE GOBLIN ESCUDO

                else:
                    print("Usted caballero luchara contra el goblin")
                    eleccion_goblin=int(input("Que goblin desea escoger (espada:1/escudo:2): "))
                    if eleccion_goblin == 1:
                        while Vida_personaje > 0:
                            while numero_goblins_espada > 0:
                                vida_goblin_espada = random.randint(1, 8)
                                while vida_goblin_espada > 0:

                                    dano_ataque_goblin_espada = random.randint(1, 8)
                                    ataque_impacto_humano_goblin = random.randint(1, 20)
                                    ataque_humano = dano_ataque + (Fuerza - 10 + 1)
                                    dad_ataque_goblin_humano = random.randint(1, 20)
                                    print("Tu turno humano vayamos con todo (Lanza el dado)")
                                    print("Usted a sacado un ", ataque_impacto_humano_goblin)
                                    if ataque_impacto_humano_goblin >= 12:
                                        print("Has conseguido acertarle el daño sera de ", ataque_humano)
                                        vida_goblin_espada -= ataque_humano
                                        if vida_goblin_espada > 0:
                                            print(
                                                "El goblin aun sigue con vida , por lo que ahora es su turno de atacarle")
                                            print("El goblin a sacado un ", dad_ataque_goblin_humano)
                                            if dad_ataque_goblin_humano >= 12 + recibir_dano:
                                                print("El goblin le ha alcanzado")
                                                Vida_personaje = Vida_personaje - dano_ataque_goblin_espada
                                                print("Su vida restante es de ", Vida_personaje)
                                            else:
                                                print("El goblin no ha conseguido alcanzarle")
                                        else:
                                            print("El goblin a muerto")
                                            experiencia_personaje = experiencia_personaje + 20
                                            print("Su experiencia actual es de ", experiencia_personaje)
                                            print("Veamos si le ha dado su espada")
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
                                        print("Ahora es turno del goblin")
                                        print("El goblin a sacado un ", dad_ataque_goblin_humano)
                                        if dad_ataque_goblin_humano >= 12 + recibir_dano:
                                            print("El goblin le ha alcanzado")
                                            print("Usted a recibido un daño de ", dano_ataque_goblin_espada)
                                            Vida_personaje = Vida_personaje - dano_ataque_goblin_espada
                                            print("Su vida restante es de ", Vida_personaje)
                                        else:
                                            print("El goblin no ha conseguido alcanzarle")





                                else:

                                    print("Muy bien hecho , uno menos")
                            else:
                                print("All right")
                                break

                        else:
                            print("Usted a muerto game over")
                            #AQUI VA EL DEF COMBATE GOBLIN ESPADA
                    else:
                        while Vida_personaje > 0:
                            while numero_goblins_escudo > 0:
                                vida_goblin_escudo = random.randint(1, 8)
                                while vida_goblin_escudo > 0:

                                    dano_ataque_goblin_escudo = random.randint(1, 6)
                                    ataque_impacto_humano_goblin_escudo = random.randint(1, 20)
                                    ataque_humano = dano_ataque + (Fuerza - 10 + 1)
                                    dad_ataque_goblin_escudo_humano = random.randint(1, 20)
                                    print("Tu turno humano vayamos con todo (Lanza el dado)")
                                    print("Usted a sacado un ", ataque_impacto_humano_goblin_escudo)
                                    if ataque_impacto_humano_goblin_escudo >= 13:
                                        print("Has conseguido acertarle el daño sera de ", ataque_humano)
                                        vida_goblin_escudo -= ataque_humano
                                        if vida_goblin_escudo > 0:
                                            print(
                                                "El goblin aun sigue con vida , por lo que ahora es su turno de atacarle")
                                            print("El goblin a sacado un ", dad_ataque_goblin_escudo_humano)
                                            if dad_ataque_goblin_escudo_humano >= 12 + recibir_dano:
                                                print("El goblin le ha alcanzado")
                                                Vida_personaje = Vida_personaje - dano_ataque_goblin_escudo
                                                print("Su vida restante es de ", Vida_personaje)
                                            else:
                                                print("El goblin no ha conseguido alcanzarle")
                                        else:
                                            print("El goblin a muerto")
                                            experiencia_personaje = experiencia_personaje + 20
                                            print("Su experiencia total es de ", experiencia_personaje)
                                            print("Veamos si le ha dado su espada")
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
                                        print("Ahora es turno del goblin")
                                        print("El goblin a sacado un ", dad_ataque_goblin_escudo_humano)
                                        if dad_ataque_goblin_escudo_humano >= 12 + recibir_dano:
                                            print("El goblin le ha alcanzado")
                                            print("Usted a recibido un daño de ", dano_ataque_goblin_escudo)
                                            Vida_personaje = Vida_personaje - dano_ataque_goblin_escudo
                                            print("Su vida restante es de ", Vida_personaje)
                                        else:
                                            print("El goblin no ha conseguido alcanzarle")





                                else:

                                    print("Muy bien hecho , uno menos")
                            else:
                                print("All right")
                                break

                        else:
                            print("Usted a muerto game over")
                            #AQUI VA EL DEF COMBATE GOBLIN ESCUDO

            #Cuestion De Huida 2





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
                    break
                else:
                    print ("Usted debera de continuar luchando")
                    eleccion_goblin=int(input("Que goblin desea escoger (espada:1/escudo:2): "))
                    if eleccion_goblin == 1:
                        while Vida_personaje > 0:
                            while numero_goblins_espada > 0:
                                vida_goblin_espada = random.randint(1, 8)
                                while vida_goblin_espada > 0:

                                    dano_ataque_goblin_espada = random.randint(1, 8)
                                    ataque_impacto_humano_goblin = random.randint(1, 20)
                                    ataque_humano = dano_ataque + (Fuerza - 10 + 1)
                                    dad_ataque_goblin_humano = random.randint(1, 20)
                                    print("Tu turno humano vayamos con todo (Lanza el dado)")
                                    print("Usted a sacado un ", ataque_impacto_humano_goblin)
                                    if ataque_impacto_humano_goblin >= 12:
                                        print("Has conseguido acertarle el daño sera de ", ataque_humano)
                                        vida_goblin_espada -= ataque_humano
                                        if vida_goblin_espada > 0:
                                            print(
                                                "El goblin aun sigue con vida , por lo que ahora es su turno de atacarle")
                                            print("El goblin a sacado un ", dad_ataque_goblin_humano)
                                            if dad_ataque_goblin_humano >= 12 + recibir_dano:
                                                print("El goblin le ha alcanzado")
                                                Vida_personaje = Vida_personaje - dano_ataque_goblin_espada
                                                print("Su vida restante es de ", Vida_personaje)
                                            else:
                                                print("El goblin no ha conseguido alcanzarle")
                                        else:
                                            print("El goblin a muerto")
                                            experiencia_personaje = experiencia_personaje + 20
                                            print("Su experiencia actual es de ", experiencia_personaje)
                                            print("Veamos si le ha dado su espada")
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
                                        print("Ahora es turno del goblin")
                                        print("El goblin a sacado un ", dad_ataque_goblin_humano)
                                        if dad_ataque_goblin_humano >= 12 + recibir_dano:
                                            print("El goblin le ha alcanzado")
                                            print("Usted a recibido un daño de ", dano_ataque_goblin_espada)
                                            Vida_personaje = Vida_personaje - dano_ataque_goblin_espada
                                            print("Su vida restante es de ", Vida_personaje)
                                        else:
                                            print("El goblin no ha conseguido alcanzarle")





                                else:

                                    print("Muy bien hecho , uno menos")
                            else:
                                print("All right")
                                break

                        else:
                            print("Usted a muerto game over")
                            #AQUI VA EL DEF COMBATE GOBLIN ESPADA
                    else:
                        while Vida_personaje > 0:
                            while numero_goblins_escudo > 0:
                                vida_goblin_escudo = random.randint(1, 8)
                                while vida_goblin_escudo > 0:

                                    dano_ataque_goblin_escudo = random.randint(1, 6)
                                    ataque_impacto_humano_goblin_escudo = random.randint(1, 20)
                                    ataque_humano = dano_ataque + (Fuerza - 10 + 1)
                                    dad_ataque_goblin_escudo_humano = random.randint(1, 20)
                                    print("Tu turno humano vayamos con todo (Lanza el dado)")
                                    print("Usted a sacado un ", ataque_impacto_humano_goblin_escudo)
                                    if ataque_impacto_humano_goblin_escudo >= 13:
                                        print("Has conseguido acertarle el daño sera de ", ataque_humano)
                                        vida_goblin_escudo -= ataque_humano
                                        if vida_goblin_escudo > 0:
                                            print(
                                                "El goblin aun sigue con vida , por lo que ahora es su turno de atacarle")
                                            print("El goblin a sacado un ", dad_ataque_goblin_escudo_humano)
                                            if dad_ataque_goblin_escudo_humano >= 12 + recibir_dano:
                                                print("El goblin le ha alcanzado")
                                                Vida_personaje = Vida_personaje - dano_ataque_goblin_escudo
                                                print("Su vida restante es de ", Vida_personaje)
                                            else:
                                                print("El goblin no ha conseguido alcanzarle")
                                        else:
                                            print("El goblin a muerto")
                                            experiencia_personaje = experiencia_personaje + 20
                                            print("Su experiencia total es de ", experiencia_personaje)
                                            print("Veamos si le ha dado su espada")
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
                                        print("Ahora es turno del goblin")
                                        print("El goblin a sacado un ", dad_ataque_goblin_escudo_humano)
                                        if dad_ataque_goblin_escudo_humano >= 12 + recibir_dano:
                                            print("El goblin le ha alcanzado")
                                            print("Usted a recibido un daño de ", dano_ataque_goblin_escudo)
                                            Vida_personaje = Vida_personaje - dano_ataque_goblin_escudo
                                            print("Su vida restante es de ", Vida_personaje)
                                        else:
                                            print("El goblin no ha conseguido alcanzarle")





                                else:

                                    print("Muy bien hecho , uno menos")
                            else:
                                print("All right")
                                break

                        else:
                            print("Usted a muerto game over")
                            #AQUI VA EL DEF COMBATE GOBLIN ESCUDO






            else:
                print("Muy bien caballero a enfrentarse al primer goblin")
                eleccion_goblin=int(input("Que goblin desea escoger (espada:1/escudo:2): "))
                if eleccion_goblin == 1:
                    while Vida_personaje > 0:
                        while numero_goblins_espada > 0:
                            vida_goblin_espada = random.randint(1, 8)
                            while vida_goblin_espada > 0:

                                dano_ataque_goblin_espada = random.randint(1, 8)
                                ataque_impacto_humano_goblin = random.randint(1, 20)
                                ataque_humano = dano_ataque + (Fuerza - 10 + 1)
                                dad_ataque_goblin_humano = random.randint(1, 20)
                                print("Tu turno humano vayamos con todo (Lanza el dado)")
                                print("Usted a sacado un ", ataque_impacto_humano_goblin)
                                if ataque_impacto_humano_goblin >= 12:
                                    print("Has conseguido acertarle el daño sera de ", ataque_humano)
                                    vida_goblin_espada -= ataque_humano
                                    if vida_goblin_espada > 0:
                                        print("El goblin aun sigue con vida , por lo que ahora es su turno de atacarle")
                                        print("El goblin a sacado un ", dad_ataque_goblin_humano)
                                        if dad_ataque_goblin_humano >= 12 + recibir_dano:
                                            print("El goblin le ha alcanzado")
                                            Vida_personaje = Vida_personaje - dano_ataque_goblin_espada
                                            print("Su vida restante es de ", Vida_personaje)
                                        else:
                                            print("El goblin no ha conseguido alcanzarle")
                                    else:
                                        print("El goblin a muerto")
                                        experiencia_personaje = experiencia_personaje + 20
                                        print("Su experiencia actual es de ", experiencia_personaje)
                                        print("Veamos si le ha dado su espada")
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
                                    print("Ahora es turno del goblin")
                                    print("El goblin a sacado un ", dad_ataque_goblin_humano)
                                    if dad_ataque_goblin_humano >= 12 + recibir_dano:
                                        print("El goblin le ha alcanzado")
                                        print("Usted a recibido un daño de ", dano_ataque_goblin_espada)
                                        Vida_personaje = Vida_personaje - dano_ataque_goblin_espada
                                        print("Su vida restante es de ", Vida_personaje)
                                    else:
                                        print("El goblin no ha conseguido alcanzarle")





                            else:

                                print("Muy bien hecho , uno menos")
                        else:
                            print("All right")
                            break

                    else:
                        print("Usted a muerto game over")                         #AQUI VA EL DEF COMBATE GOBLIN ESPADA
                else:
                    while Vida_personaje > 0:
                        while numero_goblins_escudo > 0:
                            vida_goblin_escudo = random.randint(1, 8)
                            while vida_goblin_escudo > 0:

                                dano_ataque_goblin_escudo = random.randint(1, 6)
                                ataque_impacto_humano_goblin_escudo = random.randint(1, 20)
                                ataque_humano = dano_ataque + (Fuerza - 10 + 1)
                                dad_ataque_goblin_escudo_humano = random.randint(1, 20)
                                print("Tu turno humano vayamos con todo (Lanza el dado)")
                                print("Usted a sacado un ", ataque_impacto_humano_goblin_escudo)
                                if ataque_impacto_humano_goblin_escudo >= 13:
                                    print("Has conseguido acertarle el daño sera de ", ataque_humano)
                                    vida_goblin_escudo -= ataque_humano
                                    if vida_goblin_escudo > 0:
                                        print("El goblin aun sigue con vida , por lo que ahora es su turno de atacarle")
                                        print("El goblin a sacado un ", dad_ataque_goblin_escudo_humano)
                                        if dad_ataque_goblin_escudo_humano >= 12 + recibir_dano:
                                            print("El goblin le ha alcanzado")
                                            Vida_personaje = Vida_personaje - dano_ataque_goblin_escudo
                                            print("Su vida restante es de ", Vida_personaje)
                                        else:
                                            print("El goblin no ha conseguido alcanzarle")
                                    else:
                                        print("El goblin a muerto")
                                        experiencia_personaje = experiencia_personaje + 20
                                        print("Su experiencia total es de ", experiencia_personaje)
                                        print("Veamos si le ha dado su espada")
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
                                    print("Ahora es turno del goblin")
                                    print("El goblin a sacado un ", dad_ataque_goblin_escudo_humano)
                                    if dad_ataque_goblin_escudo_humano >= 12 + recibir_dano:
                                        print("El goblin le ha alcanzado")
                                        print("Usted a recibido un daño de ", dano_ataque_goblin_escudo)
                                        Vida_personaje = Vida_personaje - dano_ataque_goblin_escudo
                                        print("Su vida restante es de ", Vida_personaje)
                                    else:
                                        print("El goblin no ha conseguido alcanzarle")





                            else:

                                print("Muy bien hecho , uno menos")
                        else:
                            print("All right")
                            break

                    else:
                        print("Usted a muerto game over")                         #AQUI VA EL DEF COMBATE GOBLIN ESCUDO






cueva_goblins(Vida_personaje,experiencia_personaje)



















