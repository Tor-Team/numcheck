import phonenumbers
from phonenumbers import carrier, geocoder, timezone, PhoneNumberType

def get_phone_info(number_str):
    try:
        phone = phonenumbers.parse(number_str, None)
        if not phonenumbers.is_valid_number(phone):
            return {"Ошибка": "Недействительный номер"}

        country = geocoder.country_name_for_number(phone, "ru") or geocoder.country_name_for_number(phone, "en")
        region = geocoder.description_for_number(phone, "ru") or geocoder.description_for_number(phone, "en")
        operator = carrier.name_for_number(phone, "ru") or carrier.name_for_number(phone, "en") or "Не определён"
        timezones = timezone.time_zones_for_number(phone)
        num_type = phonenumbers.number_type(phone)
        type_map = {
            PhoneNumberType.MOBILE: "Мобильный",
            PhoneNumberType.FIXED_LINE: "Стационарный",
            PhoneNumberType.FIXED_LINE_OR_MOBILE: "Стационарный/Мобильный",
            PhoneNumberType.TOLL_FREE: "Бесплатный (Toll-Free)",
            PhoneNumberType.PREMIUM_RATE: "Платный (Premium)",
            PhoneNumberType.SHARED_COST: "Совместного использования",
            PhoneNumberType.VOIP: "VoIP",
            PhoneNumberType.PERSONAL_NUMBER: "Персональный",
            PhoneNumberType.PAGER: "Пейджер",
            PhoneNumberType.UAN: "UAN",
            PhoneNumberType.VOICEMAIL: "Голосовая почта",
            PhoneNumberType.UNKNOWN: "Неизвестный"
        }
        type_str = type_map.get(num_type, "Неизвестный")
        international = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        national = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.NATIONAL)
        e164 = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.E164)
        is_possible = phonenumbers.is_possible_number(phone)
        is_valid = phonenumbers.is_valid_number(phone)
        country_code = phone.country_code
        national_num = phone.national_number

        info = {
            "Номер (E.164)": e164,
            "Международный": international,
            "Национальный": national,
            "Код страны": f"+{country_code}",
            "Страна": country or "Не определена",
            "Регион": region or "Не определён",
            "Оператор": operator,
            "Тип линии": type_str,
            "Часовой пояс": ", ".join(timezones) if timezones else "Не определён",
            "Возможный": "Да" if is_possible else "Нет",
            "Действительный": "Да" if is_valid else "Нет",
            "Национальный номер": str(national_num),
        }

        if region and region != country:
            info["Регион (детально)"] = f"{region}, {country}"

        number_length = len(str(national_num))
        info["Длина номера"] = f"{number_length} цифр"

        possible_countries = phonenumbers.phonenumberutil.country_code_for_region
        info["Формат для набора"] = f"+{country_code} {national_num}"

        return info
    except Exception as e:
        return {"Ошибка": str(e)}
