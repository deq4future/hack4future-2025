import requests
import random
import time

resposta = requests.get("https://fun.codelearn.cat/hackathon/game/new") #Web
   #200 vol dir OK!
dades = resposta.json() #Guardar datos
id = dades["game_id"]
seed = dades["seed"]


preguntes = ["Com aconsegueixes la teva finançament inicial?", 
             "Necessites promocionar-te. Com ho fas?", 
             "Posteriorment decideixes seguir la tendència i crear un compte a les xarxes socials. Què publicaràs?",
             "Com a ONG has de decidir com actuar per primera vegada. Què faràs?",
             "Veus que el país en el qual vols desenvolupar necessita ajuda en diverses àrees. A quina àrea decideixes invertir?", 
             ["Has decidit enfocar-te en l'educació del país. De quina manera ho fas?",
              "Has decidit enfocar-te en la sanitat del país. Tens 8 monedes per invertir. En que les gastes?","Has decidit enfocar-te en l'electricitat del país. Com ho fas?"
             ],
             "Ara et toca millorar el sistema educatiu del país. Com ho fas?",
             "El país té un índex de desnutrició massa elevat. Com actues?", 
             "Què fas amb les infraestructures del país? Quines millores implantaràs als habitatges?",
             "L'economia del país depèn massa de les teves inversions. Com ho reverteixes?", 
             "El govern et demana la teva col·laboració. Què decideixes fer?",
             ["L'index de corrupció a la teva ONG és molt elevat, com ho gestiones?",
             "Els petits poblats tenen molta dependència de la teva ONG. Com ho resols?",
             "Sobtadament, un desastre natural arrasa amb el país. Com fas front a la situació?",
             "Un grup de vandalisme europeu ha atacat un petit poblat del teu país. Com actues?"],
            "Has ajudat moltíssim al món, però tot i així, s'ha de continuar amb el teu llegat. Què fas al respecte?"]

opcions = [["Decideixes fer una manifestació","Surts al carrer i demanes diners per una bona causa","Demanes un préstec"],
           ["Crees un anunci","Parles amb coneguts perquè s'uneixin a la teva campanya", "Pagues a famosos perquè et promocionin"],
           ["Tots els progressos, tant positius com negatius","No publiques res, únicament promoció", "Publiques només els progressos positius"],
           ["Visites tots els països per conèixer les seves necessitats", "Envies diners perquè ho gastin com ells decideixin","Envies aliments"],
           ["Educació","Sanitat","Electricitat"],
           [["Envies docents procedents del teu país", "Aportes tauletes i recursos digitals a més d'internet", "Formes a docents locals"],
            ["Fas un gran hospital a la capital del país","Fas petits centres mèdics a cada zona", "Fas hospitals a cada regió i millores les comunicacions"],
            ["Envies pressupost per tal que s'autogestionin", "Compres electrodomèstics", "Aportes electricitat a cada llar"]],
           ["Implantes el sistema educatiu del teu país", "Decideixes continuar amb el seu sistema educatiu, però inverteixes en infraestructures i recursos","Decideixes continuar amb el seu sistema educatiu"],
           ["Fas recaptacions d'aliments a supermercats","Millores els estris i tècniques de conreu del país", "Ensenyes a racionar el menjar que tenen"],
           ["Construeixes cases de baix cost","Fas les cases locals més resistents", "Construeixes cases sostenibles"],
           ["Portes empreses desenvolupades procedents del teu país perquè ajudin al desenvolupament del país", "Dones recursos a les empreses locals", "Formes a joves que en un futur sostinguin l'economia local"],
           ["Dones tot el poder al govern","Col·labores amb el govern","Continues per la teva banda amb independència del govern"],
           [["Ocultes la corrupció","Fas pública la corrupció","Ho resols confidencialment"],["Aportes motocicletes a cada nucli familiar","Construeixes carreteres i crees transport públic","Ho ignores"],["Ho ignores","Demanes ajuda a altres països", "Ho resols amb ajuda dels cossos locals"],["Ignores la situació","Ho denuncies","Decideixes ajudar els poblats a revertir la situació sense nomenar-te en contra de les forces europees"]],
           ["Confies que les idees continuïn prosseguint a la societat", "Decideixes oferir els teus serveis a escoles","Decideixes tancar l'ONG"]
           ]

