from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from game_logic.gameboard import player_move, run_game

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    board = run_game(row, column)
    # return {
    #     "row": row,
    #    "column": column
    # }
    return {"board": board} # Should return the state of the game 