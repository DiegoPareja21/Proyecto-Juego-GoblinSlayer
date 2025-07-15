
import Libreria
Fuerza=10
Constitucion=10
Destreza=10
puntos=3
monedas_totales=0
mochila=["puños"]
Utensilio_combate=" "
Utensilio_defensa=" "
experiencia_personaje=0
dano_ataque=0+(Fuerza-10)
recibir_dano=0+(Destreza-10)
Vida_personaje=20+((Constitucion-10)*2)
Donde_ir=" "
pocion_vida=0




Libreria.creacion_basica()
Libreria.tutorial()
Fuerza,Constitucion,Destreza,puntos,Vida_personaje=Libreria.cualidades_personaje(Fuerza,Constitucion,Destreza,puntos,Vida_personaje)
while Vida_personaje>0:
    Vida_personaje,Donde_ir,experiencia_personaje=Libreria.pueblo(Vida_personaje,Constitucion,Donde_ir,experiencia_personaje)
    if Donde_ir == "tienda":
         monedas_totales, mochila =Libreria.tienda(monedas_totales, mochila)

    elif Donde_ir == "alcantarillado":
        pocion_vida,Vida_personaje,mochila,Utensilio_combate,Utensilio_defensa,dano_ataque,recibir_dano,Fuerza=Libreria.mochila_personaje(pocion_vida,Vida_personaje,mochila,Utensilio_combate,Utensilio_defensa,dano_ataque,recibir_dano,Fuerza)
        Vida_personaje,monedas_totales=Libreria.combate_rata(Vida_personaje,monedas_totales,recibir_dano,dano_ataque,Fuerza)

    elif Donde_ir == "cueva de goblins":
        pocion_vida,Vida_personaje,mochila,Utensilio_combate,Utensilio_defensa,dano_ataque,recibir_dano,Fuerza=Libreria.mochila_personaje(pocion_vida,Vida_personaje,mochila,Utensilio_combate,Utensilio_defensa,dano_ataque,recibir_dano,Fuerza)
        Vida_personaje,experiencia_personaje,mochila,recibir_dano,dano_ataque=Libreria.cueva_goblins(Vida_personaje,experiencia_personaje,mochila,recibir_dano,dano_ataque,Fuerza)

    elif Donde_ir == "ogro":
        pocion_vida,Vida_personaje,mochila,Utensilio_combate,Utensilio_defensa,dano_ataque,recibir_dano,Fuerza=Libreria.mochila_personaje(pocion_vida,Vida_personaje,mochila,Utensilio_combate,Utensilio_defensa,dano_ataque,recibir_dano,Fuerza)
        Vida_personaje,recibir_dano,dano_ataque,monedas_totales,experiencia_personaje=Libreria.combate_ogro(Vida_personaje, recibir_dano, dano_ataque, monedas_totales, experiencia_personaje,Fuerza)

    elif Donde_ir == "hechicero":
        experiencia_personaje,Vida_personaje,puntos=Libreria.subir_experencia(experiencia_personaje,Vida_personaje,puntos)

    elif Donde_ir == "tengo un punto mas":
        Fuerza,Constitucion,Destreza,puntos,Vida_personaje=Libreria.cualidades_personaje(Fuerza,Constitucion,Destreza,puntos,Vida_personaje)










