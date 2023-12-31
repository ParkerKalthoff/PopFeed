from django.shortcuts import render, get_object_or_404
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from itertools import chain


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

# User Profile and Other User Apis ----------------

@api_view(['GET'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def following(request): 

    if request.method == 'GET':
        user = request.user

        following = UserFollowing.objects.all().filter(follower_id=user)
        following = [following.followee_id for following in following]
        following = [following.id for following in following]

        following_on = UserAccount.objects.all().filter(id__in=following)
        serializer = UserAccountSerializer(following_on, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

# Pop Getters --------------

    # Timeline with interactions ::  --------------

    # TODO: Return Pops that were liked by a user

    # TODO: Return Pops that were repopped by a user

    # Single Pop --------------


@api_view(['GET'])
def Pop(request, pop_id):

    if request.method == 'GET':
        pop = get_object_or_404(PopPosts, pk=pop_id)
        serializer = PopPostsSerializer(pop)
        return Response({"Pop": serializer.data})
    

    # Normal Timeline Pops --------------

@api_view(['GET'])
def anom_timeline(request, page):

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
def user_timelime(request, page): 

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

# TODO: v Return User specific Timeline that includes Repops v
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated])
def user_timelime_with_repops(request, page): 

    if request.method == 'GET':

        page = max(int(page), 1)
        start_index = (page - 1) * 10
        end_index = page * 10
        user = request.user

        following = UserFollowing.objects.all().filter(follower_id=user)
        following = [following.followee_id for following in following]
        following = [following.id for following in following]

        pops = PopPosts.objects.filter(user_id__in=following).order_by('-created_at')
        repops = PopRepop.objects.filter(user_id__in=following).order_by('-created_at')

        combined = sorted(
            chain(pops, repops),
            key=lambda instance: instance.created_at,
        )[start_index:end_index]


        print(combined, "combined length" , len(combined))

        timeline = []
        for item in combined:
            if isinstance(item, PopPosts):
                timeline.append(PopPostsSerializer(item).data)
            else:
                repop = PopRepopSerializer(item).data
                repop['pop'] = PopPostsSerializer(item.pop_id).data
                timeline.append(repop)

        return Response(timeline, status=status.HTTP_200_OK)

# Pop Interactions --------------

    # Like Functions --------------
@api_view(['GET', 'PUT'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated]) 
def like(request, pop_id):

    if request.method == 'GET':
        user = request.user
        likes = PopLikes.objects.all().filter(user_id=user)
        liked_pops = likes.filter(pop_id=pop_id)
        liked_pops.values_list('pop_id', flat=True)
        
        if liked_pops.exists():
            #serializer = PopLikesSerializer(liked_pops[0], many=False)
            serializer = { "pop_id": pop_id, "liked": True }
            return Response(serializer, status=status.HTTP_200_OK)
        else:
            serializer = { "pop_id": pop_id, "liked": False }
            return Response(serializer, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        user = request.user
        likes = PopLikes.objects.all().filter(user_id=user)
        liked_pop = likes.filter(pop_id=pop_id).values_list('pop_id', flat=True)

        if liked_pop.exists():
            # Unlike
            PopLikes.objects.filter(user_id=user, pop_id=pop_id).delete()
            serializer = { "pop_id": pop_id, "liked": False }
            return Response(serializer, status=status.HTTP_200_OK)
        else:
            # Like
            targetPop = PopPosts.objects.get(pk=pop_id)
            PopLikes.objects.create(user_id=user, pop_id=targetPop)
            serializer = { "pop_id": pop_id, "liked": True }
            return Response(serializer, status=status.HTTP_200_OK)
        
    # Repop Functions

@api_view(['GET', 'PUT'])
@authentication_classes([TokenAuthentication, SessionAuthentication])
@permission_classes([IsAuthenticated]) 
def repop(request, pop_id):

    if request.method == 'GET':
        user = request.user
        repops = PopRepop.objects.all().filter(user_id=user)
        repoped_pops = repops.filter(pop_id=pop_id)
        repoped_pops.values_list('pop_id', flat=True)
        
        if repoped_pops.exists():
            serializer = { "pop_id": pop_id, "repoped": True }
            return Response(serializer, status=status.HTTP_200_OK)
        else:
            serializer = { "pop_id": pop_id, "repoped": False }
            return Response(serializer, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        user = request.user
        repops = PopRepop.objects.all().filter(user_id=user)
        repoped = repops.filter(pop_id=pop_id).values_list('pop_id', flat=True)

        if repoped.exists():
            PopRepop.objects.filter(user_id=user, pop_id=pop_id).delete()
            serializer = { "pop_id": pop_id, "repoped": False }
            return Response(serializer, status=status.HTTP_200_OK)
        else:
            targetPop = PopPosts.objects.get(pk=pop_id)
            PopRepop.objects.create(user_id=user, pop_id=targetPop)
            serializer = { "pop_id": pop_id, "repoped": True }
            return Response(serializer, status=status.HTTP_200_OK)
        

# TODO: Profile changes
# TODO: Follow Function
# TODO: any more needed functions?