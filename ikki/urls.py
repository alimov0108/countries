from django.contrib import admin
from django.urls import path
from core.views import index, AboutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about/', AboutView.as_view()),
]
