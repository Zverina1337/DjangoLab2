from django.urls import include, path
from .views import AuthorViewSet, BookViewSet


urlpatterns = [
    path('authors/', AuthorViewSet.as_view({'get': 'list'})),
    path('author/<int:pk>', AuthorViewSet.as_view({'get': ''})),


    path('books/', BookViewSet.as_view({'get': 'list'})),
    path('book/<int:pk>', BookViewSet.as_view({'get': ''}))

]
