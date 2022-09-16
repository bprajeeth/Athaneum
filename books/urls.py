
from django.contrib import admin
from django.urls import path,include
from books.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('reserve/', make_reservation),
    path('fail/', failure),
    path('success/', successfull),
    path('users/',show_reservation),
    path('cancel/',cancel_reservation),
]
