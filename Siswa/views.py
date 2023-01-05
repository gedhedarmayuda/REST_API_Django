from django.shortcuts import render
from django.http.response import JsonResponse
from django.http.request import HttpRequest
from rest_framework.parsers import JSONParser
from rest_framework import status
from Siswa.models import Siswa
from Siswa.serializers import SiswaSerializer
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET', 'POST','DELETE'])
def siswa_list(request):
    # Show All
    if request.method == 'GET':
        siswa = Siswa.objects.all()
        no_siswa = request.GET.get('no_siswa',None)
        if no_siswa is not None:
            siswa = siswa.filter(no_siswa__icontains=no_siswa)
        siswa_serializer = SiswaSerializer(siswa, many=True)
        return JsonResponse(siswa_serializer.data, safe=False)
        
    # Create Object
    elif request.method == 'POST':
        siswa_data = JSONParser().parse(request)
        siswa_serializer = SiswaSerializer(data=siswa_data)
        if siswa_serializer.is_valid():
            siswa_serializer.save()
            return JsonResponse(siswa_serializer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(siswa_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'PUT','DELETE'])
def siswa_detail(request, pk):
    try:
        siswa = Siswa.objects.get(pk=pk)
    except Siswa.DoesNotExist:
        return JsonResponse({'message':'Siswa tidak ada'}, status=status.HTTP_404_NOT_FOUND)
    
    # Show single Object
    if request.method == 'GET':
        siswa_serializer = SiswaSerializer(siswa)
        return JsonResponse(siswa_serializer.data)
    
    # Update Object
    elif request.method == 'PUT':
        siswa_data = JSONParser().parse(request)
        siswa_serializer = SiswaSerializer(siswa, data=siswa_data)
        if siswa_serializer.is_valid():
            siswa_serializer.save()
            return JsonResponse(siswa_serializer.data)
        return JsonResponse(siswa_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete an Object
    elif request.method == 'DELETE':
        siswa.delete()
        return JsonResponse({'message':'Siswa telah berhasil dihapus'}, status=status.HTTP_204_NO_CONTENT)
    
    # Delete all Object
    elif request.method == 'DELETE':
        count = Siswa.objects.all().delete()
        return JsonResponse({'message':'{} Siswa telah dihapus'.format(count[0])}, status = status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def siswa_list_published(request):
    siswa = Siswa.objects.filter(published=True)
    if request.method == 'GET':
        siswa_serializer = SiswaSerializer(siswa, many=True)
        return JsonResponse(siswa_serializer.data, safe=False)