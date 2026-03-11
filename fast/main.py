from fastapi import FastAPI
from pydantic import BaseModel
from game_logic.gameboard import player_move, run_game

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
    result = run_game(row, column)
    # return {
    #     "row": row,
    #    "column": column
    # }
    return result # Should return the state of the game 