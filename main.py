from typing import Optional

from fastapi import FastAPI

<<<<<<< HEAD
from fastapi.responses import HTMLResponse #インポート


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "たこやき"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
<<<<<<< HEAD


@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
=======
