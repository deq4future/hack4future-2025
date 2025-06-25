import requests
import random
import time

resposta = requests.get("https://fun.codelearn.cat/hackathon/game/new") #Web
   #200 vol dir OK!
dades = resposta.json() #Guardar datos
id = dades["game_id"]
seed = dades["seed"]

missatges = ["Guanyar diners de forma ràpida pot sonar temptador, però no sempre és la millor opció",
             "La unió crea el poder, mai ho oblidis",
             "Les xarxes socials poden amagar moltes històries",
             "Sempre és millor saber les necessitats de la població a la qual van destinats els nostres diners",
             "Les millors decisions són les quals es prenen amb el cor",
             ["Les accions han de suposar un canvi a llarg termini, amb l'objectiu de progressar com a societat",
            "Si repartim els hospitals i oferim transport, tothom podrà accedir a la sanitat",
             "Sempre és millor no començar la casa pel sostre, sense electricitat, no funcionarà res"],
             "La nostra forma de fer les coses no sempre és la correcta, millor els ensenyem de la forma que més ajudi a la resta",
             "Si oferim aliments a llarg termini continuarem igual, millor ajudem-los a autogestionar-se",
             "Les millors cases són les sostenibles, les quals ajudaran al país i al món", 
             "No es pot dependre sempre de la mateixa persona, millor repartir la feina",
             "Si pots ajudar a evitar la corrupció fes-ho!",
             ["Explica sempre la veritat, la gent confiarà en tu", 
             "Ajuda a tothom a poder dependre d'ells mateixos",
             "A grans desgràcies, majors solucions",
             "La vida ens posa obstacles, però junts els podrem afrontar"],
             "Consciència a tothom per seguir el teu llegat i crear un món millor!"]

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

opcions = [["Decideixes fer una manifestació (0 monedes)","Surts al carrer i demanes diners per una bona causa (+4 monedes)","Demanes un préstec (+80 monedes i -7 monedes per ronda)"],
           ["Crees un anunci (-4 monedes)","Parles amb coneguts perquè s'uneixin a la teva campanya (+4 monedes)", "Pagues a famosos perquè et promocionin (-12 monedes)"],
           ["Tots els progressos, tant positius com negatius","No publiques res, únicament promoció", "Publiques només els progressos positius"],
           ["Visites tots els països per conèixer les seves necessitats (-4 monedes)", "Envies diners perquè ho gastin com ells decideixin (-12 monedes)","Envies aliments (-8 monedes)"],
           ["Educació","Sanitat","Electricitat"],
           [["Envies docents procedents del teu país (-8 monedes)", "Aportes tauletes i recursos digitals a més d'internet (-4 monedes)", "Formes a docents locals (-8 monedes)"],
            ["Fas un gran hospital a la capital del país (-8 monedes)","Fas petits centres mèdics a cada zona (-8 monedes)", "Fas hospitals a cada regió i millores les comunicacions (-8 monedes)"],
            ["Envies pressupost per tal que s'autogestionin (-12 monedes)", "Compres electrodomèstics (-8 monedes)", "Aportes electricitat a cada llar (-8 monedes)"]],
           ["Implantes el sistema educatiu del teu país (-8 monedes)", "Decideixes continuar amb el seu sistema educatiu, però inverteixes en infraestructures i recursos (-8 monedes)","No actues i deixes el sistema educatiu com estava (0 monedes)"],
           ["Fas recaptacions d'aliments a supermercats (+4 monedes)","Millores els estris i tècniques de conreu del país (-8 monedes)", "Ensenyes a racionar el menjar que tenen (-4 monedes)"],
           ["Construeixes cases de baix cost (-4 monedes)","Fas les cases locals més resistents (-8 monedes)", "Construeixes cases sostenibles (-12 monedes)"],
           ["Portes empreses desenvolupades procedents del teu país perquè ajudin al desenvolupament del país (0 monedes)", "Dones recursos a les empreses locals (-8 monedes)", "Formes a joves que en un futur sostinguin l'economia local (-12 monedes)"],
           ["Dones tot el poder al govern","Col·labores amb el govern","Continues per la teva banda amb independència del govern"],
           [["Ocultes la corrupció (-4 monedes)","Fas pública la corrupció (0 monedes)","Ho resols confidencialment (-8 monedes)"],["Aportes motocicletes a cada nucli familiar (0 monedes)","Construeixes carreteres i crees transport públic (-4 monedes)","Ho ignores (0 monedes)"],["Ho ignore (0 monedes)s","Demanes ajuda a altres països (-4 monedes)", "Ho resols amb ajuda dels cossos locals (-4 monedes)"],["Ignores la situació (0 monedes)","Ho denuncies (-4 monedes)","Decideixes ajudar els poblats a revertir la situació sense nomenar-te en contra de les forces europees (-4 monedes)"]],
           ["Confies que les idees continuïn prosseguint a la societat", "Decideixes oferir els teus serveis a escoles","Decideixes tancar l'ONG"]
           ]



