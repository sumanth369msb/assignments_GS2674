class class1:
    def __init__(self,author_name):
        self.author_name = author_name
        self.book = []
        self.emails = []
    def add_book(self, book_title):
        self.book.append(book_title)
    def add_email(self, email_subject):
        self.emails.append(email_subject)
    def get_books(self):
        return self.book
    def get_emails(self):
        return self.emails
class class2:
    def __init__(self, title):
        self.title = title
    def get_title(self):
        return self.title
class class3(class2):
    def __init__(self, title, date):
        super().__init__(title)
        self.date = date
    def get_date(self):
        return self.date
class class4(class2):
    def __init__(self, title, to):
        super().__init__(title)
        self.to = to
    def get_to(self):
        return self.to
