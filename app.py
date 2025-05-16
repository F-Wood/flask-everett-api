from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

EXPLORATIONS = [
    {
        "citation": "All possible histories are real – Hugh Everett",
        "concept": "Décorrélation quantique entre branches de l'univers.",
        "niveau": "Intermédiaire"
    },
    {
        "citation": "La fonction d’onde ne s’effondre jamais. Elle se déploie.",
        "concept": "Décohérence + interprétation sans effondrement.",
        "niveau": "Avancé"
    },
    {
        "citation": "Chaque décision crée une nouvelle réalité.",
        "concept": "Lien avec l'expérience du chat de Schrödinger.",
        "niveau": "Débutant"
    }
]

@app.route('/api/explore')
def explore():
    return jsonify(random.choice(EXPLORATIONS))

if __name__ == '__main__':
    app.run(port=5000)