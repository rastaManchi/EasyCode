text = 'http://text.ru/?offer_id=privetTIHON&locale=ru'

offer_id = text.split('?offer_id=')[1].split('&')[0]

print(offer_id)
new_url = f'https://www.yoybuy.com/api/transaction/product/ProductSearchQueryProductDetail?country=ru&offerId={offer_id}'

print(new_url)