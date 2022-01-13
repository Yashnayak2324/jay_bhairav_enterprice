from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('contact/',views.contact,name="contact"),
    path('category',views.category,name="category"),
    path('category1/<int:pk>/',views.category1,name="category1"),
    path('Newsletter/',views.Newsletter,name="Newsletter"),
    path('about/',views.about,name="about"),
    path('catlog/',views.catlog,name="catlog"),
    path('search/',views.search,name="search")
]