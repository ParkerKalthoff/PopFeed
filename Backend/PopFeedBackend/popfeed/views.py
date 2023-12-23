from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, JsonResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.



# User Auth Apis ----------------
@api_view(['POST'])
def login(request):
    user = get_object_or_404(UserAccount, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"errors": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserAccountSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})

@api_view(['POST'])
def signup(request):
    serializer = UserAccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = UserAccount.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data})
    return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    print(request.user.is_authenticated)
    return Response("passed for {}".format(request.user.username))

# Pop Getters --------------


    # Single Pop --------------


@api_view(['GET'])
def Pop(request, pop_id):

    if request.method == 'GET':
        pop = get_object_or_404(PopPosts, pk=pop_id)
        serializer = PopPostsSerializer(pop)
        return Response({"Pop": serializer.data})
    

    # Timeline Pops --------------

@api_view(['GET'])
def Anom_timeline_pops(request, page):

    if request.method == 'GET':
        page = max(int(page), 1)
        start_index = (page - 1) * 10
        end_index = page * 10
        recent_pops = PopPosts.objects.all().order_by('-created_at')[start_index:end_index]
        serializer = PopPostsSerializer(recent_pops, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def user_timelime_pops(request, page): 

    if request.method == 'GET':
        page = max(int(page), 1)
        start_index = (page - 1) * 10
        end_index = page * 10
        user = request.user
        following = UserFollowing.objects.all().filter(follower_id=user)
        following = [following.followee_id for following in following]
        following = [following.id for following in following]
        recent_pops = PopPosts.objects.filter(user_id__id__in=following).order_by('-created_at')[start_index:end_index]
        serializer = PopPostsSerializer(recent_pops, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

# TODO: Make list of other needed functions