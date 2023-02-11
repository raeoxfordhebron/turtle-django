## Library for working with json
import json

def GetBody(request):
    # decode the request body into a unicode string
    unicode = request.body.decode('utf-8')
    # turn the unicode string into a python dictionary
    return json.loads(unicode)