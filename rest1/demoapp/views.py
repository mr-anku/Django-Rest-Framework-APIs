
# from rest_framework.decorators import api_view
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework import viewsets

from demoapp.models import Post, User
from demoapp.serializers import PostSerializer, UserSerializer
from demoapp.pagination import MyPaginator

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = MyPaginator

""""Views Using GenericAPIView and Mixins"""
# class UserData(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

"""Function based Views"""
# @api_view(['GET',])
# def get_users(request):    
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users , many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         data = request.data
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {"msg":"Data saved successfully"}
#             return Response(res)
#         return Response({"msg":serializer.errors})

"""classbased view using APIView"""
# class UserData(APIView):
#     # authentication_classes = [BasicAuthentication]
#     # permission_classes = [IsAuthenticated]

#     def get(self,request,pk=None,format =None):
#         id = pk 

#         if id is not None:
#             users = User.objects.get(id = id)
#             serializer = UserSerializer(users , many=True)
#             return Response(serializer.data)

#         users = User.objects.all()
#         serializer = UserSerializer(users , many=True)
#         return Response(serializer.data)

#     def post(self,request,format =None):
        
#         data= request.data
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {"msg":"Data saved successfully"}
#             return Response(res)
