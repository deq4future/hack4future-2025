import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import json
import os
import requests
import threading

NOM_FITXER = "jugador.json"
SERVER_BASE_URL = "https://fun.codelearn.cat/hackathon/game"

class ScapeRoomApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scape Room")
        self.geometry("1280x800")

        self.score = 0
        self.nom_jugador = ""
        self.game_id = None
        self.estat_joc = "menu" 

        self.frame_imatge = tk.Label(self)
        self.frame_imatge.pack(pady=10)

        self.text_label = tk.Label(self, text="", font=("Helvetica", 14), wraplength=650, justify="left")
        self.text_label.pack(pady=10)

        self.entry_resposta = tk.Entry(self, font=("Helvetica", 14))
        self.entry_resposta.pack(pady=10)

        self.boto_confirmar = tk.Button(self, text="Confirmar", command=self.confirmar_resposta)
        self.boto_confirmar.pack(pady=10)

        self.boto_nova_partida = tk.Button(self, text="Nova Partida", command=self.iniciar_nova_partida)
        self.boto_sortir = tk.Button(self, text="Sortir", command=self.destroy)

        self.boto_nova_partida.pack(side="left", padx=20, pady=20)
        self.boto_sortir.pack(side="right", padx=20, pady=20)

        self.imatges = {}
        self.carregar_imatges()

        self.entry_resposta.pack_forget()
        self.boto_confirmar.pack_forget()

        self.progress_thread = None
        self.stop_progress_thread = False

    def carregar_imatges(self):
        noms_imatges = {
            "intro": "intro.jpg",
            "Mates": "Mates.jpg",
            "Enigma": "Enigma.jpg",
            "Historia": "Historia.jpg",
            "Natus": "Natus.jpg",
            "Espai": "Espai.jpg",
        }
        for nom, fitxer in noms_imatges.items():
            path = os.path.join("imatges", fitxer)
            if os.path.exists(path):
                img = Image.open(path)
                img = img.resize((600, 300))
                self.imatges[nom] = ImageTk.PhotoImage(img)
            else:
                print(path + " No trobat")
                self.imatges[nom] = None

    def mostrar_imatge(self, nom):
        img = self.imatges.get(nom)
        if img:
            self.frame_imatge.config(image=img, text="")
            self.frame_imatge.image = img
        else:
            self.frame_imatge.config(image="", text=f"No s'ha trobat la imatge {nom}")

    def iniciar_nova_partida(self):
        self.nom_jugador = simpledialog.askstring("Nom jugador", "Introdueix el teu nom:")
        if not self.nom_jugador:
            messagebox.showwarning("Atenció", "Has de posar un nom per continuar.")
            return
        
        
        try:
            resposta = requests.get(f"{SERVER_BASE_URL}/new")
            resposta.raise_for_status()
            dades_resposta = resposta.json()
            self.game_id = dades_resposta.get("game_id")
            if not self.game_id:
                messagebox.showerror("Error", "No s'ha pogut obtenir el game_id del servidor.")
                return
        except Exception as e:
            messagebox.showerror("Error", f"Error al comunicar-se amb el servidor: {e}")
            return

        self.score = 0
        self.guardar_dades({"nom": self.nom_jugador, "punts": self.score, "nivell": 1})

        self.boto_nova_partida.pack_forget()
        self.boto_sortir.pack_forget()

        self.estat_joc = "historia"
        self.mostrar_historia()

        
        self.stop_progress_thread = False
        self.progress_thread = threading.Thread(target=self.enviar_progresos_periodic, daemon=True)
        self.progress_thread.start()

    def enviar_progresos_periodic(self):
        import time
        while not self.stop_progress_thread:
            self.enviar_progress()
            time.sleep(10)

    def enviar_progress(self):
        if not self.game_id:
            return
        dades_partida = {
            "nom_jugador": self.nom_jugador,
            "score": self.score,
            "estat_joc": self.estat_joc,
        }
        try:
            resp = requests.post(f"{SERVER_BASE_URL}/store_progress",
                                 json={"game_id": self.game_id, "data": dades_partida})
            resp.raise_for_status()
        except Exception as e:
            print(f"Error enviant progrés al servidor: {e}")

    def mostrar_historia(self):
        text_historia = f"""
Un dia {self.nom_jugador} estava acampant amb els seus amics al bosc. Tots van decidir anar a explorar, però {self.nom_jugador} es va perdre.
Va trobar una petita casa de fusta i va decidir entrar a buscar ajuda.
Va picar a la porta, però va veure que era oberta.
Va entrar amb una mica de por.
Tot era fosc, i just quan va posar els dos peus a dins, la porta es va tancar a la seva esquena.
I, ara tu tens que ajudar a {self.nom_jugador} a sortir d'aquí. Bona sort!
"""
        self.mostrar_imatge("intro")
        self.text_label.config(text=text_historia.strip())
        self.entry_resposta.pack_forget()
        self.boto_confirmar.pack_forget()
        self.boto_continuar = tk.Button(self, text="Començar", command=self.problema1)
        self.boto_continuar.pack(pady=10)

    def problema1(self):
        self.estat_joc = "problema1"
        self.mostrar_imatge("Mates")
        text = (
            "Mires al teu voltant.\n"
            "Les parets són de fusta i, just al teu davant hi ha una pissarra amb operacions matemàtiques i un problema:\n"
            "Quin és el resultat de fer la meitat del doble de 12, més 8, dividit per 4?"
        )
        self.text_label.config(text=text)
        self.entry_resposta.delete(0, tk.END)
        self.entry_resposta.pack()
        self.boto_confirmar.pack()

        if hasattr(self, 'boto_continuar'):
            self.boto_continuar.destroy()

    def problema2(self):
        self.estat_joc = "problema2"
        self.mostrar_imatge("Enigma")
        self.pistes = [
            "Comença amb la lletra 'o'.",
            "Té la lletra 'b' al mig.",
            "Acaba amb la lletra 'a'.",
            "Es relaciona amb la llum i la foscor.",
        ]
        self.text_label.config(text=(
            "En aquesta segona sala hauràs de descobrir quina és la paraula amagada.\n\n"
            "Sóc una paraula de 5 lletres.\n"
            "Si treus la primera lletra, encara sona com abans.\n"
            "Si treus la segona lletra, també.\n"
            "Fins i tot si només queda una lletra, la paraula segueix sent la mateixa.\n"
            "Quina paraula sóc?"
        ))
        self.entry_resposta.delete(0, tk.END)

    def problema3(self):
        self.estat_joc = "problema3"
        self.mostrar_imatge("Historia")
        self.text_label.config(text=(
            "Heu entrat a la sala d'història.\n\n"
            "Sabeu quin any es va descobrir Amèrica, quin?"
        ))
        self.entry_resposta.delete(0, tk.END)
        self.intents_historia = 1
        self.etapa_historia = "america"

    def problema4(self):
        self.estat_joc = "problema4"
        self.mostrar_imatge("Natus")
        self.text_label.config(text="Quin gas és el més abundant a l’atmosfera terrestre?")
        self.entry_resposta.delete(0, tk.END)

    def problema5(self):
        self.estat_joc = "problema5"
        self.mostrar_imatge("Espai")
        self.text_label.config(text="Quin planeta és conegut com el planeta vermell?")
        self.entry_resposta.delete(0, tk.END)

    def confirmar_resposta(self):
        resposta = self.entry_resposta.get().strip()

        if self.estat_joc == "problema1":
            if resposta == "5":
                messagebox.showinfo("Correcte", "Molt bé, ho has aconseguit!")
                self.score += 3
                self.guardar_puntuacio()
                self.problema2()
            else:
                messagebox.showwarning("Incorrecte", "Resposta incorrecta. Torna-ho a intentar!")
                self.score += 1
                self.guardar_puntuacio()

        elif self.estat_joc == "problema2":
            if resposta.lower() == "ombra":
                if len(self.pistes) == 4:
                    messagebox.showinfo("Correcte", "Molt bé, a la primera!")
                    self.score += 3
                else:
                    messagebox.showinfo("Correcte", "Molt bé, passes a la següent sala!")
                    self.score += 1
                self.guardar_puntuacio()
                self.problema3()
            else:
                if self.pistes:
                    pista = self.pistes.pop(0)
                    messagebox.showwarning("Pista", pista)
                else:
                    messagebox.showwarning("Incorrecte", "No és correcte i no hi ha més pistes.")
                self.score += 0
                self.guardar_puntuacio()

        elif self.estat_joc == "problema3":
            if self.etapa_historia == "america":
                if resposta == "1492":
                    if self.intents_historia == 1:
                        messagebox.showinfo("Correcte", "Tu no seràs un expert en història, no?")
                        self.score += 3
                    else:
                        messagebox.showinfo("Correcte", "Molt bé!")
                        self.score += 1
                    self.guardar_puntuacio()
                    self.intents_historia = 1
                    self.etapa_historia = "revolucio"
                    self.text_label.config(text="Quin any va ser la revolució francesa?")
                    self.entry_resposta.delete(0, tk.END)
                else:
                    messagebox.showwarning("Incorrecte", "Torna a intentar!")
                    self.intents_historia += 1
            elif self.etapa_historia == "revolucio":
                if resposta == "1789":
                    if self.intents_historia == 1:
                        messagebox.showinfo("Correcte", "Fàcil?")
                        self.score += 3
                    else:
                        messagebox.showinfo("Correcte", "Molt bé!")
                        self.score += 1
                    self.guardar_puntuacio()
                    self.problema4()
                else:
                    messagebox.showwarning("Incorrecte", "Torna a intentar!")
                    self.intents_historia += 1

        elif self.estat_joc == "problema4":
            if resposta.lower() == "nitrogen":
                messagebox.showinfo("Correcte", "Mare meva que bo!")
                self.score += 3
                self.guardar_puntuacio()
                self.problema5()
            else:
                messagebox.showwarning("Incorrecte", "Torna a intentar!")
                self.score += 0
                self.guardar_puntuacio()

        elif self.estat_joc == "problema5":
            if resposta.lower() == "mart":
                messagebox.showinfo("Correcte", "Super Bé\nHas aconseguit escapar!")
                self.score += 3
                self.guardar_puntuacio()
                self.finalitzar_partida()
            else:
                messagebox.showwarning("Incorrecte", "Torna a intentar!")
                self.score += 0
                self.guardar_puntuacio()

    def guardar_puntuacio(self):
        dades = self.carregar_dades()
        if dades:
            dades["punts"] = self.score
            self.guardar_dades(dades)

    def carregar_dades(self):
        if os.path.exists(NOM_FITXER):
            with open(NOM_FITXER, "r") as f:
                return json.load(f)
        return None

    def guardar_dades(self, dades):
        with open(NOM_FITXER, "w") as f:
            json.dump(dades, f)

    def finalitzar_partida(self):
        self.stop_progress_thread = True  
        self.entry_resposta.pack_forget()
        self.boto_confirmar.pack_forget()
        text = f"""
{self.nom_jugador} surt corrents de la casa, feliç per haver aconseguit sortir sencer d'allà.
Corre pel bosc i aconsegueix trobar-se amb els seus amics, que l'estaven buscant.
Fi.
Has aconseguit {self.score} punts!
"""
        self.mostrar_imatge(None)
        self.text_label.config(text=text.strip())

        
        dades_partida = {
            "nom_jugador": self.nom_jugador,
            "score": self.score,
            "estat_joc": self.estat_joc,
        }
        try:
            resp = requests.post(f"{SERVER_BASE_URL}/finalize",
                                 json={"game_id": self.game_id, "data": dades_partida, "score": self.score})
            resp.raise_for_status()
        except Exception as e:
            print(f"Error notificació finalització al servidor: {e}")

        boto_sortir_final = tk.Button(self, text="Sortir", command=self.destroy)
        boto_sortir_final.pack(pady=20)

if __name__ == "__main__":
    app = ScapeRoomApp()
    app.mainloop()
