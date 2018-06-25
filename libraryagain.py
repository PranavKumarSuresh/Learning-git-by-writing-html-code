class Lib:
	
	def __init__(self,books):
		self.bookList = books

	def displayBooks(self):
		print("Books available for you")
		for book in self.bookList:
			print(book)

	def lendBook(self,book):
		self.bookList.remove(book)
		print("removed ",book)
		
	def acceptBook(self,book):
		self.bookList.append(book)
		print ("added ",book)


class Customer:
	pass
	def borrowBook(self):
		self.book = input()
		return self.book

	def returnBook(self):
		self.book = input()
		return self.book

books = ["w","e","r","t","y","yr"]
lib = Lib(books)
cust = Customer()



while True:

	print("1 to display")
	print("2 to borrow")
	print("3 to return")
	print("4 to quit")

	custinput = int(input())

	if custinput is 1:
		lib.displayBooks()
	elif custinput is 2:
		print("borrowing book:")
		lib.lendBook(cust.borrowBook())
		
	elif custinput is 3:
		print("returnign book:")
		lib.acceptBook(cust.returnBook())
		

	else:
		quit()	