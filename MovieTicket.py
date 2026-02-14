class MovieTicket:
    ticket_price = 200

    def __init__(self, movie_name, seats=0):
        self.movie_name = movie_name
        self.seats = seats

    def book_seat(self, count):
        self.seats += count
        return f"{count}"

    def cancel_booking(self, count):
        if count <= self.seats:
            self.seats -= count
            return f"{count}"
        return "Cancellation not possible"

    def calculate_ticket_price(self):
        return self.seats * MovieTicket.ticket_price

    @classmethod
    def update_ticket_price(cls, new_price):
        cls.ticket_price = new_price

t1 = MovieTicket("Inception")
t1.book_seat(3)
print("Total Price:", t1.calculate_ticket_price())
MovieTicket.update_ticket_price(250)
print("Updated Total Price:", t1.calculate_ticket_price())
t1.cancel_booking(1)
print("Total Price after cancellation:", t1.calculate_ticket_price())