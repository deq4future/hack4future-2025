import requests
import random

preguntas = []

dinero = 0
reputacion = 50 #sobre 100
felicidad = 30
progreso = 0
dependencia = 0

def menu():
  print()
  print()
  print("========================================================================")
  print("                           MENÚ PRINCIPAL                               ")
  print("========================================================================")
  print("1. Començar nova partida")
  print("2. Instruccions")
  print("3. Puntuacions")
  print("4. Sortir")
  print("========================================================================")
  choice = input("Inserta la teva opció: ")

  while(choice not in ["1", "2", "3", "4"]):
    choice = input("Número no vàlid. Torna a provar.")

  if choice == "1":
    game()
  elif choice == "2":
    instrucciones()
  elif choice == "3":
    puntuaciones()
  elif choice == "4":
    print("Adéu!")

def instrucciones():
  print()
  print()
  print("========================================================================")
  print("                           INSTRUCCIONS                                 ")
  print("========================================================================")
  print("En aquest joc hauràs de gestionar els recursos de la teva ONG per tal de")
  print("crear el major impacte positiu al planeta.")
  print("Començaràs amb 0€ i una reputació de 50/100.")
  print("")
  print("Hauràs de prendre decisions per tal de millorar el pais en el que estas")
  print("treballant. ")
  print("Després de 12 preguntes, el joc acabará i es mostrarà el teu progrés")
  print("toal. Has de tractar que la teva ONG no es quedi sense fons, que la ")
  print(" teva reputació no baixi de 0 i que el pais no tingui una dependència")
  print("massa alta ni una felicitat massa baixa. Bona sort!")
  print("========================================================================")
  menu()

def puntuaciones():
  #Hay que hacerlo
  menu()

def game():
  for i in range(12):
    print("========================================================================")
    print("                      PREGUNTA " + str(i+1) + " DE 12                   ")
    print("========================================================================")
    print("Diners: " + str(dinero) + "€")
    print("Reputació: " + str(reputacion) + "/100")
    print("Felicitat: " + str(felicidad) + "/100")
    print("Progrés: " + str(progreso) + "/100")
    print("========================================================================")
    print("")
    print("")
    print(pregunta[i])
    for j in range(4):
      print(respuesta[i][j])
    print("========================================================================")
    opcio = input("Inserta la acció que duràs a terme: ")
    while(opcio not in ["1", "2", "3", "4"]):
      opcio = input("Número no vàlid. Torna a provar.")
    print("========================================================================")

    #Poner pregunta 
    


print("========================================================================")
print("                   🌍 ONG SIMULATOR GAME 🌍                ")
print("========================================================================")
print("Benvingut a l'ONG simulator!")
print("En aquest joc, hauràs de gestionar una ONG per a poder ajudar")
print("a la gent que ho necessiti.")

menu()
