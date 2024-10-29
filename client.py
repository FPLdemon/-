import sqlite3
import psycopk

class Client:
    def __init__(self, surname, phone_number, bonus_points=0):
        self.surname = surname
        self.phone_number = phone_number
        self.bonus_points = bonus_points

    def __str__(self):
        return f"Клиент: {self.surname}, Телефон: {self.phone_number}, Баллы: {self.bonus_points}"

class ClientDatabase:
    def __init__(self, database_filename='clients.db'):
        self.conn = sqlite3.connect(database_filename)
        self.create_table()

    def create_table(self):
        create_table_sql = '''
            CREATE TABLE IF NOT EXISTS clients1 (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                surname TEXT NOT NULL,
                phone_number TEXT NOT NULL,
                bonus_points INTEGER DEFAULT 0
            );
        '''
        self.conn.execute(create_table_sql)

    def add_client(self, client):
        insert_sql = f'''
            INSERT INTO clients1 (surname, phone_number, bonus_points) 
            VALUES ('{client.surname}', '{client.phone_number}', {client.bonus_points});
        '''
        self.conn.execute(insert_sql)
        self.conn.commit()

    def find_client_by_phone(self, phone_number):
        select_sql = f'''SELECT surname, phone_number, bonus_points FROM clients1 WHERE phone_number='{phone_number}';'''
        cursor = self.conn.execute(select_sql)
        row = cursor.fetchone()
        if row:
            surname, phone_number, bonus_points = row
            return Client(surname, phone_number, bonus_points)
        else:
            return None

    def get_all_clients(self):
        select_sql = '''SELECT surname, phone_number, bonus_points FROM clients1;'''
        cursor = self.conn.execute(select_sql)
        rows = cursor.fetchall()
        clients = []
        for row in rows:
            surname, phone_number, bonus_points = row
            clients.append(Client(surname, phone_number, bonus_points))
        return clients

    def __del__(self):
        self.conn.close()

# Создание базы данных клиентов
db = ClientDatabase()

# Добавление клиентов
db.add_client(Client("Иванов", "1234567890"))
db.add_client(Client("Петров", "9876543210", 100))



