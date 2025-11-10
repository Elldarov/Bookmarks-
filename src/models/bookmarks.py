from pydantic import BaseModel, HttpUrl, Field, field_validator
from typing import Optional, List
from datetime import datetime

class BookmarkBase(BaseModel):
    """Базовая модель закладки"""
    url: HttpUrl 
    title: str = Field(..., min_length=1, max_length=200, description="Название закладки")
    description: Optional[str] = Field(None, max_length=500, description="Описание")
    tags: List[str] = Field(default=[])

    @field_validator('title')
    @classmethod
    def validate_title(cls, v: str):
        """Убираем пробелы"""
        if v:
            return v.strip()
        return v
    
    @field_validator('url')
    @classmethod
    def validate_url(cls, v: HttpUrl):
        forbidden_domains = ['localhost', '127.0.0.1', 'example.com']
        domain = str(v.host)
        
        if domain in forbidden_domains:
            raise ValueError('URL содержит запрещённый домен')
        return v
       










class BookmarkCreate(BookmarkBase):
    """Загатовка для создания закладки"""
    pass

class BookmarkUpdate(BaseModel):
    """Модель для обновления закладки"""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=500)
    tags: Optional[List[str]] = Field(None)

class BookmarkResponse(BookmarkBase):
    """Модель для отображения закладки"""
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True