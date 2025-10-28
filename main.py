from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Bose": "Can't Brick Us"}


@app.post("/marge/streaming/support/power_on")
def read_item(song_id: int, q: Union[str, None] = None):
    return {"song_id": song_id, "q": q}
