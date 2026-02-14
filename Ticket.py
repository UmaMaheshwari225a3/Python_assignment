class Ticket:
    base_fare = 100

    def __init__(self, ticket_id, distance):
        self.ticket_id = ticket_id
        self.distance = distance   
        self.is_booked = False
        self.is_cancelled = False


    def book_ticket(self):
        if self.is_cancelled:
            print("Cannot book cancelled ticket.")
        else:
            self.is_booked = True
            print(f"Ticket {self.ticket_id} booked successfully.")


    def cancel_ticket(self):
        if self.is_booked:
            self.is_cancelled = True
            print(f"Ticket {self.ticket_id} cancelled.")
        else:
            print("Ticket not booked yet.")

 
    def calculate_fare(self):
        if not self.is_booked:
            print("Book the ticket first.")
            return 0
        return Ticket.base_fare + (self.distance * 5)

 
    @classmethod
    def update_base_fare(cls, new_fare):
        cls.base_fare = new_fare
        print(f"Base fare updated to ₹{new_fare}")

t1 = Ticket(1, 10) 

t1.book_ticket()
print("Fare:", t1.calculate_fare())

Ticket.update_base_fare(250)
print("Updated Fare:", t1.calculate_fare())
