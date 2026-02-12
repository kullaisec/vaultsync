from flask import Flask, request, jsonify
from auth import get_current_user
from services.note_service import create_note
from services.report_service import generate_org_report

app = Flask(__name__)

@app.route("/create", methods=["POST"])
def create():
    user = get_current_user()
    if not user:
        return "Unauthorized", 401

    create_note(
        user,
        request.json.get("title"),
        request.json.get("content")
    )

    return "Created"

@app.route("/report")
def report():
    user = get_current_user()
    if not user:
        return "Unauthorized", 401

    note_id = request.args.get("note_id")
    org_override = request.args.get("org")

    result = generate_org_report(user, note_id, org_override)

    if not result:
        return "Forbidden", 403

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
