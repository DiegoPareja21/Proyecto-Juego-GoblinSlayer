
import random


def monedas_ratas():
    monedas_totales=0

    numero_moneda_rata=random.randint(1,100)
    input("Veamos si has podido conseguir alguna moneda")
    if numero_moneda_rata <=40:
        moneda_aleatoria_rata=random.randint(1,4)
        monedas_totales += numero_moneda_rata
        print("Has conseguido ", moneda_aleatoria_rata, " monedas")
    else:
        print("No ha habido suerte")
        print("No has podido conseguir ninguna moneda")



def huida_rata():
    print("Acaba de aparecer una rata")
    cuestion_huida_rata = input("¿Desea usted huir?: ")
    if cuestion_huida_rata.lower() == "si":
        print("Se procede a lanzar el dado")
        dado_huida_rata = random.randint(1, 20)
        print("Usted a sacado un ", dado_huida_rata)
        if dado_huida_rata >= 8:
            return "Usted puede huir"
        else:
            return "Toca ir a por ella"
    elif cuestion_huida_rata.lower() == "no":
        return "Vamos a por esa rata"


def combate_rata(monedas_totales):
    huida = "Vamos a por esa rata"

    print("Se adentra y aparece una rata")
    personaje_vida= 20 + ((Constitucion - 10) * 2)

    while huida == "Vamos a por esa rata" or huida == "Toca ir a por ella":


        rata_vida = 4
        huida = huida_rata()
        while rata_vida > 0:
            dad0_ataque = random.randint(1, 20)
            golpe_rata = random.randint(1, 4)
            ataque_humano = dano_ataque + (Fuerza - 10 )
            dado_golpe_rata = random.randint(1, 20)
            input("Es su turno de atacarla, lancemos el dado ")
            if dad0_ataque >= 10:
                print("Usted a sacado un ", dad0_ataque, " por lo que el daño que le hara a la rata sera de: ")
                print(ataque_humano, " puntos de vida")
                rata_vida = rata_vida - ataque_humano
                print("La vida restante de la rata es ", rata_vida)
                if rata_vida >0:
                    input("La dichosa rata aun sigue con vida")
                else:
                    input("La rata fallecio en combate")
                    numero_moneda_rata = random.randint(1, 100)
                    input("Veamos si has podido conseguir alguna moneda")
                    if numero_moneda_rata <= 40:
                        moneda_aleatoria_rata = random.randint(1, 4)
                        monedas_totales += numero_moneda_rata
                        print("Has conseguido ", moneda_aleatoria_rata, " monedas")
                    else:
                        print("No ha habido suerte")
                        print("No has podido conseguir ninguna moneda")


            else:
                input("Ha fallado su ataque , ahora es turno de la rata")
                print("La rata a sacado un ", dado_golpe_rata)
                if dado_golpe_rata >= (12 + recibir_dano):
                    print("La rata a conseguido alcanzarte con un dado de ", dado_golpe_rata)
                    print("Ella le ha hecho un daño de ", golpe_rata, " puntos")
                    personaje_vida = personaje_vida - golpe_rata
                    print("Le quedan un total de ", personaje_vida, " puntos de vida")
                else:
                    print("La rata no ha conseguido alcanzarte")
    else:
     print("Usted volvera al poblado")
     print("Se ha llevado un total de ", monedas_totales, "monedas de oro")


monedas_totales=combate_rata(monedas_totales)



def alcantarillado():

    print("Acabas de llegar al  tenebroso alcantarillado")
    input("Aquí encontraras infinitas ratas que puedes combatir")


#Variables
Fuerza=10
Constitucion=10
Destreza=10
puntos=2
monedas_totales=0
mochila=[]
Utensilio_uso=" "
experiencia_personaje=1001
dano_ataque=0+(Fuerza-10)
recibir_dano=0+(Destreza-10)
Vida_personaje=20+((Constitucion-10)*2)
#
## Funcionamiento

combate_rata(monedas_totales)