from services.note_service import get_note
from services.org_service import user_in_org

def generate_org_report(user, note_id, org_override=None):
    note = get_note(note_id)

    if not note:
        return None

    target_org = org_override if org_override else note["org_id"]

    if not user_in_org(user, target_org):
        return None

    if user["role"] not in ["manager", "admin"]:
        return None

    return {
        "note_id": note["id"],
        "org": target_org,
        "content": note["content"]
    }
