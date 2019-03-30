from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from app.models import Url
import json


# GET  API to handle the short url redirection to the long url
# Redirection
@csrf_exempt
def redirection(request, num):
    url_objects = Url.objects.all()
    # check if the short url is present or not
    exists: str = ""
    for url_object in url_objects:
        if url_object.num == num:
            long_url = url_object.long_url
            exists += "exists"
            return HttpResponseRedirect(long_url)
        else:
            exists += "not exists"

    return HttpResponse("Short url you entered is not correct")


# Post API to get the long url entered by the user
@csrf_exempt
def url(request):
    if request.method == "POST":
        # Get the post data
        json_data = json.loads(request.body)
        long = json_data["long_url"]
        # For storing short url
        result = ""

        # Checking if long url exists in tha database
        for url_object in Url.objects.all():
            # If long url exists, saving the corresponding short url to the result
            if long == url_object.long_url:
                result += url_object.short_url
                break

        # If long url did not exists in the database, returns the short url
        if result == "":
            count = Url.objects.all().count()
            # Getting the short url from the method
            short_url = generate_url(count)
            url_object = Url()
            url_object.short_url = short_url
            url_object.long_url = long
            url_object.num = count+1
            # Saving data to the database
            url_object.save()
            result += short_url
        return HttpResponse(result)


# Method to generate the short url
# Alog:
# getting the count of the objects in the Url Model
# (this will show the number of urls in the database)
# and hence creating a unique url by incrementing the count by 1 everytime
def generate_url(count):
    return "http://localhost:8000/"+str(count+1)
