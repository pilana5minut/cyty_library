from django.contrib import admin
from . models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'sbin', 'pages', 'status',]
    ordering = ['title',]
    list_display_links = ['title', 'author', 'sbin',]

    actions_on_bottom = True


admin.site.register(Book, BookAdmin)
