from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
import sqlite3

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# MODELS
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    description = db.Column(db.String(500))
    date = db.Column(db.String(100))


class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    institution = db.Column(db.String(200))
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))


class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    round_name = db.Column(db.String(200))
    time = db.Column(db.String(100))
    venue = db.Column(db.String(200))


# ROUTES
@app.route("/")
def index():
    events = Event.query.all()
    return render_template("index.html", events=events)


@app.route("/event/add", methods=['GET', 'POST'])
def add_event():
    if request.method == "POST":
        new_event = Event(
            name=request.form["name"],
            description=request.form["description"],
            date=request.form["date"]
        )
        db.session.add(new_event)
        db.session.commit()
        return redirect("/")
    return render_template("add_event.html")


@app.route("/participant/add/<int:event_id>", methods=["GET", "POST"])
def add_participant(event_id):
    if request.method == "POST":
        p = Participant(
            name=request.form["name"],
            institution=request.form["institution"],
            event_id=event_id
        )
        db.session.add(p)
        db.session.commit()
        return redirect("/")
    return render_template("add_participant.html", event_id=event_id)


@app.route("/schedule/add/<int:event_id>", methods=["GET", "POST"])
def add_schedule(event_id):
    if request.method == "POST":
        s = Schedule(
            event_id=event_id,
            round_name=request.form["round_name"],
            time=request.form["time"],
            venue=request.form["venue"]
        )
        db.session.add(s)
        db.session.commit()
        return redirect("/")
    return render_template("schedule.html", event_id=event_id)


# API ENDPOINTS (For automation or mobile usage)
@app.route("/api/events")
def api_events():
    events = Event.query.all()
    return jsonify([{"id": e.id, "name": e.name, "date": e.date} for e in events])


@app.route("/api/participants/<int:event_id>")
def api_participants(event_id):
    participants = Participant.query.filter_by(event_id=event_id).all()
    return jsonify([
        {"id": p.id, "name": p.name, "institution": p.institution}
        for p in participants
    ])


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
