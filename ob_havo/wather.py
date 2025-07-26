
weather_data = {
    "Toshkent": " Quyoshli, +36°C",
    "Samarqand": " Biroz bulutli, +33°C",
    "Buxoro": " Issiq, +38°C",
    "Andijon": " Yomg'ir ehtimoli, +29°C",
    "Xiva": " Juda issiq, +40°C"
}

def show_all_weather():
    print(" Barcha shaharlar bo‘yicha ob-havo:")
    for city, info in weather_data.items():
        print(f"- {city}: {info}")

def search_weather():
    city = input(" Qaysi shaharni qidirmoqchisiz? ").title()
    info = weather_data.get(city)
    if info:
        print(f" {city} uchun ob-havo: {info}")
    else:
        print(" Bu shahar bo‘yicha ma'lumot topilmadi.")
