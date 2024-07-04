from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    # Поточна дата
    today = datetime.today().date()
    # Дата через 7 днів
    end_date = today + timedelta(days=7)

    upcoming_birthdays = []

    for user in users:
        # Перетворення дати народження з рядка у об'єкт datetime
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Створення дати народження для поточного року
        birthday_this_year = birthday.replace(year=today.year)
        
        # Якщо день народження вже минув у поточному році, розглянемо дату на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        # Перевірка, чи день народження знаходиться в діапазоні наступних 7 днів
        if today <= birthday_this_year <= end_date:
            # Перевірка, чи припадає день народження на вихідний (субота чи неділя)
            if birthday_this_year.weekday() >= 5:  # 5 = субота, 6 = неділя
                # Перенесення дати привітання на наступний понеділок
                while birthday_this_year.weekday() != 0:
                    birthday_this_year += timedelta(days=1)
            
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays

# Приклад використання функції:
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Alex Job", "birthday": "1986.07.05"},
    {"name": "Michel Bob", "birthday": "1977.07.08"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
