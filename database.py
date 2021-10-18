import sqlite3

class Database(object):
    DB_LOCATION = "DataBase/dados.db"

    def __init__(self):
        self.connection = sqlite3.connect(self.DB_LOCATION)
        self.cur = self.connection.cursor()

    def close(self):
        self.connection.close()

    def execute(self, new_data):
        """execute a row of data to current cursor"""
        self.cur.execute(new_data)

    def show_tables(self):
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        print(self.cur.fetchall())
        

    def show_collumns(self, table):
        cursor = self.cur.execute(f'select * from {table}')
        print([description[0] for description in cursor.description])

    def insert_data(self, tabela,  new_data, columns=''):
        self.cur.execute(f'''INSERT INTO {tabela} {columns} VALUES {new_data}''')
        self.commit()
 
    def create_table_msg(self):
        self.cur.execute(f'''CREATE TABLE IF NOT EXISTS Menssagens (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                                                canal_id INTERGER,
                                                                menssagem text NOT NULL,
                                                                data TEXT,
                                                                FOREIGN KEY(canal_id) REFERENCES Canais(id)
                                                                )''')
    def create_table_canal(self):
        self.cur.execute(f'''CREATE TABLE IF NOT EXISTS Canais (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                                                nome text (32),
                                                                data TEXT
                                                                )''')

    def get_msg_by_colum(self, colum, search):
        cursor = self.cur.execute(f'''select * from Menssagens where {colum} like "%{search}%"''')
        print(self.cur.fetchall())

    def get_msg_by_canal(self, canal):
        cursor = self.cur.execute(f'''select * from {canal}''')
        print(self.cur.fetchall())

    def get_data(self, codigo:str):
        self.cur.execute(codigo)
        return self.cur.fetchall()

    def get_data(self, codigo:str):
        self.cur.execute(codigo)
        return self.cur.fetchall()

    def commit(self):
        self.connection.commit()


# a = Database()
# a.create_table_canal()
# a.create_table_msg()
# # dados =f"('{nome}', '{item['site']}', '{item['preco']}', '{link}', '{data}')"     
# a.insert_data('Canais', "('TOCA DO COELHO',  '18/08/2021')", '(nome, data)')
# #a.get_msg_by_colum('')

