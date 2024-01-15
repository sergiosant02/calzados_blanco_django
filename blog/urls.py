from django.urls import path, include
from. import views

urlpatterns = [
    path("", views.blog, name="blog"),
    path("category/<int:category_id>/", views.category, name="category"),
    
]
