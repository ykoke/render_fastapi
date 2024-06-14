from typing import Optional

from fastapi import FastAPI

import random

from fastapi.responses import HTMLResponse #インポート


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "たこやき"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]
    
    return {"result" : omikuji_list[random.randrange(10)]}

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>NetPro No.9</h1>
            <p>PythonとRender</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
