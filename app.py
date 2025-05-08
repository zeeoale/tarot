from flask import Flask, render_template, jsonify, url_for, send_from_directory, request
import os, random

app = Flask(__name__, static_url_path='/helly_ryu/static')

@app.before_request
def log_request():
    print(f"🔍 Richiesta in arrivo: {request.path}")

@app.route('/helly_ryu/')
def index():
    print("📘 Home page caricata")
    return render_template('index.html')

@app.route('/helly_ryu/dante')
def dante():
    print("🃏 Pagina Tenebris Arcanum caricata")
    return render_template('dante.html')

@app.route('/helly_ryu/helly')
def helly():
    print("🌞 Pagina Sun of Arcana caricata")
    return render_template('helly.html')

@app.route('/helly_ryu/dante/draw_card')
def draw_card_dante():
    print("🎴 Estrazione carta da Tenebris Arcanum")
    cards_folder = os.path.join(app.static_folder, 'dante')
    card_files = [f for f in os.listdir(cards_folder) if f != 'back.jpg']
    selected = random.choice(card_files)
    return jsonify({'card': f"/helly_ryu/static/dante/{selected}"})

@app.route('/helly_ryu/helly/draw_card')
def draw_card_helly():
    print("🌅 Estrazione carta da Sun of Arcana")
    cards_folder = os.path.join(app.static_folder, 'helly')
    card_files = [f for f in os.listdir(cards_folder) if f != 'back.jpg']
    selected = random.choice(card_files)
    return jsonify({'card': f"/helly_ryu/static/helly/{selected}"})

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
