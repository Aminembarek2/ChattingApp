from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/login/', admin.site.urls),
    path('',include('Chat.urls'))
]
