import sqlite3


class Seat:

    def __init__(self, db, user_, seat_):
        self.database = db
        self.user = user_
        self.seat = seat_.capitalize()
        self.price = self.get_price()

    def get_price(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
                SELECT "price" FROM "Seat" WHERE "seat_id"=?
                """, [self.seat])
        result = cursor.fetchall()
        connection.close()
        return result[0][0]

    def is_free(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "taken" FROM "Seat" WHERE "seat_id"=?
        """, [self.seat])
        result = cursor.fetchall()
        connection.close()
        return True if result[0][0] == 0 else False

    def occupy(self):
        connection = sqlite3.connect(self.database)
        connection.execute("""
            UPDATE "Seat" SET "taken"=? WHERE "seat_id"=?
            """, [1, self.seat])
        connection.commit()
        connection.close()
