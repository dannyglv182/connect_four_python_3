from fastapi import FastAPI
from pydantic import BaseModel
from game_logic.gameboard import player_move

app = FastAPI()

class Move(BaseModel):
    row: int
    column: int


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/move")
def move_request(move: Move):
    row = move.row
    column = move.column
    result = player_move(row, column, "player_1")
    return {
        "row": row,
        "column": column
    }