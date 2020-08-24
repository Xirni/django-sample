from django.http import HttpResponse
from rest.models import Product
from rest_framework import serializers, viewsets

def index(request):
    return HttpResponse("Hello, world. You're at the rest index.")



# Serializers define the API representation.
class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']

# ViewSets define the view behavior.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

