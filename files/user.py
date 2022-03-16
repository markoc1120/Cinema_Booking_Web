class User:

    def __init__(self, name_):
        self.name = name_

    def buy(self, seat_, card, ticket):
        if seat_.is_free():
            if card.validate(seat_.price) is None:
                print('There was a problem with your card!')
            else:
                ticket.to_pdf()
                seat_.occupy()
                print('Purchase completed.')
        else:
            print('That seat has been taken!')
