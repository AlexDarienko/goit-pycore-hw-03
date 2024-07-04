import random

def get_numbers_ticket(min, max, quantity):
    # Перевірка на відповідність параметрів заданим обмеженням
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []
    
    # Генерація унікальних випадкових чисел у заданому діапазоні
    numbers = random.sample(range(min, max + 1), quantity)
    
    # Повернення відсортованого списку
    return sorted(numbers)

# Приклад використання функції:
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)