from django.contrib import admin
from django.urls import path
from core.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",frontpage,name="frontpage"),
    path("sales/",salepage,name="sales"),
    path("product/<str:pk>/",product_page,name="sproduct")
]
