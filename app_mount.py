
from flask import Flask, render_template, jsonify, url_for
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import os, random

# Flask app specifica per il mount
flask_app = Flask(__name__)
flask_app.config['APPLICATION_ROOT'] = '/helly_ryu'

@flask_app.route('/')
def index():
    return render_template('index.html')

@flask_app.route('/dante')
def dante():
    return render_template('dante.html')

@flask_app.route('/helly')
def helly():
    return render_template('helly.html')

@flask_app.route('/dante/draw_card')
def draw_card_dante():
    cards_folder = os.path.join('static', 'dante')
    card_files = [f for f in os.listdir(cards_folder) if f != 'back.jpg']
    selected = random.choice(card_files)
    card_url = url_for('static', filename=f'dante/{selected}', _external=False)
    return jsonify({'card': f"/helly_ryu{card_url}"})

@flask_app.route('/helly/draw_card')
def draw_card_helly():
    cards_folder = os.path.join('static', 'helly')
    card_files = [f for f in os.listdir(cards_folder) if f != 'back.jpg']
    selected = random.choice(card_files)
    card_url = url_for('static', filename=f'helly/{selected}', _external=False)
    return jsonify({'card': f"/helly_ryu{card_url}"})

# Mount su /helly_ryu
app = DispatcherMiddleware(None, {
    '/helly_ryu': flask_app
})
