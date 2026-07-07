# My site
Мой личный сайт, cозданный от нечего делать.

## Стек
- HTML / CSS / JavaScript (vanilla, без фреймворков)
- Python (BeautifulSoup) - парсинг данных
- GitHub Actions - автообновление данных по расписанию
- Vercel - хостинг и автодеплой

## Структура проекта
```
├── .github/workflows/
│   └── update_movies.yml     # автообновление movies.json раз в 3 дня
├── projects/
│   ├── python.parser/
│   │   ├── index.html        # страница с фильмами
│   │   ├── movies.js         # рендер карточек фильмов
│   │   ├── movies.json       # данные (обновляются автоматически)
│   │   └── parser.py         # скрипт парсинга
│   └── index.html            # страница проектов
├── setup/
│   └── index.html
├── index.html                 # главная страница
├── script.js                  # reveal-анимации
└── style.css
```
