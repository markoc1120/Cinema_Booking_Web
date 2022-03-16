import os
import random
import string
import webbrowser
from fpdf import FPDF


class Ticket:
    filename = './pdf/ticket.pdf'

    def __init__(self, seat_):
        self.id = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        self.user = seat_.user
        self.price = seat_.price
        self.seat = seat_

    def to_pdf(self):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Your Digital Ticket', border=0, align='C', ln=1)

        pdf.set_font(family="Times", size=14, style='B')
        # Insert name
        pdf.cell(w=100, h=40, txt='Name:', border=0)
        pdf.set_font(family="Times", size=14)
        pdf.cell(w=150, h=40, txt=self.user.name, border=0, ln=1)

        pdf.set_font(family="Times", size=14, style='B')
        # Insert ticket_id
        pdf.cell(w=100, h=40, txt='Ticket ID:', border=0)
        pdf.set_font(family="Times", size=14)
        pdf.cell(w=150, h=40, txt=self.id, border=0, ln=1)

        pdf.set_font(family="Times", size=14, style='B')
        # Insert ticket price
        pdf.cell(w=100, h=40, txt='Price:', border=0)
        pdf.set_font(family="Times", size=14)
        pdf.cell(w=150, h=40, txt=str(self.price) + '$', border=0, ln=1)

        pdf.set_font(family="Times", size=14, style='B')
        # Insert seat number
        pdf.cell(w=100, h=40, txt='Seat Number:', border=0)
        pdf.set_font(family="Times", size=14)
        pdf.cell(w=150, h=40, txt=self.seat.seat, border=0, ln=1)

        pdf.output(self.filename)
        webbrowser.open('file://' + os.path.realpath(self.filename))
