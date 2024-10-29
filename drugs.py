import sqlite3
import psycopk

class Pharmacy:
    def __init__(self, db_name='pharmacy.db'):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS medicine2 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                prescription TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def add_medicine(self, name, description, prescription, quantity, price):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('''
            INSERT INTO medicine2 (name, description, prescription, quantity, price)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, description, prescription, quantity, price))
        conn.commit()
        conn.close()

    def purchase_medicine(self, name, quantity):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('''
            UPDATE medicine2
            SET quantity = quantity - ?
            WHERE name = ? AND quantity >= ?
        ''', (quantity, name, quantity))
        
        if c.rowcount == 0:
            print("Недостаточно товара или препарат не найден.")
        else:
            print("Покупка выполнена успешно.")
        
        conn.commit()
        conn.close()

    def get_price_by_name(self, name):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('SELECT price FROM medicine2 WHERE name = ?', (name,))
        price = c.fetchone()
        conn.close()
        
        if price:
            return price[0]  # Возвращаем только цену
        return None

    def get_all_medicines(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute('SELECT * FROM medicine2')
        medicines = c.fetchall()
        
        for medicine in medicines:
            print(f'ID: {medicine[0]}, Название: {medicine[1]}, Описание: {medicine[2]}, Рецепт: {medicine[3]}, Количество: {medicine[4]}, Цена: {medicine[5]}')
        
        conn.close()

# Пример использования
pharmacy = Pharmacy()
pharmacy.add_medicine("Парацетамол", "Обезболивающее средство", "Нет", 100, 50.0)
pharmacy.add_medicine("Ибуфен", "Противовоспалительное средство", "Нет", 50, 75.0)



