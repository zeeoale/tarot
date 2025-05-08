import os
import random
from flask import Flask, render_template, jsonify, url_for
from werkzeug.middleware.dispatcher import DispatcherMiddleware

print("🟢 INIT: import success")

flask_app = Flask(__name__)
flask_app.debug = True
print("🟢 Flask app creata")

flask_app.config['APPLICATION_ROOT'] = '/helly_ryu'

@flask_app.route('/')
def index():
    print("📥 GET /helly_ryu/")
    return "<h1>HELLO WORLD</h1>"

@flask_app.route('/draw_card')
def draw_card():
    print("📥 GET /draw_card")
    cards_folder = os.path.join('static', 'cards')
    try:
        card_files = [f for f in os.listdir(cards_folder) if f != 'back.jpg']
        selected = random.choice(card_files)
        print(f"🎴 Carta scelta: {selected}")
        card_url = url_for('static', filename=f'cards/{selected}', _external=False)
        return jsonify({'card': card_url})
    except Exception as e:
        print("❌ Errore in draw_card:", e)
        return jsonify({'error': str(e)}), 500

from werkzeug.middleware.dispatcher import DispatcherMiddleware

def app_with_script_name(environ, start_response):
    # Forza SCRIPT_NAME manualmente se non presente
    if 'SCRIPT_NAME' not in environ:
        environ['SCRIPT_NAME'] = '/helly_ryu'
    return flask_app(environ, start_response)

app = DispatcherMiddleware(None, {
    '/helly_ryu': app_with_script_name
})
