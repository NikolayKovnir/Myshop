from django.urls import path

from .api_views import (
    CategoryListAPIView,
    SmartphoneListAPIView,
    NotebookListAPIView,
    SmartphoneDetailView,
    CustomerListAPIview
)


urlpatterns = [
    path('categories/<str:id>', CategoryListAPIView.as_view(), name='categories'),
    path('customers/', CustomerListAPIview.as_view(), name='customers_list'),
    path('smartphones/', SmartphoneListAPIView.as_view(), name='smartphones_list'),
    path('notebooks/', NotebookListAPIView.as_view(), name='notebooks_list'),
    path('smartphones/<str:id>', SmartphoneDetailView.as_view(), name='smartphone_detail'),
]
