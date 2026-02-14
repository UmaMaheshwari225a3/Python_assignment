class HostelRoom:
    room_rent = 5000  

    def __init__(self, room_no, room_type):
        self.room_no = room_no
        self.room_type = room_type
        self.is_allocated = False

    def allocate_room(self):
        if self.is_allocated:
            print("Room already allocated.")
        else:
            self.is_allocated = True
            print(f"Room {self.room_no} allocated successfully.")

 
    def vacate_room(self):
        if self.is_allocated:
            self.is_allocated = False
            print(f"Room {self.room_no} vacated.")
        else:
            print("Room is already vacant.")

    def calculate_monthly_fee(self):
        if not self.is_allocated:
            print("Room is not allocated.")
            return 0
        return HostelRoom.room_rent

    @classmethod
    def update_room_rent(cls, new_rent):
        cls.room_rent = new_rent
        print(f"Room rent updated to ₹{new_rent}")
r1 = HostelRoom(101, "Single")
r1.allocate_room()
print("Monthly Fee:", r1.calculate_monthly_fee())
HostelRoom.update_room_rent(6000)
print("Updated Monthly Fee:", r1.calculate_monthly_fee())
r1.vacate_room()
