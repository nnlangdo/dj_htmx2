from django.contrib import admin
from django.urls import path
from app.views import create_contact, ContactList, delete_contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-contact/', create_contact, name='create-contact'),
    path("contacts/", ContactList.as_view(), name='contact-list'),
    path('delete-contact/<int:pk>/', delete_contact, name='delete-contact'),
]