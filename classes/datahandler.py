import sqlite3

class DataHandler:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def execute(self, query, params=None):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()

    def insert_data(self, table_name, data):
        self.execute(f"INSERT INTO {table_name} VALUES ({', '.join(['?'] * len(data))})", data)
        self.conn.commit()

    def get_data(self, table_name, condition=None):
        if condition:
            condition = f"WHERE {condition}"
        else:
            condition = ''
        query = f"SELECT * FROM {table_name} {condition}"
        self.execute(query,'')
        return self.fetchall()

    def delete_data(self, table_name, condition=None):
        if condition:
            condition = f"WHERE {condition}"
        else:
            condition = ''
        query = f"DELETE FROM {table_name} {condition}"
        self.execute(query,'')
        self.conn.commit()

    def update_data(self, table_name, data, condition=None):
        if condition:
            condition = f"WHERE {condition}"
        else:
            condition = ''
        query = f"UPDATE {table_name} SET {', '.join([f'{key} = ?' for key in data.keys()])} {condition}"
        self.execute(query, list(data.values()))
        self.conn.commit()

    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
        self.execute(query, '')
        self.conn.commit()