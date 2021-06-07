from django.urls import path

from .api_views import (
    CategoryListAPIView,
    CustomerListAPIview
)


urlpatterns = [
    path('categories/<str:id>', CategoryListAPIView.as_view(), name='categories'),
    path('customers/', CustomerListAPIview.as_view(), name='customers_list'),
]
