from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import PopComments, PopLikes, PopPosts, PopRepop, CommentLikes, UserAccount, UserFollowing
from .serializers import PopCommentsSerializer, PopLikesSerializer, PopRepopSerializer, PopPostsSerializer, CommentLikesSerializer, UserAccountSerializer, UserFollowingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def Pop(request, pop_id):

    if request.method == 'GET': # Pop Getter
        pop = get_object_or_404(PopPosts, pk=pop_id)
        serializer = PopPostsSerializer(pop)
        return Response({"Pop": serializer.data})

@api_view(['GET'])
def Anom_timeline_pops(request, page):

    if request.method == 'GET':
        page = max(int(page), 1)
        start_index = (page - 1) * 10
        end_index = page * 10
        recent_pops = PopPosts.objects.all().order_by('-created_at')[start_index:end_index]
        serializer = PopPostsSerializer(recent_pops, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
             
# TODO: Make User Specific timeline api call
# TODO: Make list of other needed functions