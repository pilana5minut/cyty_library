from django.contrib import admin
from . models import Book, Author


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'sbin', 'pages', 'status',]
    list_display_links = ['title', 'author', 'sbin',]
    ordering = ['title',]
    actions_on_bottom = True


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    ordering = ['name', 'id']
    actions_on_bottom = True


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
