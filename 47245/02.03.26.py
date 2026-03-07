import tkinter as tk
from tkinter import messagebox, scrolledtext
import sqlite3
from datetime import datetime


# Создание основного окна
root = tk.Tk()
root.title("Блокнот")


# Подключение к базе данных
conn = sqlite3.connect('notes.db')
cursor = conn.cursor()


# Создание базы данных и таблицы, если они не существуют
cursor.execute('''
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY,
        note TEXT NOT NULL,
        date TEXT NOT NULL
        )
    ''')


#Сохранение изменений в базе данных
conn.commit()


# Функция для добавления заметки
def add_note():
    note = text_area.get("1.0", tk.END).strip()  # Получаем текст из текстового поля
    if note: # Если текст записки НЕ пустой...
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Получаем текущее время
        cursor.execute('INSERT INTO notes (note, date) VALUES (?, ?)', (note, date)) # Вставляем новую заметку в БД
        messagebox.showinfo("Успех", "Заметка добавлена!") # Сообщаем о добавлении заметки
        text_area.delete("1.0", tk.END)  # Очищаем текстовое поле после добавления заметки
        conn.commit() #Сохранение изменений в базе данных
    else:
        messagebox.showerror("Ошибка", "Вы ввели пустую заметку!") # Сообщаем об ошибке
        

def delete_note(note_id):
    cursor.execute('''DELETE FROM notes
                   WHERE id=?''', [note_id])
    conn.commit()
    messagebox.showinfo("Успех", 'Заметка удалена')
    


# Функция для отображения всех заметок
def show_notes():
    cursor.execute('SELECT id, note, date FROM notes') # Выбираем поля note и date из всех записей в БД
    notes = cursor.fetchall() # Получаем все полученные записи
   
    if notes: # Если какие-то записи в БД есть...
        notes_window = tk.Tk()
        notes_window.title("Все заметки")
       
        for note_id, note, date in notes:
            note_frame = tk.Frame(notes_window)
            note_frame.pack(fill="x", padx=10, pady=5)
            
            note_label = tk.Label(note_frame, text=f"{date}: {note}", wraplength=400)
            note_label.pack(anchor='w', padx=10, pady=5)
            
            delete_button = tk.Button(note_frame, text="Удалить", command=lambda id=note_id: delete_note(id))
            delete_button.pack(side='right')
            
            
           
    else: # Если в БД пусто...
        messagebox.showinfo("Информация", "Нет заметок для отображения.") # Сообщаем о невозможности отобразить заметки




# Создание текстового поля для ввода заметки
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=15)
text_area.pack(pady=10)


# Кнопка для добавления заметки
add_note_button = tk.Button(root, text="Добавить заметку", command=add_note)
add_note_button.pack(pady=10)


# Кнопка для отображения всех заметок
show_notes_button = tk.Button(root, text="Показать все заметки", command=show_notes)
show_notes_button.pack(pady=10)


# Запуск главного цикла приложения
root.mainloop()
