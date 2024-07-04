from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворення рядка дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
        input_date = datetime.strptime(date, '%Y-%m-%d').date()
        # Отримання поточної дати без часу
        today_date = datetime.today().date()
        # Розрахунок різниці між датами у днях
        difference = (today_date - input_date).days
        return difference
    except ValueError:
        # Обробка неправильного формату вхідних даних
        return "Неправильний формат дати. Введіть дату у форматі 'РРРР-ММ-ДД'."

# Приклади використання функції:
print(get_days_from_today("2023-06-29"))
print(get_days_from_today("2024-06-29"))
print(get_days_from_today("2025-01-01"))

#Обробка неправильного формату:
print(get_days_from_today("23-23-23")) 
print(get_days_from_today("1-1-1")) 
print(get_days_from_today("2024-02-30")) 
