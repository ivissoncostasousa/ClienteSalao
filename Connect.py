import mysql.connector
from mysql.connector import Error


class Connect:
    def __init__(self) -> None:
        pass
    
    def conectar(self):
        try:
            con = mysql.connector.connect(host="localhost", database="db_salao", user="root", password="aluno99")
            if con.is_connected():
                return con, True
        except Error as e:
            return e, False