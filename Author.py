# Boris Pizha 
#Creating a new class called Author
class Author:

    def __init__(self, name):
        self.name = name
        self.books = []
    
    def publish(self, title):
        self.books.append(title)

# Handling the books that are not published yet
    def __str__(self):
        titles = ', '.join(self.books) or 'No published books'
        return f'{self.name}. Books:{titles}'
        
# List of the books added to the class(Author's Name, and books published)        
def main():

    twain = Author('Mark Twain ')
    twain.publish(' The Advantures of Huckleberry Finn ')
    twain.publish(' The Advanture of Tom ')
    print(twain)
    
    boris = Author('Boris')
    print(boris)

main()
