import sqlite3

class Conexion:

    @staticmethod
    def conectar():
        return sqlite3.connect("facturacion_comercial.db")