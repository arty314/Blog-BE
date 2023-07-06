from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Blog, Category, Tag, Post, Comment
from .serializers import BlogSerializer, CategorySerializer, TagSerializer, PostSerializer, CommentSerializer

# blog create view
class BlogCreateView(APIView):
    def post(self, request):
        serializer = BlogSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(owner = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# blog detail view
class BlogDetailView(APIView):
    def get(request, pk):
        blogs = Blog.objects.get(pk)
        if blogs is not None():
            serializer = BlogSerializer(blogs)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

# blog update view
class BlogUpdateView(APIView):
    def put(request, pk):
        blogs = Blog.objects.get(pk)
        if blogs is not None:
            serializer = BlogSerializer(blogs, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# blog delete view
class BlogDeleteView(APIView):
    def delete(request, pk):
        blogs = request.get_object(pk)
        if blogs is not None:
            blogs.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

