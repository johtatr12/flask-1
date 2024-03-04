from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///players.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    grade = db.Column(db.String(20), nullable=False)
    position = db.Column(db.String(30), nullable=False)

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    at_bats = db.Column(db.Integer, nullable=False)
    runs = db.Column(db.Integer, nullable=False)
    hits = db.Column(db.Integer, nullable=False)
    doubles = db.Column(db.Integer, nullable=False)
    triples = db.Column(db.Integer, nullable=False)
    home_runs = db.Column(db.Integer, nullable=False)
    rbis = db.Column(db.Integer, nullable=False)
    walks = db.Column(db.Integer, nullable=False)
    strikeouts = db.Column(db.Integer, nullable=False)
    batting_average = db.Column(db.Float, nullable=False)
    on_base_percentage = db.Column(db.Float, nullable=False)
    slugging_percentage = db.Column(db.Float, nullable=False)
    ops = db.Column(db.Float, nullable=False)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    players = Player.query.all()
    return render_template('index.html', players=players)

@app.route('/player/<int:player_id>')
def player(player_id):
    player = Player.query.get_or_404(player_id)
    records = Record.query.filter_by(player_id=player_id).all()
    return render_template('player.html', player=player, records=records)

if __name__ == '__main__':
    app.run(debug=True)
