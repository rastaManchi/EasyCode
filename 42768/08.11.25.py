import random

issued_card_numbers = []

def generate_unique_card_number():
    
    while True:
        card_number = random.randint(1000000000000000, 9999999999999999)
        
        if card_number not in issued_card_numbers:
            issued_card_numbers.append(card_number)
            print(f"номер карты: {card_number}")
            break
        else:
            print(f"номер {card_number} уже существует, генерируем новый...")

print("=== выдача первой карты ===")
generate_unique_card_number()

print("\n=== выдача второй карты ===")
generate_unique_card_number()

print(f"\nвсего выдано карт: {len(issued_card_numbers)}")
print(f"выданные номера: {issued_card_numbers}")