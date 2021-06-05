from rest_framework.generics import ListAPIView

from .serializers import CategorySerializers
from ..models import Category


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
