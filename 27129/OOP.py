class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def show_info(self):
        print(f'Название -- {self.name}\nАвтор -- {self.author}\n')

b1 = Book('Название1', 'Автор1')
b2 = Book('Название2', 'Автор2')
b1.show_info()
b2.show_info()
