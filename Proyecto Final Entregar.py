import tkinter as tk 
from tkinter import messagebox
root = tk.Tk()
root.withdraw
def mostrar_alerta():
    messagebox.showinfo("Notificación","Estás listo para esta Aventura")
mostrar_alerta()

"""JUEGO PIEDRA, PAPEL Y TIJERAS"""
# JUEGO PRINCIPAL
import random

def jugar_ronda ():
    opciones = ["piedra", "papel", "tijeras"]
    usuario = input("Elige piedra, papel o tijeras: ").lower()

    while usuario not in opciones:
        usuario = input("Entrada invalida. Por favor ingresa piedra, papel o tijeras: ").lower()

    maquina = random.choice(opciones)

    print(f"Tú elegiste:  {usuario}")
    print(f"La máquina eligió: {maquina}")

    if usuario == maquina:
        print("Tenemos un Empate!!")
        return 0
    elif (usuario == "piedra" and maquina == "tijeras") or \
         (usuario == "papel" and maquina == "piedra") or \
         (usuario == "tijeras" and maquina == "papel"):
         print ("Eres el Ganador!!")
         return 1
    else:
        print("La máquina te ganó!!")
        return -1


""" MARCADOR Y BUCLE HASTA GANAR """

usuario_puntos = 0
maquina_puntos = 0

print ("Comienza la partida!! " \
"El primero que obtena 3 puntos gana")

while usuario_puntos < 3 and maquina_puntos < 3:
    resultado = jugar_ronda()

    if resultado == 1:
        usuario_puntos += 1
    elif resultado == -1:
        maquina_puntos += 1
    
    print(f"Marcador -> Tú {usuario_puntos} | Máquina:{maquina_puntos}")
    print("-" * 40)

if usuario_puntos == 3:
    
    print("Ganaste la partida!!")
else:
   
    print("La máquina ha ganado!!")