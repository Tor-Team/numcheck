def get_breach_links(phone):
    clean = phone.replace("+", "").replace(" ", "").replace("-", "")
    return {
        "Have I Been Pwned": f"https://haveibeenpwned.com/PhoneNumber/{clean}",
        "LeakCheck": f"https://leakcheck.io/search?query={clean}",
        "DeHashed": f"https://dehashed.com/search?query={clean}",
        "IntelX": f"https://intelx.io/?s={clean}",
        "Snusbase": f"https://snusbase.com/search?q={clean}",
        "Leak-Lookup": f"https://leak-lookup.com/search?query={clean}",
    }

def get_breach_summary(phone):
    return {
        "Проверка утечек": "Используйте внешние сервисы (ссылки ниже)",
        "Статус": "Требуется ручная проверка",
        "Рекомендация": "Проверьте номер на Have I Been Pwned",
    }
