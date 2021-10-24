from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@api_view(['POST'])
def userLogout(request):
    logout(request)
    return Response(({"message": "You were logout!"}))


@api_view(['POST'])
def userLogin(request):
    if request.method == "POST":
        username = request.data["username"]
        password = request.data["password"]

        user = authenticate(username=username, password=password)        
        if user is not None:
            login(request, user)
            detailUser = User.objects.get(username=username)
            serializer = UserSerializer(detailUser)
            return Response(serializer.data)
        else:
            return Response({
                "message": "Invalid username and/or password."
            })
    else:
        return Response({"message": "Please Login"})




@api_view(['POST'])
@permission_classes([AllowAny])
def userRegister(request):
    username = request.data["username"]
    email = request.data["email"]
    password = request.data["password"]
    confirmation = request.data["password2"]
    if password != confirmation:
        return Response({"message": "Passwords must match."})
    try:
        user = User.objects.create_user(username, email, password)
        user.save()        
        return Response(UserSerializer(user).data)
    except IntegrityError:
        return Response({"message": "Username already taken."})
    

