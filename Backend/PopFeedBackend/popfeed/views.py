from django.shortcuts import render
from django.http import JsonResponse
from .models import PopComments, PopLikes, PopPosts, PopRepop, CommentLikes, UserAccount, UserFollowing
from .serializers import PopCommentsSerializer, PopLikesSerializer, PopRepopSerializer, PopPostsSerializer, CommentLikesSerializer, UserAccountSerializer, UserFollowingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST'])
def Single_Pop(request):

    if request.method == 'GET': # Pop Getter
        posts = PopPosts.objects.all()
        serializer = PopPostsSerializer(posts, many=True)
        return JsonResponse({"Pops": serializer.data})
    
    if request.method == 'POST':
        serializer = PopPostsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# TODO: Make generic timeline api call
# TODO: Make User Specific timeline api call
# TODO: Make list of other needed functions