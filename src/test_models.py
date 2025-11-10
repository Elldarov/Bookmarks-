# test_models.py
import sys
import os

# ДОБАВИЛ ПУТЬ К src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from models.bookmarks import BookmarkCreate
from pydantic import ValidationError

def test_valid_bookmark():
    """Тест 1: Проверяем создание закладки с валидными данными"""
    print("🧪 Тест 1: Валидные данные")
    
    bookmark = BookmarkCreate(
        url="https://python.org", # type: ignore
        title="Python Official Site",
        description="Home page of Python programming language",
        tags=["programming", "python", "docs"]
    )
    
    # Проверяем что поля заполнились правильно
    assert str(bookmark.url) == "https://python.org/"  # ← HttpUrl автоматически добавляет /
    assert bookmark.title == "Python Official Site"
    assert bookmark.description == "Home page of Python programming language"
    assert bookmark.tags == ["programming", "python", "docs"]
    
    print("✅ Тест 1 пройден: Валидные данные работают")
    return bookmark

def test_tag_normalization():
    """Тест 2: Проверяем нормализацию тегов"""
    print("🧪 Тест 2: Нормализация тегов")
    
    bookmark = BookmarkCreate(
        url="https://example.com", # type: ignore
        title="Test Site",
        tags=["  PYTHON  ", "python", "WEB", "  web  ", "  "] ,# Теги с пробелами и дубликатами
        description="Test description"
    )
    
    # Проверяем что теги нормализовались
    expected_tags = ["python", "web"]  # Должны остаться только уникальные, в нижнем регистре
    assert bookmark.tags == expected_tags, f"Ожидалось {expected_tags}, но получил {bookmark.tags}"
    
    print("✅ Тест 2 пройден: Теги нормализуются правильно")

def test_invalid_url():
    """Тест 3: Проверяем обработку невалидного URL"""
    print("🧪 Тест 3: Невалидный URL")
    
    try:
        bookmark = BookmarkCreate( # type: ignore
            url="not-a-valid-url",  # ← Это вызовет ошибку # type: ignore
            title="Test",
            description="Test description"
        )
        print("❌ Тест 3 не пройден: Должна быть ошибка валидации URL")
        return False
    except ValidationError as e: # type: ignore
        print("✅ Тест 3 пройден: Невалидный URL вызывает ошибку")
        return True

def test_empty_title():
    """Тест 4: Проверяем обработку пустого заголовка"""
    print("🧪 Тест 4: Пустой заголовок")
    
    try:
        bookmark = BookmarkCreate( # type: ignore
            url="https://example.com", # type: ignore
            title="   ", # Только пробелы
            description="Test description"
        )
        print("❌ Тест 4 не пройден: Должна быть ошибка пустого заголовка")
        return False
    except ValidationError as e: # type: ignore
        print("✅ Тест 4 пройден: Пустой заголовок вызывает ошибку")
        return True

def test_too_many_tags():
    """Тест 5: Проверяем ограничение на количество тегов"""
    print("🧪 Тест 5: Слишком много тегов")
    
    try:
        bookmark = BookmarkCreate( # type: ignore
            url="https://example.com", # type: ignore
            title="Test",
            tags=[f"tag{i}" for i in range(15)]  # 15 тегов вместо 10
            ,
            description="Test description"
        )
        print("❌ Тест 5 не пройден: Должна быть ошибка слишком много тегов")
        return False
    except ValidationError as e: # type: ignore
        print("✅ Тест 5 пройден: Слишком много тегов вызывает ошибку")
        return True

def test_forbidden_domain():
    """Тест 6: Проверяем запрещённые домены"""
    print("🧪 Тест 6: Запрещённый домен")
    
    try:
        bookmark = BookmarkCreate( # type: ignore
            url="http://localhost:8000",  # ← Запрещённый домен # type: ignore
            title="Test",
            description="Test description"
        )
        print("❌ Тест 6 не пройден: Должна быть ошибка запрещённого домена")
        return False
    except ValidationError as e: # type: ignore
        print("✅ Тест 6 пройден: Запрещённый домен вызывает ошибку")
        return True

def run_all_tests():
    """Запускаем все тесты"""
    print("🚀 ЗАПУСК ТЕСТИРОВАНИЯ МОДЕЛЕЙ")
    print("=" * 50)
    
    tests_passed = 0
    tests_failed = 0
    
    # Запускаем все тесты
    try:
        test_valid_bookmark()
        tests_passed += 1
    except Exception as e:
        print(f"❌ Тест 1 упал: {e}")
        tests_failed += 1
    
    try:
        test_tag_normalization()
        tests_passed += 1
    except Exception as e:
        print(f"❌ Тест 2 упал: {e}")
        tests_failed += 1
    
    try:
        if test_invalid_url():
            tests_passed += 1
        else:
            tests_failed += 1
    except Exception as e:
        print(f"❌ Тест 3 упал: {e}")
        tests_failed += 1
    
    try:
        if test_empty_title():
            tests_passed += 1
        else:
            tests_failed += 1
    except Exception as e:
        print(f"❌ Тест 4 упал: {e}")
        tests_failed += 1
    
    try:
        if test_too_many_tags():
            tests_passed += 1
        else:
            tests_failed += 1
    except Exception as e:
        print(f"❌ Тест 5 упал: {e}")
        tests_failed += 1
    
    try:
        if test_forbidden_domain():
            tests_passed += 1
        else:
            tests_failed += 1
    except Exception as e:
        print(f"❌ Тест 6 упал: {e}")
        tests_failed += 1
    
    print("=" * 50)
    print(f"📊 РЕЗУЛЬТАТ: {tests_passed} пройдено, {tests_failed} упало")
    
    if tests_failed == 0:
        print("🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ! Твои модели работают правильно!")
    else:
        print("💪 Есть над чем поработать. Проверь валидаторы в моделях!")

if __name__ == "__main__":
    run_all_tests()