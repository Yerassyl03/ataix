import requests


API_BASE_URL = "https://api.ataix.kz/api"


def log_event(message, event_type="INFO"):
    icons = {
        "INFO": "ℹ️",
        "SUCCESS": "✅",
        "WARNING": "⚠️",
        "ERROR": "❌"
    }
    print(f"{icons.get(event_type, 'ℹ️')} {message}")

# Получение списка всех валют
def get_currencies():
    url = f"{API_BASE_URL}/currencies"
    log_event(f"🔄 Запрос к API: {url}", "INFO")

    response = requests.get(url)
    if response.status_code == 200:
        currencies = response.json()
        log_event("✅ Успешный ответ от API (валюты)", "SUCCESS")

        print("\n📊 **Список валют:**")
        print("🔍 Debug:", currencies)  

        # Если `currencies` - список строк, просто выводим их
        if isinstance(currencies, list) and all(isinstance(item, str) for item in currencies):
            for currency in currencies:
                print(f"💰 {currency}")  # Вывод без .get()
        # Если `currencies` - список словарей, используем .get()
        elif isinstance(currencies, list) and all(isinstance(item, dict) for item in currencies):
            for currency in currencies:
                print(f"💰 {currency.get('symbol', 'N/A')} - {currency.get('name', 'N/A')}")
        else:
            log_event("⚠️ Непонятный формат данных!", "WARNING")

        log_event(f"📈 Общее количество валют: {len(currencies)}", "INFO")
    else:
        log_event(f"❌ Ошибка {response.status_code}: {response.text}", "ERROR")

# Получение списка торговых пар
def get_symbols():
    url = f"{API_BASE_URL}/symbols"
    log_event(f"🔄 Запрос к API: {url}", "INFO")

    response = requests.get(url)
    if response.status_code == 200:
        symbols = response.json()
        log_event("✅ Успешный ответ от API (торговые пары)", "SUCCESS")

        print("\n📊 **Список торговых пар:**")
        for symbol in symbols:
            print(f"🔄 {symbol}")
        
        log_event(f"📈 Общее количество торговых пар: {len(symbols)}", "INFO")
    else:
        log_event(f"❌ Ошибка {response.status_code}: {response.text}", "ERROR")

# Получение цен всех монет и токенов
def get_prices():
    url = f"{API_BASE_URL}/prices"
    log_event(f"🔄 Запрос к API: {url}", "INFO")

    response = requests.get(url)
    if response.status_code == 200:
        prices = response.json()
        log_event("✅ Успешный ответ от API (цены)", "SUCCESS")

        print("\n📊 **Цены монет и токенов (Debug):**")
        print(prices)  # Выводим сырые данные

        # Проверяем, является ли prices списком словарей
        if isinstance(prices, list) and all(isinstance(item, dict) for item in prices):
            for price in prices:
                print(f"💲 {price.get('symbol', 'N/A')}: {price.get('price', 'N/A')}")
            log_event(f"📈 Всего записей: {len(prices)}", "INFO")
        else:
            log_event("⚠️ Формат данных неожиданный! Возможно, API изменилось.", "WARNING")
    else:
        log_event(f"❌ Ошибка {response.status_code}: {response.text}", "ERROR")

# Запуск программы
if __name__ == "__main__":
    get_currencies()
    get_symbols()
    get_prices()
