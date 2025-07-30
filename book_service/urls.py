
from django.contrib import admin
from django.urls import path, include
from book import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('book.urls')),
    path('books/', views.book_view, name='book_view'),
    path('book/', views.book_input, name='book_add'),
    path('books/edit/<int:id>/', views.book_input, name='book_edit'), 
    path('books/delete/<int:id>/', views.book_delete, name='book_delete'), 
]
