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

class TurtleViewID(View):
    ## Show
    def get(self, request, id):
        ## get the turtle
        turtle = Turtle.objects.get(id=id)
        ## serialize then turn into dictionary
        finalData = json.loads(serialize("json", [turtle]))
        ## send json response
        return JsonResponse(finalData, safe=False)
    
    def put(self, request, id):
        ## get the body
        body = GetBody(request)
        ## update turtle
        ## ** is like JS spread operator
        Turtle.objects.filter(id=id).update(**body)
        ## query for turtle
        turtle = Turtle.objects.get(id=id)
        ## serialize and make dictionary
        finalData = json.loads(serialize("json", [turtle]))
        ## return json data
        return JsonResponse(finalData, safe=False)
