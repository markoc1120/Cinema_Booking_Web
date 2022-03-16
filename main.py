from files.card import Card
from files.seat import Seat
from files.user import User
from files.ticket import Ticket

name = input('Your full name: ')
seat = input('Preferred seat: ')
card_type = input('Your card type: ')
card_number = input('Your card number: ')
card_cvc = input('Your card cvc: ')
card_holder_name = input('Card holder name: ')

user1 = User(name)
seat1 = Seat('cinema.db', user1, seat)
card1 = Card('banking.db', card_type, card_number, card_cvc, card_holder_name)
ticket1 = Ticket(seat1)
user1.buy(seat1, card1, ticket1)
