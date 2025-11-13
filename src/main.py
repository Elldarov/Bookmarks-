import uuid
from fastapi import FastAPI

from datetime import datetime

from src.models.bookmarks import BookmarkCreate, BookmarkResponse 
from src.database import getNoteins
app = FastAPI(
    title="Bookmarks API",
    description="Мой первый API для управления закладками!",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Успешный запуск"}


@app.post("/test-bookmark", response_model=BookmarkResponse)
async def test_bookmark(bookmark: BookmarkCreate) -> BookmarkResponse:
    """Тестовый эндпоинт для проверки работы моделей"""
    return BookmarkResponse(
        id=0,
        url=bookmark.url,
        title=bookmark.title,
        description=bookmark.description,
        tags=bookmark.tags,
        created_at=datetime.now(),
        updated_at=datetime.now()
    ) 
   
@app.post("/test-create")
async def test_create(bookmark: BookmarkCreate):
    """Тестовый эндпоинт для проверки работы моделей"""
    id = int(uuid.uuid4())
    getNoteins( 
        id ,
        url=str(bookmark.url),        # преобразуем HttpUrl в строку
        title=bookmark.title,
        description=bookmark.description,
        tags=bookmark.tags,           # или {'tag1': 'value1'} если нужен словарь
        createdDate=datetime.now(),
        updateDate=datetime.now()
    )
    return BookmarkCreate(
        id=id,
        url=bookmark.url,
        title=bookmark.title,
        description=bookmark.description,
        tags=bookmark.tags,
        created_at=datetime.now(),
        updated_at=datetime.now()
    ) 
   







    