from book_class import Book

with open("book.text", 'w') as f:
    f.write("Avengers Endgame\t$1.7747 billion\n")
    f.write("Frozen 2\t$1.450 billion")

with open("book.text", 'r') as f:
    data = f.read()

movies = data.split("\n")
movie1 = Book(movies[0].split("\t")[0], movies[0].split("\t")[1])
movie2 = Book(movies[1].split("\t")[0], movies[1].split("\t")[1])

print(movie1)
print(movie2)
