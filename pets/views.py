from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Turtle
from django.views import View
from .helper import GetBody
from django.core.serializers import serialize

# Create your views here.

class TurtleView(View):
    ## Index
    def get(self, request):
        all = Turtle.objects.all() # get all the turtle objects
        serialized = serialize("json", all) # turn objects into json strings
        finalData = json.loads(serialized) # turn json strings into dictionaries
        return JsonResponse(finalData, safe=False)
    
    ## Create
    def post(self, request):
        body = GetBody(request)
        turtle = Turtle.objects.create(name=body["name"], age=body["age"])
        finalData = json.loads(serialize("json", [turtle]))
        return JsonResponse(finalData, safe=False)

