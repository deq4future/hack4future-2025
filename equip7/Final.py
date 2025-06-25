def finalitzar_partida(game_id):
    if not os.path.exists(NOM_FITXER):
        print(" No s'ha trobat el fitxer de la partida.")
        return

    with open(NOM_FITXER, "r") as f:
        dades_partida = json.load(f)

    score = dades_partida.get("punts", 0)

    cos = {
        "game_id": game_id,
        "data": dades_partida,
        "score": score
    }

    try:
        resposta = requests.post("https://fun.codelearn.cat/hackathon/game/finalize", json=cos)
        if resposta.status_code == 200:
            print(" Partida finalitzada correctament!")
            print(" Resposta del servidor:")
            print(resposta.json())

            os.remove(NOM_FITXER)
            print(" Fitxer de partida eliminat.")
        else:
            print(f" Error en finalitzar la partida: codi {resposta.status_code}")
    except requests.exceptions.RequestException as e:
        print(f" Error de connexió finalitzant la partida: {e}")
