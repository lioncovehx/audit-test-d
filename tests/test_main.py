from fastapi.testclient import TestClient

from app.main import app


def test_app_has_notes_route():
    assert any(r.path == "/notes/{note_id}" for r in app.routes)
