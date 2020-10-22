from django.urls import path
# from .views import view_function
from .views import CalculationViewTemplate

urlpatterns=[
    # path('', view_function, name="home"),
    path('', 
    CalculationViewTemplate.as_view(num=100), 
    name="calc"),
]