import requests

class ServidorCodelearn:
    BASE_URL = "https://fun.codelearn.cat/hackathon/game"

    def __init__(self):
        self.game_id = None
        self.seed = None

    def iniciar_partida(self):
        resposta = requests.get(f"{self.BASE_URL}/new")
        dades = resposta.json()
        self.game_id = dades["game_id"]
        self.seed = dades["seed"]
        print(f"Partida iniciada amb ID: {self.game_id}")
        return [self.seed , self.game_id]

    def guardar_progres(self, data):
        body = {"game_id": self.game_id, "data": data}
        resposta = requests.post(f"{self.BASE_URL}/store_progress", json=body)
        return resposta.json()

    def finalitzar_partida(self, data, score):
        body = {"game_id": self.game_id, "data": data, "score": score}
        resposta = requests.post(f"{self.BASE_URL}/finish", json=body)
        return resposta.json()

    def recuperar_estat(self):
        resposta = requests.get(f"{self.BASE_URL}/get_progress?game_id={self.game_id}")
        return resposta.json()