let names = ['Булат', 'Денис', 'Павел', 1,2,5, true , []]
console.log(names[0])
names.push('Новый элемент')
console.log(names)
names.splice(0, 1)
names.pop() // удаляет последний элемент списка
console.log(names.length)



let books = ["Гарри Поттер и философский камень", "Гарри Поттер и тайная комната ", "Гарри Поттер и Узник Азкабана"];
books.splice(1, 1, "Хроники Нарнии");
console.log(books);
books.splice(3, 0, "Новая книга")
