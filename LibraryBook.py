class LibraryBook:
    fine_per_day = 5

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False
        self.days_late = 0


    def issue_book(self):
        if not self.is_issued:
            self.is_issued = True
            print(f"Book '{self.title}' issued successfully")
        else:
            print("Book already issued")

   
    def return_book(self, days_late):
        if self.is_issued:
            self.is_issued = False
            self.days_late = days_late
            print(f"Book '{self.title}' returned")
        else:
            print("Book was not issued")

    
    def calculate_fine(self):
        if self.days_late > 0:
            fine = self.days_late * LibraryBook.fine_per_day
            print("Fine amount:", fine)
            return fine
        else:
            print("No fine")
            return 0

   
    @classmethod
    def update_fine_per_day(cls, new_fine):
        cls.fine_per_day = new_fine
        print("Fine per day updated to:", new_fine)

b1 = LibraryBook(101, "Book1", "Guido")

b1.issue_book()
b1.return_book(4)
b1.calculate_fine()

LibraryBook.update_fine_per_day(10)

b1.calculate_fine()
