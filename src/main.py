from fastapi import FastAPI
from src.models.bookmarks import BookmarkCreate, BookmarkResponse 
from datetime import datetime

app = FastAPI(
    title="Bookmarks API",
    description="Мой первый API для управления закладками!",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "🎉 Ура! Мой Bookmarks API работает!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "project": "bookmarks_api"}


@app.post("/test-bookmark", response_model=BookmarkResponse)
async def test_bookmark(bookmark: BookmarkCreate) -> BookmarkResponse:
    """Тестовый эндпоинт для проверки работы моделей"""
    return BookmarkResponse(
        id="test-id-123",
        url=bookmark.url,
        title=bookmark.title,
        description=bookmark.description,
        tags=bookmark.tags,
        created_at=datetime.now(),
        updated_at=datetime.now()
    ) 