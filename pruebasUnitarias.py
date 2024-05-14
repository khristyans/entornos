import unittest

# Supongamos que tenemos una clase llamada LibraryManagement que queremos probar
from library_management import LibraryManagement

class TestLibraryManagement(unittest.TestCase):
    
    def setUp(self):
        # Crear una instancia de LibraryManagement para usarla en todas las pruebas
        self.library = LibraryManagement()

    def test_add_book(self):
        # Verificar si el método add_book() agrega un libro correctamente
        self.library.add_book("Harry Potter", "J.K. Rowling")
        self.assertIn("Harry Potter", self.library.books)

    def test_remove_book(self):
        # Verificar si el método remove_book() elimina un libro correctamente
        self.library.add_book("Lord of the Rings", "J.R.R. Tolkien")
        self.library.remove_book("Lord of the Rings")
        self.assertNotIn("Lord of the Rings", self.library.books)

    def test_find_books_by_author(self):
        # Verificar si el método find_books_by_author() devuelve los libros de un autor dado
        self.library.add_book("The Hobbit", "J.R.R. Tolkien")
        self.library.add_book("The Silmarillion", "J.R.R. Tolkien")
        books_by_tolkien = self.library.find_books_by_author("J.R.R. Tolkien")
        self.assertEqual(books_by_tolkien, ["The Hobbit", "The Silmarillion"])

    #Ampliación 
    
    def test_add_existing_book(self):
        # Probar agregar un libro que ya está en la biblioteca
        self.library.add_book("Harry Potter", "J.K. Rowling")
        self.library.add_book("Harry Potter", "J.K. Rowling")  # Intentar agregar el mismo libro otra vez
        self.assertEqual(len(self.library.books), 1)  # La longitud del diccionario debe ser 1

    def test_remove_nonexistent_book(self):
        # Probar eliminar un libro que no está en la biblioteca
        self.library.remove_book("Nonexistent Book")
        self.assertEqual(len(self.library.books), 0)  # La biblioteca no debe cambiar

    def test_find_books_by_nonexistent_author(self):
        # Probar buscar libros de un autor que no tiene libros en la biblioteca
        books_by_nonexistent_author = self.library.find_books_by_author("Nonexistent Author")
        self.assertEqual(books_by_nonexistent_author, [])

    def test_add_book_with_empty_title(self):
        # Probar agregar un libro con un título vacío
        self.library.add_book("Harry Potter", "Author")
        self.assertNotIn("", self.library.books)  # El libro con título vacío no debe ser agregado
        #Fail 

    def test_add_book_with_empty_author(self):
        # Probar agregar un libro con un autor vacío
        self.library.add_book("Book Title", "Cristian")
        self.assertNotIn("Book Title", self.library.books)  # El libro con autor vacío no debe ser agregado
        #Fail 

    #Actualización 
    
    def test_count_books(self):
        self.library.add_book("Book 1", "Author 1")
        self.library.add_book("Book 2", "Author 2")
        self.library.add_book("Book 3", "Author 3")
        self.assertEqual(self.library.count_books(), 3)


if __name__ == '__main__':
    unittest.main()