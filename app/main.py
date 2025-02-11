from app import create_app
from app.config import settings
import uvicorn
config = settings
app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host=config.HOST, port=config.PORT)