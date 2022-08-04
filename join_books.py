import zipfile
from os import listdir


def read_book(archive_name):
    zf = zipfile.ZipFile(f'books/{archive_name}')
    f = zf.filelist[0]
    return zf.read(f.filename).decode('cp1251')


books_list = listdir('books')
texts = ('\n' * 3).join(read_book(n) for n in books_list)

result_file = open('text.txt', 'w')
result_file.write(texts)
