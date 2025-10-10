balance_global = 1000

def buy(balance, price):
    if balance >= price:
        balance -= price
    print(f"Локальная: {balance}")
    return balance

balance_global = buy(balance_global, 500) # 500
print(balance_global)
