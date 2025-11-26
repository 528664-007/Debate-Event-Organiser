# Debate Event Organiser
# Debate Event Organiser

A complete Flask-based system for managing debate competitions.  
Features:

- Add Events
- Add Participants
- Create Event Schedules
- Auto-generated API endpoints
- SQLite database
- Clean UI (HTML + CSS)

---

## Installation

git clone https://github.com/your-username/debate-event-organiser
cd debate-event-organiser
pip install -r requirements.txt



---

## Run the Server

python app.py


The website runs at:

http://127.0.0.1:5000/


---

## API Endpoints

| Endpoint | Purpose |
|---------|---------|
| `/api/events` | List all events |
| `/api/participants/<event_id>` | Get participants for event |

---

## Folder Structure

debate-event-organiser/
├── app.py
├── config.py
├── requirements.txt
├── templates/
├── static/
├── models/
├── database/
