from flask import Flask, jsonify, request

app = Flask(__name__)

class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# TODO: Task 1 - Define the Problem
@app.route("/events", methods=["POST"])
def create_event():
    # TODO: Task 2 - Design and Develop the Code
    data = request.get_json(silent=True)

    # TODO: Task 3 - Implement the Loop and Process Each Element
    if not data or "title" not in data:
        return jsonify({"error": "Missing required field: title"}), 400

    title = data["title"]
    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "title must be a non-empty string"}), 400

    new_id = max((e.id for e in events), default=0) + 1
    new_event = Event(new_id, title.strip())
    events.append(new_event)

    # TODO: Task 4 - Return and Handle Results
    return jsonify(new_event.to_dict()), 201

# TODO: Task 1 - Define the Problem
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    data = request.get_json(silent=True)

    # TODO: Task 3 - Implement the Loop and Process Each Element
    event = next((e for e in events if e.id == event_id), None)
    if event is None:
        return jsonify({"error": f"Event with id {event_id} not found"}), 404

    if not data or "title" not in data:
        return jsonify({"error": "Missing required field: title"}), 400

    title = data["title"]
    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "title must be a non-empty string"}), 400

    event.title = title.strip()

    # TODO: Task 4 - Return and Handle Results
    return jsonify(event.to_dict()), 200

# TODO: Task 1 - Define the Problem
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    event = next((e for e in events if e.id == event_id), None)

    # TODO: Task 3 - Implement the Loop and Process Each Element
    if event is None:
        return jsonify({"error": f"Event with id {event_id} not found"}), 404

    events.remove(event)

    # TODO: Task 4 - Return and Handle Results
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)