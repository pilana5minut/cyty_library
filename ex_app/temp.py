from ex_app.models import Book, Author

for book in Book.objects.all():
    # Найти запись автора по имени
    author = Author.objects.get(name=book.author)
    # Обновить поле author модели Book,
    # чтобы оно ссылалось на запись в Author
    book.author = author
    book.save()
