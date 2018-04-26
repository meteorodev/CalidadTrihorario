# _*_ coding: utf-8 *_*
#Autor: Darwin Rosero Vaca
#Descripción: lee la configuración generada een la base inicial que esta dentro de sqlite3

import sqlite3
import os

class LoadConfig():
    """"""
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __init__(self):
        """Constructor vacio"""

    def getConfig(self,user):
        print("##############################################3")
        print("##############################################3")
        print("getconfig from util package")
        print(self.BASE_DIR)

        base=os.path.join(self.BASE_DIR, 'db.sqlite3')
        print(base)
        con_bd = sqlite3.connect(base)
        print()
        cursor=con_bd.cursor()
        cursor.execute('SELECT type,name,sql,tbl_name FROM `main`.sqlite_master;')
        tablas = cursor.fetchone()  # retrieve the first row
        if tablas is None:
            print("La base esta vacia")
        else:
            print("Si hay datos en la base")

        #print(user1[0])  # Print the first column retrieved(user's name)
