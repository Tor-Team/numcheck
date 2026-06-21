# numcheck - TOR TEAM

**TOR TEAM** — инструмент для анализа телефонных номеров на основе библиотеки `phonenumbers`.  
Получение информации о номере, проверка активности в социальных сетях, поиск утечек данных.

## Возможности

- Определение страны, региона, оператора и типа линии
- Форматирование номера (E.164, международный, национальный)
- Проверка наличия аккаунта в Telegram, WhatsApp, Viber
- Генерация ссылок для ручной верификации
- Ссылки на сервисы поиска утечек (Have I Been Pwned, LeakCheck, DeHashed, IntelX, Snusbase, Leak-Lookup)

## Установка

```bash
git clone https://github.com/tor-team/numcheck.git
cd numcheck
python -m venv venv
source venv/bin/activate  # Linux/macOS
# или: venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

## Использование

```bash
python main.py
```

## Зависимости

- `phonenumbers` — парсинг и валидация номеров
- `colorama` — цветной вывод в терминал

## Лицензия

MIT


##Разработчик - создатель 
