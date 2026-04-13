from flask import Flask, jsonify
import json
import random

app = Flask(__name__)

# Funzione per caricare dati dal file JSON (players.json)
def load_players():
    with open('players.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def home():
    return "Benvenuto nella mia API di giocatori NBA!"

@app.route('/players')
def all_players():
    players = load_players()
    return jsonify(players)

@app.route('/random')
def random_player():
    players = load_players()
    player = random.choice(players)
    return jsonify(player)

if __name__ == "__main__":
    app.run(debug=True)
