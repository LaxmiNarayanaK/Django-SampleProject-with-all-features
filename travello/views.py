from django.shortcuts import render,redirect
from .models import Destination
from django.contrib.auth.decorators import login_required
from . serializers  import DestinationSerializer
from rest_framework import generics
from .decorator import above18
from rest_framework import permissions

# Create your views here.

def index(request):

    dests = Destination.objects.all()

    return render(request, "index.html", {'dests': dests})

class DestinationList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]  # CAN BE USED FOR BOTH JWT AND TOKEN AUTHENTICATION(NRML LOGIN)
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]  # CAN BE USED FOR BOTH JWT AND TOKEN AUTHENTICATION(NRML LOGIN)
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

@login_required(login_url="/accounts/login")
@above18
def example(request):
    return render(request, "ex.html")


   