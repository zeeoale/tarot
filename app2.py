from flask import Flask, render_template, jsonify, url_for
import os, random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/draw_card')
def draw_card():
    cards_folder = os.path.join('static', 'cards')
    card_files = [f for f in os.listdir(cards_folder) if f != 'back.jpg']
    selected = random.choice(card_files)
    return jsonify({'card': url_for('static', filename=f'cards/{selected}').replace('/static/', '/helly_ryu/static/')})
