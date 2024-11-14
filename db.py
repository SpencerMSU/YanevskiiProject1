import sqlite3
class DatabaseManager:
    #Подключение к БД
    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        self.cur = self.conn.cursor()

    #Команда для запуска хранимых процедур и SQL инструкций в виде текстовых строк.
    def query(self, arg, values=None):
        if values is None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        self.conn.commit()
    #Работа с одним элементов
    def fetchone(self, arg, values=None):
        if values is None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchone()
    #Работа со всеми элементами строки/столбца
    def fetchall(self, arg, values=None):
        if values is None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchall()

    def __del__(self):
        self.conn.close()




