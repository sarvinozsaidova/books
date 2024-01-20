from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Books
from .serializers import BookSerializer
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
# from rest_framework import status
import jwt
from django.conf import settings
from rest_framework.viewsets import ModelViewSet



@api_view(['GET'])
def get_decode_token(request):
    decode_token = jwt.decode(request.META['HTTP_TOKEN'])
    return Response({'token': decode_token})


class BooksModelViewset(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer