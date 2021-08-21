from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import get_user_model,get_user


from .serializers import *
from .models import *


@api_view(['POST','PUT','DELETE'])
def salesApi(request):
    if request.method== 'POST':
        data=request.data
        serializer=SaleSerialzer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created successfully'})
        return Response(serializer.errors)

    if request.method== 'PUT':
        id = request.data.get('id')
        sm=Sales.objects.get(pk=id)
        serializer=SaleSerialzer(sm,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data is updated"})
        return Response(serializer.errors)

    if request.method== "DELETE":

        id=request.data.get('id')
        sm=Sales.objects.get(pk=id)
        SaleSerialzer.delete()
        return Response({'msg':"Data Deleted"})

#@api_view(['GET'])
# def salesViewall(request):
#     user=get_user(request)
#     if get_user(request):
#         if request.method == 'GET':
# 
#             # id = request.data.get('id')
#             #
#             # if id is not None:
#             #     sm = Sales.objects.get(pk=id)
#             #     serializer= SalesSerializer(data=sm)
#             #     return Response(serializer.data)
# 
#             #sm=Sales.objects.get(u)
# 
#             print(sm)
#             ss=SaleSerialzer(data=sm,many=True)
# 
#             print(ss.data,'salesmana')
#             return Response(ss.data)
# 
