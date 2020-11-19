from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from .models import Pizza
from .serializer import PizzaSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def pizza_list(request):
    if request.method == 'GET': 
        pizza = Pizza.objects.all()
        Pizza_serializer = PizzaSerializer(pizza, many=True)
        return JsonResponse(Pizza_serializer.data, safe=False)
 
    elif request.method == 'POST':
        Pizza_data = JSONParser().parse(request)
        Pizza_serializer = PizzaSerializer(data=Pizza_data)
        if Pizza_serializer.is_valid():
            Pizza_serializer.save()
            return JsonResponse(Pizza_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(Pizza_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Pizza.objects.all().delete()
        return JsonResponse({'message': '{} Pizza were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
   

@api_view(['GET', 'PUT', 'DELETE'])
def pizza_detail(request, pk):
    try: 
        pizza = Pizza.objects.get(pk=pk) 
    except Pizza.DoesNotExist: 
        return JsonResponse({'message': 'The pizza does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        Pizza_serializer = PizzaSerializer(pizza) 
        return JsonResponse(Pizza_serializer.data) 
 
    elif request.method == 'PUT': 
        Pizza_data = JSONParser().parse(request) 
        Pizza_serializer = PizzaSerializer(pizza, data=Pizza_data) 
        if Pizza_serializer.is_valid(): 
            Pizza_serializer.save() 
            return JsonResponse(Pizza_serializer.data) 
        return JsonResponse(Pizza_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        pizza.delete() 
        return JsonResponse({'message': 'Pizza was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
  





