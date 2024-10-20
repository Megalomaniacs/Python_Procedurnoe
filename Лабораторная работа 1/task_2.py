# TODO Найдите количество книг, которое можно разместить на дискете



dsize = 1.44
dsizebyte = dsize * 1024 * 1024

book_pages = 100
book_strings = 50
book_symbols = 25
book_symbolzise = 4

rez = dsizebyte / (book_pages * book_strings * book_symbols * book_symbolzise)
rezr = round(rez)
print("Количество книг, помещающихся на дискету:", rezr)