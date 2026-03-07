from fastapi import FastAPI
from game_logic.gameboard import player_move

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}