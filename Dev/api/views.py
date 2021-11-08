from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from states.models import States
from .serializers import StateSerializer

@api_view(['GET'])
def get_all_states(request):
    states = States.objects.all()
    serializer = StateSerializer(states, many=True)

    return Response(serializer.data)



@api_view(['GET'])
def index(request):
    return HttpResponse("Hello, world. You're at the States index.")
    