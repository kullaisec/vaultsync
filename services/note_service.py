from db import get_db
from cache import set_cache, get_cache

def create_note(user, title, content):
    db = get_db()
    db.execute(
        "INSERT INTO notes (owner_id, org_id, title, content) VALUES (?, ?, ?, ?)",
        (user["id"], user["org_id"], title, content)
    )
    db.commit()

def get_note(note_id):
    cached = get_cache(f"note:{note_id}")
    if cached:
        return cached

    db = get_db()
    note = db.execute(
        "SELECT * FROM notes WHERE id = ?",
        (note_id,)
    ).fetchone()

    if note:
        set_cache(f"note:{note_id}", note)

    return note
