import sqlite3


class Card:

    def __init__(self, db, type_, number, cvc, holder_name):
        self.database = db
        self.type = type_
        self.number = number
        self.cvc = cvc
        self.holder_name = holder_name

    def validate(self, price):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
            SELECT *  FROM "Card" WHERE "type"=? and "number"=? and "cvc"=? and "holder"=? and "balance">=?
            """, [self.type, self.number, self.cvc, self.holder_name, price])
        result = cursor.fetchall()
        self.make_payment(connection, price)
        connection.close()
        return result

    def make_payment(self, connection, price):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT "balance" FROM "Card" WHERE "type"=? and "number"=? and "cvc"=? and "holder"=?
            """, [self.type, self.number, self.cvc, self.holder_name])
        balance = cursor.fetchall()[0][0]
        new_balance = balance - price
        connection.execute("""
        UPDATE "Card" SET "balance"=? WHERE "type"=? and "number"=? and "cvc"=? and "holder"=?
        """, [new_balance, self.type, self.number, self.cvc, self.holder_name])
        connection.commit()