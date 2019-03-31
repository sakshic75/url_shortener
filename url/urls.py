from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('url', views.url),
    path('url/<str:unique_key>', views.redirection)
]
