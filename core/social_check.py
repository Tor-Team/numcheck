import urllib.request
import urllib.error
import json

def check_telegram(phone):
    clean = phone.replace("+", "").replace(" ", "").replace("-", "")
    try:
        url = f"https://t.me/+{clean}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        resp = urllib.request.urlopen(req, timeout=5)
        final = resp.geturl()
        if final != url and "not" not in final:
            return "Аккаунт найден"
        return "Возможно найден (проверьте ссылку)"
    except urllib.error.HTTPError as e:
        return "Не обнаружен" if e.code in (404, 302) else f"Ошибка ({e.code})"
    except Exception:
        return "Не удалось проверить"

def check_whatsapp(phone):
    clean = phone.replace("+", "").replace(" ", "").replace("-", "")
    try:
        url = f"https://wa.me/{clean}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        resp = urllib.request.urlopen(req, timeout=5)
        return "WhatsActive (откройте ссылку для проверки)"
    except Exception:
        return "Не удалось проверить"

def check_viber(phone):
    clean = phone.replace("+", "").replace(" ", "").replace("-", "")
    try:
        url = f"https://chats.viber.com/{clean}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        resp = urllib.request.urlopen(req, timeout=5)
        return "Возможно найден (проверьте ссылку)"
    except Exception:
        return "Не удалось проверить"

def check_social_networks(phone):
    results = {}

    telegram = check_telegram(phone)
    results["Telegram"] = telegram

    whatsapp = check_whatsapp(phone)
    results["WhatsApp"] = whatsapp

    viber = check_viber(phone)
    results["Viber"] = viber

    return results

def get_social_links(phone):
    clean = phone.replace("+", "").replace(" ", "").replace("-", "")
    return {
        "Telegram": f"tg://resolve?domain={clean}",
        "WhatsApp": f"https://wa.me/{clean}",
        "Viber": f"viber://chat?number=%2B{clean}",
        "Telegram Web": f"https://t.me/+{clean}",
        "WhatsApp Web": f"https://web.whatsapp.com/send?phone={clean}",
    }
