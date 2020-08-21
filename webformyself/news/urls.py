from django.urls import path
from .views import *

urlpatterns = [
    # path('', index, name='home'),
    path('', HomeNews.as_view(), name='home'), #при добавлении ListView во views.py
    # path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/add_news/', add_news, name='add_news'),
]
