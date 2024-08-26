from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('example/', views.example, name='example'),  # Example URL pattern

    path('example2/', views.Example2.as_view()),

    path('example3/', views.ExampleModelListCreateView.as_view(), name='example-list-create'),
    path('example3/<int:pk>/', views.ExampleModelRetrieveUpdateDestroyView.as_view(), name='example-retrieve-update-destroy'),
]
