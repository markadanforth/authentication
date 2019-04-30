import mysql.connector
from typing import List

class Database:

    def Connection(self):
        return mysql.connector.connect(
            user="enter info",
            password="enter info",
            host="enter info",
            database="enter info")

    def CreateUsersTable(self):
        sql = \
        """CREATE TABLE users (
        `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        firstname VARCHAR(50) NOT NULL,
        lastname VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        password VARCHAR(100) NOT NULL,
        timestamp timestamp NOT NULL
        )ENGINE=InnoDB;"""

        conn = self.Connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        cursor.close()
        conn.close()

    def GetUser(self,email):
        sql = "SELECT * FROM users WHERE email = %s"

        db = self.Connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute(sql, (email,))
        user = cursor.fetchone()
        cursor.close()
        db.close()

        return user

    def CreateUser(self,user):
        sql = "INSERT INTO `users` " \
            "(`firstname`, `lastname`, `email`, `password`, `timestamp`) " \
            "VALUES (%s, %s, %s, %s, NOW())"

        conn = self.Connection()
        cursor = conn.cursor()
        cursor.execute(sql,
                      (user["firstname"],
                       user["lastname"],
                       user["email"],
                       user["password"]))
        cursor.close()
        conn.commit()
        conn.close()