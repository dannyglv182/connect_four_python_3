# Python 3 Connect Four

A full-stack Connect Four web application built with Python, FastAPI, React, and Vite.

![Screenshot](./screenshots/game.png)

## Overview

This project allows a player to play a quick game of connect four against the computer through a simple frontend interface that interacts with the backend.

The goal of this project was to strengthen my understanding of:
- Frontend and backend communication
- REST APIs
- React state management
- Python application structure
- Full-stack application design

---

## Why I Built This

This was one of my first coding projects.

At the time, I was looking for a way to turn basic loops and data structures into a functional program. I ended up using Python dictionaries to store lists of possible wins throughout the grid which might have been a little more than necessary, but made it a valuable learning experience. It was originally a terminal based game and ended with either stating win, lose or draw. Eventually, I decided to add React, FastAPI, and Docker for the learning experience. Now the backend returns an array with X's and O's representing moves that the front end displays

## How to run
1. Start Fastapi server ```fastapi dev```
2. Start React server ``` npm run dev ```

## Dependencies
- **Pytest**
Used for unit testing. 
