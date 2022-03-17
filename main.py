from files.card import Card
from files.seat import Seat
from files.user import User
from files.ticket import Ticket
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, redirect, url_for, flash, abort
from forms import RegisterForm



# name = input('Your full name: ')
# seat = input('Preferred seat: ')
# card_type = input('Your card type: ')
# card_number = input('Your card number: ')
# card_cvc = input('Your card cvc: ')
# card_holder_name = input('Card holder name: ')
#
# user1 = User(name)
# seat1 = Seat('cinema.db', user1, seat)
# card1 = Card('banking.db', card_type, card_number, card_cvc, card_holder_name)
# ticket1 = Ticket(seat1)
# user1.buy(seat1, card1, ticket1)

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/booking')
def booking():
    form = RegisterForm()
    return render_template("booking.html", form=form)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
