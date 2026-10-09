#run as uvicorn app:app --reload in app.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request

from backend.routes.upload import router as upload_router
from backend.routes.query import router as query_router
from backend.routes.database import router as database_router
from backend.config import STATIC_DIR, TEMPLATE_DIR

app = FastAPI(title="RAG PDF Chatbot")

app.mount(
    "/static",
    StaticFiles(directory=str(STATIC_DIR)),
    name="static"
)

templates = Jinja2Templates(
    directory=str(TEMPLATE_DIR)
)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(

        "index.html",

        {"request": request}

    )


app.include_router(upload_router)

app.include_router(query_router)

app.include_router(database_router)


if __name__ == "__main__":

    import uvicorn

    uvicorn.run(

        "app:app",

        host="127.0.0.1",

        port=8000,

        reload=True

    )