recompenses = [
  [[0,-4,4,0,0],[4,0,2,0,0],[80,0,-2,0,0]],
  [[-4,0,4,0,0],[4,0,2,0,0],[-12,0,6,0,0]],
  [[0,0,+4,0,0],[0,0,2,0,0],[0,0,-2,0,0]],
  [[-4,12,6,2,-6.6],[-12,0,2,-12,6.6],[-8,8,2,0,9.9]],
  [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
  [[[-8,8,4,6,3.3],[-8,4,2,-12,6.6],[-8,12,4,12,-6.6]],
   [[-8,-8,-4,0,+6.6],[-8,8,2,6,-3.3],[-8,12,4,18,-6.6]],
   [[-12,-4,2,-6,6.6],[-8,-4,-2,-6,0],[-8,8,4,12,-6.6]]],
  [[-8,-8,4,6,6.6],[-8,8,6,6,-6.6],[0,-4,0,0,0]],
  [[4,4,6,0,6.6],[-8,12,4,6,-6.6],[-4,-4,2,-6,0]],
  [[-4,-4,-2,-6,6.6],[-8,4,4,0,0],[-12,12,4,12,-6.6]],
  [[0,-8,2,6,6.6],[-8,8,4,12,-9.9],[-12,4,2,6,-3.3]],
  [[0,0,0,0,-3.3],[0,0,0,6,0],[0,0,0,0,6.6]],
  [[[-4,0,0,0,0],[0,0,-2,0,0],[-8,0,0,0,0]],
   [[0,0,-2,0,-3.3],[-4,-4,0,0,-3.3],[0,-4,0,0,-3.3]],
   [[0,-4,-2,0,0],[-4,4,0,0,3.3],[-4,4,0,0,-3.3]],
   [[0,0,-2,0,0],[-4,4,2,0,0],[0,4,2,0,0]]],
  [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]]

global dinero 
global reputacion 
global felicidad
global progreso
global dependencia
global corrupcion
global num_pregunta 
global k

for pregunta in recompenses:
  print(pregunta)

def menu():
  global dinero, reputacion, felicidad, progreso, dependencia, corrupcion, num_pregunta, k
  dinero = 0
  reputacion = 50 #sobre 100
  felicidad = 30
  progreso = 40
  dependencia = 50
  corrupcion = 0
  num_pregunta = 0
  k = 0
  
  print()
  print()
  print("========================================================================")
  print("                           MENÚ PRINCIPAL                               ")
  print("========================================================================")
  print("1. Començar nova partida")
  print("2. Instruccions")
  print("3. Sortir")
  print("========================================================================")
  choice = input("Inserta la teva opció: ")

  while(choice not in ["1", "2", "3"]):
    choice = input("Número no vàlid. Torna a provar.")

  if choice == "1":
    game()
  elif choice == "2":
    instrucciones()
  elif choice == "3":
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
  print("total. Has de tractar que la teva ONG no es quedi sense fons, que la ")
  print("teva reputació no baixi de 0 i que el pais no tingui una dependència")
  print("massa alta ni una felicitat massa baixa. Bona sort!")
  print("========================================================================")
  menu()


def game():
  global dinero, reputacion, felicidad, progreso, dependencia, corrupcion, num_pregunta, k
  
  for i in range(12):
    if i%3==0:
      print("Un donant anònim ha decidit donar-te 20 monedes per ajudar-te.")
      print("Què fas amb els diners?")
      print("1. Te'ls estalvies")
      print("2. Els inverteixes al govern")
      print ("3. Ho inverteixes en la població")
      accio=input("Inserta la acció que duràs a terme: ")
      if accio == "1":
        dinero += 20
      elif accio == "2":
        corrupcio += 1
      else:
        felicidad+=4 
        progreso+=6
    print()
    print()
    print("========================================================================")
    print("                      PREGUNTA " + str(i+1) + " DE 12                   ")
    print("========================================================================")
    print("Diners: " + str(dinero) + "€")
    print("Reputació: " + str(reputacion) + "/100")
    print("Felicitat: " + str(felicidad) + "/100")
    print("Progrés: " + str(progreso) + "/100")
    print("Dependència: " + str(dependencia) + "/100")
    print("========================================================================")
    num_pregunta = i
    if num_pregunta == 5:
      print (preguntes[i][int(k)-1])
    elif num_pregunta == 10:
      if corrupcion > 1:
        print(preguntes[10][0]) 
    else: 
      print(preguntes[i])

      
    
    for j in range(3):
      if num_pregunta == 5:
        print("   "+str(j+1)+". "+opcions[5][int(k)-1][j])
      else:
        print("   "+str(j+1)+". "+opcions[i][j])
      
    print("========================================================================")
    opcio = input("Inserta la acció que duràs a terme: ")
    while opcio not in ["1", "2", "3"]:
      opcio = input("Número no vàlid. Torna a provar.")
    
    print("========================================================================")
    print()
    print()
    print()
    print()
    
    
    if(num_pregunta == 5 or num_pregunta == 10):
      dinero += recompenses[i][k-1][int(opcio)-1][0]
      felicidad += recompenses[i][k-1][int(opcio)-1][1]
      reputacion += recompenses[i][k-1][int(opcio)-1][2]
      progreso += recompenses[i][k-1][int(opcio)-1][3]
      dependencia += recompenses[i][k-1][int(opcio)-1][4]
    else:
      dinero += recompenses[i][int(opcio)-1][0]
      felicidad += recompenses[i][int(opcio)-1][1]
      reputacion += recompenses[i][int(opcio)-1][2]
      progreso += recompenses[i][int(opcio)-1][3]
      dependencia += recompenses[i][int(opcio)-1][4]
    k = int(opcio)
  

    
              
    dades = {"pregunta": num_pregunta, "dinero": dinero, "reputacion" : reputacion, "felicidad" : felicidad, "progreso" : progreso, "dependencia" : dependencia, "corrupcion" : corrupcion}
    payload = {"game_id" : id, "data" : dades }
    resposta = requests.post("https://fun.codelearn.cat/hackathon/game/new", json=payload)

menu()

print("========================================================================")
print("                   🌍 ONG SIMULATOR GAME 🌍                ")
print("========================================================================")
print("Benvingut a l'ONG simulator!")
print("En aquest joc, hauràs de gestionar una ONG per a poder ajudar")
print("a la gent que ho necessiti.")