recompenses = [
  [[0,0,4,0,0],[4,0,2,0,0],[80,0,-2,0,0]],
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
global prestamo


def menu():
  global dinero, reputacion, felicidad, progreso, dependencia, corrupcion, num_pregunta, k, prestamo
  dinero = 0
  reputacion = 50 #sobre 100
  felicidad = 30
  progreso = 40
  dependencia = 50
  corrupcion = 0
  num_pregunta = 0
  k = 0
  prestamo = False
  
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
  global dinero, reputacion, felicidad, progreso, dependencia, corrupcion, num_pregunta, k, prestamo
  
  for i in range(13):
    if i%3==0 and i!=0:
      monedes = random.randint(1, 30)
      print()
      print("Un donant anònim ha decidit donar-te",monedes,"monedes per ajudar-te.")
      print("Què fas amb els diners?")
      print("1. Te'ls estalvies")
      print("2. Se'ls dones al govern")
      print ("3. Ho inverteixes en la població")
      accio=input("Inserta la acció que duràs a terme: ")
      if accio == "1":
        dinero += monedes
      elif accio == "2":
        corrupcion += 1
      else:
        felicidad+=4 
        progreso+=6
    print()
    print()
    print("========================================================================")
    print("                      PREGUNTA " + str(i+1) + " DE 13                   ")
    print("========================================================================")
    if(dinero<15):
      print("💷 Diners 💷: " + str(dinero) + "€")
    else:
      print("💵 Diners 💵: " + str(dinero) + "€")
    if(reputacion<50):
      print("📉 Reputació 📉: " + str(reputacion) + "/100")
    else:
      print("📈 Reputació 📈: " + str(reputacion) + "/100")
    if(felicidad<50):
      print("😢 Felicitat 😢: " + str(felicidad) + "/100")
    else:
      print("😊 Felicitat 😊: " + str(felicidad) + "/100")
    if(progreso<50):
      print("⬇️  Progrés ⬇️: " + str(progreso) + "/100")
    else:
      print("🔝  Progrés 🔝: " + str(progreso) + "/100")
    if(dependencia<50):
      print("⛓️‍💥  Dependència ⛓️‍💥: " + str(dependencia) + "/100")
    else:
      print("🪽  Dependència 🪽: " + str(dependencia) + "/100")
    print("========================================================================")
    num_pregunta = i
    if num_pregunta == 5:
      print (preguntes[i][int(k)-1])
    elif num_pregunta == 11:
      if corrupcion >= 1:
        pos=0
        print(preguntes[11][0]) 
      elif dependencia > 60:
        pos=1
        print(preguntes[11][1]) 
      elif reputacion < 70:
        pos=2
        print(preguntes[11][2])
      else:
        pos=3
        print(preguntes[11][3])
    else: 
      print(preguntes[i])  
    for j in range(3):
      if num_pregunta == 5:
        print("   "+str(j+1)+". "+opcions[5][int(k)-1][j])
      elif num_pregunta == 11:
        print ("   "+str(j+1)+". "+opcions[11][pos][j])
      else:
        print("   "+str(j+1)+". "+opcions[i][j])
    print("========================================================================")
    opcio = input("Inserta la acció que duràs a terme: ")
    while opcio not in ["1", "2", "3"]:
      opcio = input("Número no vàlid. Torna a provar.")
    print("========================================================================")
    if(prestamo):
      dinero-=7
    if(num_pregunta == 0):
      if(int(opcio) == 3):
        print()
        print("Has decidit demanar un préstec. Hauràs de pagar 7 monedes cada ronda.")
        prestamo = True
        
    if(num_pregunta == 10):
      if(opcio==1):
        corrupcion +=1
      elif (opcio==2):
        corrupcion -=1
      
    if(num_pregunta == 5 or num_pregunta == 11):
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
    print()

    if num_pregunta == 5:
      print (missatges[i][int(k)-1])
    elif num_pregunta == 11:
      if corrupcion >= 1:
        pos=0
        print(missatges[11][0]) 
      elif dependencia > 60:
        pos=1
        print(missatges[11][1]) 
      elif reputacion < 70:
        pos=2
        print(missatges[11][2])
      else:
        pos=3
        print(missatges[11][3])
    else: 
      print(missatges[i])  
    


    dades = {"pregunta": num_pregunta, "dinero": dinero, "reputacion" : reputacion, "felicidad" : felicidad, "progreso" : progreso, "dependencia" : dependencia, "corrupcion" : corrupcion}
    payload = {"game_id" : id, "data" : dades }
    resposta = requests.post("https://fun.codelearn.cat/hackathon/game/new", json=payload)

    if(dinero<-2):
      print()
      print("Has perdut! No tens diners per continuar.")
      print()
      print()
      break

  puntos = dinero+reputacion+felicidad+progreso-dependencia
  print()
  print("Ha acabar la partida!!")
  print("PUNTUACIÓ: "+str(puntos))

  if(puntos<30):
    print("El teu objectiu era ajudar a la gent, o empitjorar la situació?")
  elif(puntos<80):
    print("Sembla que la teva ONG no ha aportat massa a la societat. Era millor que no hagués existit.")
  elif(puntos<130):
    print("Portar una ONG és una feina difícil, però esperem que hagis après per la pròxima.")
  elif(puntos<180):
    print("Has fet un bon treball, però hi ha moltes desicions que podrien haver fet un impacte més gran.")
  elif(puntos<230):
    print("Bastant bé! Has ajudat a molts, però encara hi ha molt per fer.")
  else:
    print("Has obtingut la puntuació màxima! Has creat una ONG que ha canviat moltes vides. Enhorabona!")

  
  print("")
  print("=============================================================================================")
  print("                                     🧠 MISSATGE DEL JOC 🧠                                  ")
  print("=============================================================================================")
  print("Sovint, els països amb menys recursos no poden superar les seves dificultats econòmiques ")
  print("per la manca d’oportunitats a la seva regió. ")
  print("I els països més desenvolupats pensen que només amb diners es poden resoldre tots els seus")
  print("problemes, però la realitat és molt més complexa.")
  print()
  print("Esperem que després de jugar a aquest joc hagis entès que imposar la teva manera de viure ")
  print("en un país amb pocs recursos no és la millor forma d'ajudar-lo. ")
  print("Cal entendre les seves necessitats reals i treballar colze a colze amb la seva gent per ")
  print("tal de fer un impacte positiu i durador en el seu món.")
  print()
  print("Perquè, com diu un proverbi xinès: la clau no és donar-los peix, sinó ensenyar-los a pescar.")

  
  dades = {"pregunta": num_pregunta, "dinero": dinero, "reputacion" : reputacion, "felicidad" : felicidad, "progreso" : progreso, "dependencia" : dependencia, "corrupcion" : corrupcion}
  payload = {"game_id" : id, "data" : dades, "score" : puntos }
  resposta = requests.post("https://fun.codelearn.cat/hackathon/game/new", json=payload)


print("========================================================================")
print("                   🌍 ONG SIMULATOR GAME 🌍                ")
print("========================================================================")
print("Benvingut a l'ONG simulator!")
print("En aquest joc, hauràs de gestionar una ONG per a poder ajudar")
print("a la gent que ho necessiti.")

menu()

