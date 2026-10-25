import os

import redis
from fastapi import FastAPI

app = FastAPI()
cache = redis.Redis.from_url(os.environ.get("REDIS_URL", "redis://localhost:6379/0"))


@app.get("/notes/{note_id}")
def get_note(note_id: int):
    value = cache.get(f"note:{note_id}")
    return {"id": note_id, "text": value.decode() if value else None}
