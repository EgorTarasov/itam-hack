import uvicorn
from src.app import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
