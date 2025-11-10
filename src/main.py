from fastapi import FastAPI

# Создаем экземпляр FastAPI приложения
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