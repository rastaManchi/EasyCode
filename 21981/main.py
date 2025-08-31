# def test():
#     # global result
#     result = 2 + 5
#     return result

# result = 0
# result = test() # result = 7
# print(result)


# def propper(shvabra):
#     print(f'Мистер Проппер помыл квартиру шваброй {shvabra}')

# propper("Швабра красивая черная")


import random

def Card():
    local_number = random.randint(1000000000000000, 9999999999999999)
    return local_number

global_number = Card()
print(f"Номер карты: {global_number}")