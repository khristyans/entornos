class LibraryManagement:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author):
        if title in self.books:
            print(f"El libro '{title}' ya está en la biblioteca.")
        else:
            self.books[title] = author
            print(f"El libro '{title}' de {author} ha sido agregado a la biblioteca.")

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            print(f"El libro '{title}' ha sido eliminado de la biblioteca.")
        else:
            print(f"El libro '{title}' no está en la biblioteca.")

    def find_books_by_author(self, author):
        books_by_author = []
        for title, auth in self.books.items():
            if auth == author:
                books_by_author.append(title)
        return books_by_author
    
    #Actualización 
    
    def count_books(self):
        return len(self.books)
    
print("Hola")